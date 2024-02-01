from marshmallow import Schema, fields
from flask import request, Response, Blueprint

import base64
from io import BytesIO
from typing import List

import torch
from diffusers import StableDiffusionPipeline


######################################################################################

#   Model pre-loaded (within image) using model_initializer.py

model_id = "runwayml/stable-diffusion-v1-5"

device = "cuda" if torch.cuda.is_available() else "cpu"
device = "mps" if torch.backends.mps.is_available() else "cpu"


if device != "cpu":
    #   for faster inference
    model_args = {
        "variant": "fp16",
        "torch_dtype": torch.float16,
        "use_safetensors": True
    }
else:
    model_args = {
        "use_safetensors": True
    }

pipe = StableDiffusionPipeline.from_pretrained(model_id, **model_args)


pipe = pipe.to(device)

if device == 'cpu':
    pipe.enable_attention_slicing()

######################################################################################

image_resource = Blueprint(name='image_resource',
                           import_name=__name__)

class ResponseSchema(Schema):
    class Meta:
        ordered = True

    image_string = fields.Str(required=True)


@image_resource.route('', methods=['POST'])
def post():

    data = request.get_json()

    prompt_string = data.get('prompt')
    negative_prompt_string = data.get('negative_prompt')

    #   Call the image generation function

    generated_image = get_image_for_prompt(prompt_string=prompt_string, 
                                           negative_prompt_string=negative_prompt_string)

    
    return Response(response=ResponseSchema().dumps(generated_image), status=201)


def get_image_for_prompt(prompt_string: str, negative_prompt_string: str) -> dict:
    #   Generate the image and return as base64 string

    #width = 256
    #height = 256
    #num_inference_steps = 50

    #   returns Pillow image
    img = pipe(prompt=prompt_string, 
               negative_prompt=negative_prompt_string).images[0]  

    buffered = BytesIO()
    img.save(buffered, format='JPEG')

    image_string = base64.b64encode(buffered.getvalue()).decode("utf-8")

    image = {
        'image_string': image_string
    }

    return image

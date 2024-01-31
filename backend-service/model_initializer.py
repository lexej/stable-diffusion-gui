from diffusers import StableDiffusionPipeline

model_id = "runwayml/stable-diffusion-v1-5"

#   Only for downloading an storing the model
pipe = StableDiffusionPipeline.from_pretrained(model_id, use_safetensors=True)

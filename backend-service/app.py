from flask import Flask

from image_resource import image_resource

app = Flask(__name__)

app.register_blueprint(image_resource, url_prefix='/api/image/')


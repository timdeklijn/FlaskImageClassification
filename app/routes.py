import os

import requests
from flask import render_template, request
from tensorflow.keras.preprocessing.image import load_img

from app import app
from app.inference import process_image, do_inference, load_model

print("[MODEL] loading model...")
# load model
model = load_model()
print("[MODEL] model loaded...")
# temporary image path
image_path = os.path.join("app", "model", "tmp.jpg")


@app.route("/inference")
def infer():
    """
    Download an image from given URL, save it and perform inference
    on the inference.

    example url:

        /inference?url=http://www.....

    Returns
    -------
    label: str
        Result of VGG16 inference
    """
    # Get URL from request
    # TODO: make form
    url = request.args.get("url")
    # Download and load image into keras
    resp = requests.get(url, stream=True)
    image = load_img(resp.raw, target_size=(224, 224))
    # process image and do inference
    image = process_image(image)
    param = {"preds": do_inference(model, image), "url": url}
    return render_template("index.html", param=param)


@app.route("/")
@app.route("/index")
def index():
    user = {"username": "TIM"}
    return render_template("index.html", user=user)

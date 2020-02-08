import os

import requests
from flask import render_template, request, url_for, redirect
from tensorflow.keras.preprocessing.image import load_img

from app import app
from app.inference import process_image, do_inference, load_model
from app.forms import URLForm

print("[MODEL] loading model...")
# load model
model = load_model()
print("[MODEL] model loaded...")
# temporary image path
image_path = os.path.join("app", "model", "tmp.jpg")

# For authentication
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY


@app.route("/", methods=("GET", "POST"))
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
    param = {"preds": "", "url": "", "form": ""}
    if request.method == "POST":
        param["form"] = URLForm()
        param["url"] = request.form.get("url")
        resp = requests.get(param["url"], stream=True)
        image = load_img(resp.raw, target_size=(224, 224))
        image = process_image(image)
        param["preds"] = do_inference(model, image)
    return render_template("index.html", param=param)

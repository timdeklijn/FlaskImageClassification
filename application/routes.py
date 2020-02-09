import ast

import requests
from flask import render_template, request, redirect, url_for, Blueprint
from tensorflow.keras.preprocessing.image import load_img

from application.forms import URLForm
from application.inference import process_image, do_inference, load_model

print("[MODEL] loading model...")
model = load_model()
print("[MODEL] model loaded...")

ml_app = Blueprint("ml_app", __name__)


@ml_app.route("/", methods=("GET",))
def infer():
    """
    If post reques

    Returns
    -------
    renders template
    """
    param = {"preds": "", "url": "", "form": URLForm()}
    if request.method == "GET":
        try:
            p = ast.literal_eval(request.args.get('data'))  # Convert request string to dict
            param["url"] = p["url"]
            param["preds"] = ", ".join(p["preds"])
        except:
            print("[ERROR] failed parsing request dict.")
    return render_template("index.html", param=param)


@ml_app.route("/classify", methods=("GET", "POST"))
def classify_image():
    """
    Classify an image based on URL

    Get url from request, download bytes, load into Keras and classify.

    :return:
    redirect with or without prediction data
    """
    if request.method == "POST":
        url = request.form.get("url")
        try:
            response = requests.get(url, stream=True)
            image = load_img(response.raw, target_size=(224, 224))
            image = process_image(image)
            predictions = do_inference(model, image)
            return redirect(url_for("ml_app.infer", data={"preds": predictions, "url": url}))
        except:
            print("[ERROR] Failed to parse image from url.")
    return redirect(url_for("ml_app.infer"))

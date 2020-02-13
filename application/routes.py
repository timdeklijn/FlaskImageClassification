import requests
from flask import render_template, request, redirect, url_for, Blueprint
from tensorflow.keras.preprocessing.image import load_img

from application.forms import URLForm
from application.inference import process_image, do_inference, load_model

print("[LOG] loading model...")
model = load_model()
print("[LOG] model loaded...")

print("[LOG] creating blueprint")
ml_app = Blueprint("ml_app", __name__)
print("[LOG] done creating blueprint")


@ml_app.route("/", methods=("GET", "POST"))
def index():
    """
    Show landing page, if button is pressed, redirect to inference or error
    page

    Returns
    -------
    render_tempalte or redirect
    """
    print("[LOG] Index route")
    form = URLForm()
    if request.method == "POST":
        return redirect(url_for("ml_app.infer", url=request.form["url"]))
    return render_template("index.html", form=form)


@ml_app.route("/infer", methods=("GET", "POST"))
def infer():
    """
    Handle inference requests. Load image from url, convert to NN input and perform
    inference. Based on results redirect to error page or show result. Also handle new
    for events.


    Returns
    -------
    redirect or render_template
    """

    # Handle button press
    print("[LOG] infer route")
    form = URLForm()
    if request.method == "POST":
        return redirect(url_for("ml_app.infer", url=request.form["url"]))
    # Get URL from request and perform inference on the model
    print("[LOG] Starting inference")
    url = request.args.get('url')
    try:
        # Perform inference
        response = requests.get(url, stream=True)
        image = load_img(response.raw, target_size=(224, 224))
        image = process_image(image)
        predictions = do_inference(model, image)
        return render_template("predicted.html", param={
            "form": URLForm(),
            "preds": ", ".join(predictions).replace("_", " "),
            "url": url})
    except Exception as e:
        print(f"[ERROR] Exception in inference: {e}")
        return redirect(url_for("ml_app.error"))


@ml_app.route("/error", methods=("GET", "POST"))
def error():
    """
    Show the error page, if another URL is passed, check if it is valid and
    redirect to inference page

    Returns
    -------
    render_template or redirect
    """
    form = URLForm()
    if request.method == "POST":
        if form.validate_on_submit():
            return redirect(url_for("ml_app.infer", url=request.form["url"]))
    return render_template("error.html", form=URLForm())

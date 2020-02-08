from flask_wtf import FlaskForm
from flask_wtf.html5 import URLField
from wtforms.validators import url


class URLForm(FlaskForm):
    url = URLField("image URL", validators=[url()])


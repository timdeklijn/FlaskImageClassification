from flask_wtf import FlaskForm
from wtforms.fields.html5 import URLField
from wtforms.validators import url


class URLForm(FlaskForm):
    url = URLField("image URL", validators=[url()])


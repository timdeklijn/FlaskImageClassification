import os

import numpy as np
from tensorflow import keras
from tensorflow.keras.applications.vgg16 import decode_predictions


def load_model():
    return keras.models.load_model("vgg16.h5py")


def process_image(img):
    """
    Process image to a np array of the correct shape

    Parameters
    ----------
    img: keras loaded image

    Returns
    -------
    img: np.array
        processed image

    """
    img = np.array(img)
    return img.reshape((1,) + img.shape)


def do_inference(mdl, img):
    """
    Perform inference on input image, return label with highest score

    Parameters
    ----------
    mdl: keras.model vgg16
    img: image array of shape (1,224,224)

    Returns
    -------
    label: string
    """
    labels = decode_predictions(mdl.predict(img))
    result = []
    for i in range(5):
        result.append(labels[0][i][1])
    return result

import os

import tensorflow as tf


def download_model():
    """
    Download the VGG16 model weights and save the model
    Returns
    -------
    None
    """
    print("[-] Starting to download model..")
    model = tf.keras.applications.VGG16(
        include_top=True,
        weights='imagenet',
        input_tensor=None,
        input_shape=None,
        pooling=None,
        classes=1000
    )
    model.save(os.path.join("model", "vgg16.h5"))
    print("[-] Model saved.")


if __name__ == "__main__":
    download_model()

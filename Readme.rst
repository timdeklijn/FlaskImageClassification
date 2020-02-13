Flask Image Classification
==========================

A flask app around an image classification Neural network. Past an image URL into the textbox and see what a state
of the art image recognition neural network thinks is in the image.

Install
-------

Simply build the docker container:

.. code-block::

    docker build --tag flask-image .

And run it by:

.. code-block::

    docker run -t --gpus all -p 8008:8008 flask-image

Check the browser on http://localhost:8008

If running localy, add tensorflow to the requirements file. This is not needed for the containerization since the
base image as a docker container. On another note, Pillow is required but never mentioned in the code.

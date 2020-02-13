FROM tensorflow/tensorflow:2.0.1-gpu-py3
COPY requirements.txt requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt \
    && rm requirements.txt
COPY . /app
WORKDIR /app
EXPOSE 8008
CMD python wsgi.py
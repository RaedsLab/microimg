from flask import Flask
from flask import request
from flask import jsonify

from PIL import Image
import requests
from io import BytesIO
import io
import binascii

import timeit

size = 42, 42

app = Flask(__name__)


@app.route("/", methods=['GET'])
def hello():
    return "[POST] /v0/ -F image"


@app.route("/v0/", methods=['POST'])
def v0():
    imageURL = request.values.get('image')
    if imageURL is None:
        return jsonify(status="error",
                       message="Image parameter required")

    try:
        load_start_time = timeit.default_timer()
        sourceImage = requests.get(imageURL)
        img = Image.open(BytesIO(sourceImage.content))
        load_elapsed = timeit.default_timer() - load_start_time

        process_start_time = timeit.default_timer()
        output = io.BytesIO()
        img = img.resize(size, Image.ANTIALIAS)
        img.save(output, format='JPEG', optimize=True, quality=30)

        bytes_data = output.getvalue()
        im_hex = binascii.hexlify(bytes_data)

        # remove headers
        im_header_hex = im_hex[0:360]
        im_body_hex = im_hex.replace('im_header_hex', '')

        # remove trailing FF D9
        im_body_hex = im_body_hex.replace('ffd9', '')

        im_body_base64 = im_body_hex.decode("hex").encode("base64")
        im_header_base64 = im_header_hex.decode("hex").encode("base64")

        process_elapsed = timeit.default_timer() - process_start_time

        return jsonify(status="ok",
                       header=im_header_base64,
                       data=im_body_base64,
                       load_time=load_elapsed,
                       process_time=process_elapsed)

    except IOError:
        return jsonify(status="error",
                       message="Error parsing image")

if __name__ == "__main__":
    app.run()

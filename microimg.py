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
        im_hex = im_hex.replace('ffd8ffe000104a46494600010100000100010000ffdb0043001b12141714111b1716171e1c1b2028422b28252528513a3d3042605565645f555d5b6a7899816a7190735b5d85b586909ea3abadab6780bcc9baa6c799a8aba4ffdb0043011c1e1e2823284e2b2b4ea46e5d6ea4a4a4a4a4a4a4a4a4a4a4a4a4a4a4a4a4a4a4a4a4a4a4a4a4a4a4a4a4a4a4a4a4a4a4a4a4a4a4a4a4a4a4a4a4a4a4a4a4a4ffc0001108002a002a03012200021101031101ffc400', '')
        im_base64 = im_hex.decode("hex").encode("base64")
        process_elapsed = timeit.default_timer() - process_start_time

        return jsonify(status="ok",
                       data=im_base64,
                       load_time=load_elapsed,
                       process_time=process_elapsed)

    except IOError:
        return jsonify(status="error",
                       message="Error parsing image")

if __name__ == "__main__":
    app.run()

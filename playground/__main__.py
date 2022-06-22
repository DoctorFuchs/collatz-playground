from flask import Flask, request, send_from_directory
from .collatz_image_generator import generate_image

app = Flask(__name__)

@app.route("/<path:path>")
def index(path):
    return send_from_directory("./public", path)

@app.route("/generator/", methods=["POST", "GET"])
def get_image():
    assert set(["min", "max"]).issubset(set(request.values.keys())), "Parameters didn't match"
    try:
        MINIMUM = int(request.values["min"])
        MAXIMUM = int(request.values["max"])
    except TypeError:
        assert False, "min and max need to be numbers"

    assert MINIMUM > 0, "Minmum needs to be higher than 0"
    assert MAXIMUM <= 100000, "Maximum needs to be lower"
    assert MINIMUM < MAXIMUM, "Maximum needs to be higher than the minimum"

    return f"""data:image/png;base64,{generate_image(MINIMUM, MAXIMUM).decode("utf-8")}"""

if __name__ == "__main__":
    app.run("0.0.0.0", 3000, debug=True)
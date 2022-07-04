from flask import Flask, jsonify, redirect, request, send_from_directory

from .calculator import calculator
from .collatz_image_generator import generate_image

app = Flask(__name__)

@app.errorhandler(AssertionError)
def errorHandler(e):
    return str(e), 404

@app.route("/")
def default_entry():
    return redirect("/index.html")

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
        assert False, "min und max müssen natürliche Nummern sein"
    
    except ValueError:
        assert False, "Leere Werte können nicht berechnet werden!"

    assert MINIMUM > 0, "Das Minmum muss höher als 0 sein"
    assert MAXIMUM <= 1000000, "Das Maximum muss kleiner sein"
    assert MINIMUM < MAXIMUM, "Das Maximum muss höher als das Minimum sein"

    return f"""data:image/png;base64,{generate_image(MINIMUM, MAXIMUM).decode("utf-8")}"""

@app.route("/calculator/", methods=["POST", "GET"])
def calculate():
    try:
        NUMBER = int(request.values["num"])
    except TypeError:
        assert False, "Die Nummer muss natürlich sein"

    except ValueError:
        assert False, "Leere Werte können nicht berechnet werden!"

    return jsonify(calculator(NUMBER))

if __name__ == "__main__":
    app.run("0.0.0.0", 3000, debug=True)
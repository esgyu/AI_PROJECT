from flask import Flask, render_template, Response, redirect
from flask import request, jsonify, make_response
import cv2
import time

app = Flask(__name__)

@app.route('/')
def index():
    """Video streaming home page."""
    return render_template('index.html')

@app.route("/guestbook")
def guestbook():
    return render_template("public/guestbook.html")

@app.route("/guestbook/create-entry", methods=["POST"])
def create_entry():

    req = request.get_json()

    print(req)

    res = make_response(jsonify({"message": "OK"}), 200)

    return res

if __name__ == '__main__':
    app.run(debug=True, threaded=True)

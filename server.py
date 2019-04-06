from flask import (Flask, render_template, redirect, request, flash, session, jsonify, url_for)

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("index.html")


if __name__ == '__main__':
    app.debug = True
    app.run(port=5000, host='0.0.0.0')

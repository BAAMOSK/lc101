from flask import Flask, render_template, request
from caesar import rotate_character

app = Flask(__name__)

@app.route('/', methods=["POST"])
def index():
    return render_template("index.html")

if( __name__ == "__main__"):
    app.run()

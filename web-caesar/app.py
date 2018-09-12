from flask import Flask, render_template, request
from caesar import rotate_character

app = Flask(__name__)

@app.route('/', methods=["POST"])
def index(rot, text):
    rot = int(rot)
    text = chr(text)
    encrypted = text(rotate_character)
    return render_template("index.html", text=encrypted)

if( __name__ == "__main__"):
    app.run()

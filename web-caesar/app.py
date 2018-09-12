from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from caesar import rotate_character

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    #data = request.get('rot');
    #print(request)
    print("This is after the request")
    #rot = int(rot)
    #text = chr(text)
    #encrypted = text(rotate_character)
    return render_template("index.html")


if( __name__ == "__main__"):
    app.run()

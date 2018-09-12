from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from caesar import rotate_character

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    data = request.form.get('rot');
    print(data)
    #rot = int(rot)
    #text = chr(text)
    #encrypted = text(rotate_character)
    return render_template("index.html", data=data)


if( __name__ == "__main__"):
    app.run()

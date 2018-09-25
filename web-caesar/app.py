from flask import Flask, render_template, request, url_for
from flask_wtf import FlaskForm
from caesar import rotate_string

app = Flask(__name__)

main = '''
<!DOCTYPE html>
    <html>
        <head>
            <style>
                form {{
                    background-color: #eee;
                    padding: 20px;
                    margin: 0 auto;
                    width: 540px;
                    font: 16px sans-serif;
                    border-radius: 10px;
                }}
                textarea {{
                    margin: 10px 0;
                    width: 540px;
                    height: 120px;
                }}
            </style>
        </head>
        <body>
          <!-- create your form here -->
          <form action="/encrypt" method="POST">
            <label for="rot">Rotate by: </label>
            <input id="rot" name="rot"></input>
            <textarea id="text" name="text">{value}</textarea>
            <button type="submit">SUBMIT</button>
          </form>
        </body>
    </html>
'''

@app.route('/', methods=["POST", "GET"])
def index():
    #data = request.get('rot');
    #print(request)
    #print("This is after the request")
    #rot = int(rot)
    #text = chr(text)
    #encrypted = text(rotate_character)
    #return render_template("index.html")
    return main.format(rot=8,value="Cat")

@app.route('/encrypt')
def encrypt(rot, text):
    #value = request.get('rot')
    print(rot, text)
    return main.format(value=value) 

if( __name__ == "__main__"):
    app.run()

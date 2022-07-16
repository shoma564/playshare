from flask import Flask, render_template, request
from flask_socketio import SocketIO, send, emit
import webbrowser


app = Flask(__name__, static_folder='./templates/img')


@app.route('/')
def index():
    global name
    return render_template("index.html",name = name)



@app.route('/name', methods=["POST"])
def name():
    global name
    name = request.form["name"]
    webbrowser.open(name)
    return render_template("name.html", name = name)



if __name__ == "__main__":
    app.run(host="0.0.0.0")


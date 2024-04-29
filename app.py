from flask import Flask, render_template
from flask_socketio import SocketIO, send, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

socketio = SocketIO(app)

@app.route("/")
def index():
    return render_template("index.html")

@socketio.on('message')
def handle_msg(message):
    print("received msg " + message)
    send(message, broadcast=True)

@socketio.on('image')
def handle_img(image_data):
    print("received img" + image_data)
    emit('image', image_data, broadcast=True)
    print("image data:", image_data)

@socketio.on('document')
def handle_doc(document_data):
    emit('document', document_data, broadcast=True)

@socketio.on('emoji')
def handle_emoji(emoji):
    emit('emoji', emoji, broadcast=True)

if __name__ == "__main__":
    app.debug = True
    socketio.run(app)

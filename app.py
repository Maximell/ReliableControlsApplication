#!/usr/bin/env python
from flask import Flask, render_template
from flask_socketio import SocketIO, send
from models.Models import db, Device

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./temp/test.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['debug'] = True

    db.init_app(app)

    return app

app = create_app()
with app.app_context():
    db.create_all()
socketio = SocketIO(app)

@app.route('/')
def hello_world():
  return render_template('index.html')

@socketio.on('getFaultCounts')
def handle_message(message):
    deviceList = Device.query.all()
    result = []
    for device in deviceList:
        result.append(device.serialize())
    send({
        "faultList": result
    });


if __name__ == '__main__':
  socketio.run(app)

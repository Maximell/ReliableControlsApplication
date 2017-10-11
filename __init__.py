#!/usr/bin/env python
from flask import Flask, render_template
from models.Models import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./temp/test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.route('/')
def hello_world():
  return render_template('index.html')

if __name__ == '__main__':
  app.run(debug=True)

from flask import render_template, request, redirect
from flask_app import app
from flask_app.models.burger import Burger

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/create', methods=['POST'])
def create():
    data = {
        "name": request.form['name'],
        "bun": request.form['bun'],
        "meat": request.form['meat'],
        "calories": request.form['calories']
    }
    Burger.save(data)
    return redirect('/burgers')

@app.route('/burgers')
def burgers():
    return "Hello World"
from flask import render_template, request, redirect
from flask_app import app
from flask_app.models.burger import Burger


@app.route('/burgers')
def burgers():
    burgers = Burger.get_all() 
    return render_template('index.html', burgers = burgers)

# @app.route('/burgers/new')
# def new_burger():
#     return render_template("new_burger.html")

@app.route('/burgers/new', methods=['GET','POST'])
def new_burger():
    # POST REQUEST
    if request.method == "POST":
        data = {
            "name": request.form['name'],
            "bun": request.form['bun'],
            "meat": request.form['meat'],
            "calories": request.form['calories']
        }
        Burger.save(data)
        return redirect(f'/burgers')
    
    # GET REQUEST
    return render_template("new_burger.html")

@app.route('/burgers/<int:burger_id>/edit', methods=['GET','POST'])
def edit_burger(burger_id):
    # POST REQUEST 
    if request.method == 'POST':
       data = {
            'id': burger_id,
            "name":request.form['name'],
            "bun": request.form['bun'],
            "meat": request.form['meat'],
            "calories": request.form['calories']
        }
       Burger.update(data)
       return redirect("/burgers")
    
    # GET REQUEST
    else:   
        data = {
            'id': burger_id
        }
        burger = Burger.get_one(data)
        return render_template("edit_burger.html", burger=burger)

@app.route('/burgers/<int:burger_id>/delete')
def delete_burger(burger_id):
    data = {
        'id': burger_id,
    }
    Burger.destroy(data)
    return redirect('/burgers')
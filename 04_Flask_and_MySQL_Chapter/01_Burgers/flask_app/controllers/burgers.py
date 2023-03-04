from flask import render_template, request, redirect
from flask_app import app
from flask_app.models.burger import Burger
from flask_app.models.restaurant import Restaurant
from flask_app.models.topping import Topping

@app.route('/')
def index():
    return redirect('/burgers')

@app.route('/burgers')
def burgers():
    burgers = Burger.get_all() 
    return render_template('index.html', burgers = burgers)

@app.route('/burgers/<int:burger_id>')
def burger_details(burger_id):
    data = {
        'id': burger_id
    }
    burger = Burger.get_one_with_toppings(data)
    data_2 = {
        'id': burger.restaurant_id
    }
    restaurant = Restaurant.get_one(data_2)
    unselected_toppings = Topping.get_unselected_toppings(data)
    return render_template('burger_details.html', burger = burger, restaurant=restaurant, unselected_toppings=unselected_toppings)

@app.route('/burgers/new', methods=['GET','POST'])
def new_burger():
    # POST REQUEST
    if request.method == "POST":
        data = {
            "name": request.form['name'],
            "bun": request.form['bun'],
            "meat": request.form['meat'],
            "calories": request.form['calories'],
            "restaurant_id": request.form['restaurant_id']
        }
        if not Burger.validate_burger(data):
            return redirect("/burgers/new")
        Burger.save(data)
        return redirect(f'/burgers')
    
    # GET REQUEST
    restaurants = Restaurant.get_all()
    return render_template("new_burger.html", restaurants=restaurants)

@app.route('/burgers/<int:burger_id>/edit', methods=['GET','POST'])
def edit_burger(burger_id):
    # POST REQUEST 
    if request.method == 'POST':
       data = {
            'id': burger_id,
            "name":request.form['name'],
            "bun": request.form['bun'],
            "meat": request.form['meat'],
            "calories": request.form['calories'],
            "restaurant_id": request.form['restaurant_id']
        }
       if not Burger.validate_burger(data):
            return redirect(f"/burgers/{burger_id}/edit")
       Burger.update(data)
       return redirect("/burgers")
    
    # GET REQUEST
    data = {
        'id': burger_id
    }
    burger = Burger.get_one(data)
    restaurants = Restaurant.get_all()
    return render_template("edit_burger.html", burger=burger, restaurants=restaurants)

@app.route('/burgers/<int:burger_id>/delete')
def delete_burger(burger_id):
    data = {
        'id': burger_id,
    }
    Burger.destroy(data)
    return redirect('/burgers')

@app.route('/burgers/add/toppings',methods=['POST'])
def add_topping_to_burger():
    data = {
        'burger_id': request.form['burger_id'],
        'topping_id': request.form['topping_id']
    }
    Burger.add_topping(data)
    return redirect(f"/burgers/{request.form['burger_id']}")

@app.route('/burgers/<int:burger_id>/remove/toppings/<int:topping_id>')
def remove_topping_from_burger(burger_id, topping_id):
    data = {
        'burger_id': burger_id,
        'topping_id': topping_id
    }
    Burger.remove_topping(data)
    return redirect(f"/burgers/{burger_id}")
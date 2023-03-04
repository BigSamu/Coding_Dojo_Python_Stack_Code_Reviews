from flask import render_template, request, redirect
from flask_app import app
from flask_app.models.topping import Topping
from flask_app.models.burger import Burger

@app.route('/toppings/<int:topping_id>')
def topping_details(topping_id):
    data = {
        'id': topping_id
    }
    topping = Topping.get_one_with_burgers(data)
    unselected_burgers = Burger.get_unselected_burgers(data)
    return render_template('topping_details.html', topping = topping, unselected_burgers=unselected_burgers)

@app.route("/toppings/new", methods=["GET", "POST"])
def new_topping():
    # POST REQUEST
    if request.method == "POST":
        data = {
            "name": request.form["name"],
        }
        if not Topping.validate_topping(data):
            return redirect("/toppings/new")
        Topping.save(data)
        return redirect(f"/toppings/new")

    # GET REQUEST
    toppings = Topping.get_all()
    return render_template("new_topping.html", toppings=toppings)

@app.route('/toppings/<int:topping_id>/delete')
def delete_topping(topping_id):
    data = {
        'id': topping_id,
    }
    Topping.destroy(data)
    return redirect('/toppings/new')

@app.route('/toppings/add/burgers',methods=['POST'])
def add_burger_to_topping():
    data = {
        'burger_id': request.form['burger_id'],
        'topping_id': request.form['topping_id']
    }
    Topping.add_burger(data)
    return redirect(f"/toppings/{request.form['topping_id']}")

@app.route('/toppings/<int:topping_id>/remove/burgers/<int:burger_id>')
def remove_burger_from_topping(burger_id, topping_id):
    data = {
        'burger_id': burger_id,
        'topping_id': topping_id
    }
    Topping.remove_burger(data)
    return redirect(f"/toppings/{topping_id}")
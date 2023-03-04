from flask import render_template, request, redirect
from flask_app import app
from flask_app.models.burger import Burger
from flask_app.models.restaurant import Restaurant


@app.route("/restaurants/<int:restaurant_id>")
def restaurant_details(restaurant_id):
    data = {
        'id': restaurant_id
    }
    restaurant = Restaurant.get_one_with_burgers(data)
    return render_template("restaurant_details.html", restaurant=restaurant)


@app.route("/restaurants/new", methods=["GET", "POST"])
def new_restaurant():
    # POST REQUEST
    if request.method == "POST":
        data = {
            "name": request.form["name"],
        }
        if not Restaurant.validate_restaurant(data):
            return redirect("/restaurants/new")
        Restaurant.save(data)
        return redirect(f"/restaurants/new")

    # GET REQUEST
    restaurants = Restaurant.get_all()
    return render_template("new_restaurant.html", restaurants=restaurants)


@app.route('/restaurants/<int:restaurant_id>/delete')
def delete_restaurant(restaurant_id):
    data = {
        'id': restaurant_id,
    }
    Restaurant.destroy(data)
    return redirect('/restaurants/new')
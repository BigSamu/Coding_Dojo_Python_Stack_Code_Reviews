from flask import render_template, request, redirect, session, flash
from flask_app import app
from flask_app.models.user import User
from flask_app.models.ride import Ride

@app.route("/rides/dashboard")
def rides_dashboard():
    if 'user_id' not in session:
        return redirect('/')
    data = {
        "id": session['user_id']
    }
    rider = User.get_one(data)
    rides = Ride.get_all()

    # rides_without_driver = [r for r in rides if r.driver == None]
    # rides_with_driver = [r for r in rides if r.driver != None]

    rides_without_driver = []
    rides_with_driver = []
    for r in rides:
        print(r.rider)
        print(r.driver)
        if(r.driver == None):
            rides_without_driver.append(r)
        else:
            rides_with_driver.append(r)

    # users = User.get_all()
    return render_template("dashboard.html",rider=rider, rides_without_driver=rides_without_driver)

@app.route('/rides/new',methods=['GET','POST'])
def new_ride():
    # POST REQUEST
    if request.method == "POST":
        Ride.save(request.form)
        return redirect('/rides/dashboard')
    
    # GET REQUEST
    if 'user_id' not in session:
        return redirect('/')
    return render_template("new_ride.html")

@app.route('/rides/<int:ride_id>/delete')
def delete_ride(ride_id):
    data = {
        'id': ride_id,
    }
    Ride.destroy(data)
    return redirect('/rides/dashboard')
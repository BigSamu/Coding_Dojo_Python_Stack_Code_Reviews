from flask import render_template, request, redirect, session, flash
from flask_app import app
from flask_app.models.user import User
from flask_app.models.ride import Ride

@app.route('/rides/new',methods=['GET','POST'])
def new_ride():
    # POST REQUEST
    if request.method == "POST":
        pass
        # Ride.save(data)
        return redirect('/rides/dashboard')
    
    # GET REQUEST
    if 'user_id' not in session:
        return redirect('/')
    return render_template("new_ride.html")
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Ride:
    db_name = 'ohana_rideshares'
    def __init__(self,db_data):
        self.id = db_data['id']
        self.destiantion = db_data['destiantion']
        self.pick_up_location = db_data['pick_up_location']
        self.rideshare_date = db_data['rideshare_date']
        self.details = db_data['details']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']

        self.rider_id = db_data['rider_id']
        self.driver_id = db_data['driver_id']
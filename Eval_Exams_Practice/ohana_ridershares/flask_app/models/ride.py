from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Ride:
    db_name = 'ohana_rideshares'
    def __init__(self,db_data):
        self.id = db_data['id']
        self.destination = db_data['destination']
        self.pick_up_location = db_data['pick_up_location']
        self.rideshare_date = db_data['rideshare_date']
        self.details = db_data['details']
        self.rider_id = db_data['rider_id']
        self.driver_id = None
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']

        self.rider = db_data.get('rider', None)
        self.driver = db_data.get('driver', None)

    # 1) READ OPERATIONS
    # 1.1) Get All Rides with rider and driver
    @classmethod
    def get_all(cls):
        query =  "SELECT * FROM rides LEFT JOIN users AS riders ON riders.id = rides.rider_id LEFT JOIN users AS drivers ON drivers.id = rides.driver_id;"
        results = connectToMySQL(cls.db_name).query_db(query)
        rides = []
        for row in results:
            if row['drivers.first_name']:
                driver = row['drivers.first_name'] + " " + row['drivers.last_name']
            else:
                driver = None
            
            data = {
                "id" : row["id"],
                "destination" : row['destination'],
                "pick_up_location" : row['pick_up_location'],
                "rideshare_date" : row['rideshare_date'],
                "details" : row['details'],
                "rider_id" : row['rider_id'],
                "driver_id" : row['driver_id'],
                "created_at" : row['created_at'],
                "updated_at" : row['updated_at'],
                "rider" : row['first_name'] + " " + row['last_name'],
                "driver" : driver
            }
            rides.append( cls( data ) )
       
        return rides

    # 2) CREATE OPERATIONS
    # 2.1) Create Ride
    @classmethod
    def save(cls, data):
        query = "INSERT INTO rides (destination,pick_up_location,rideshare_date,details,rider_id,driver_id,created_at,updated_at)\
              VALUES (%(destination)s,%(pick_up_location)s ,%(rideshare_date)s,%(details)s,%(rider_id)s,NULL,NOW(),NOW());"
        # data is a dictionary that will be passed into the save method from server.py
        results = connectToMySQL(cls.db_name).query_db(query, data) 
        print(results)
        return results
    
    # 4) DELETE OPERATIONS
    # 4.1) Delete Ride
    @classmethod
    def destroy(cls, data):
        query = "DELETE FROM rides WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query, data)
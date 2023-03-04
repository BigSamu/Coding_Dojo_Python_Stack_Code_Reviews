from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import topping
from flask import flash

class Burger:
    def __init__(self,data):
        self.id = data["id"]
        self.name = data["name"]
        self.bun = data["bun"]
        self.meat = data["meat"]
        self.calories = data["calories"]
        self.restaurant_id = data["restaurant_id"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.toppings = []
       
    # 1) READ OPERATIONS
    # 1.1) Get All Burgers without Topings
    @classmethod
    def get_all(cls):
        query =  "SELECT * FROM burgers;"
        results = connectToMySQL("burgers_db").query_db(query)
        burgers = []
        for burger in results:
            burgers.append(cls(burger))
        return burgers
 
    # 1.2) Get One Burger without Topings
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM burgers WHERE id=%(id)s;"
        results = connectToMySQL("burgers_db").query_db(query, data)
        return cls(results[0])
    
    # 1.3) Get One Burger with Topings
    @classmethod
    def get_one_with_toppings( cls , data ):
        query = "SELECT * FROM burgers LEFT JOIN burgers_toppings ON burgers_toppings.burger_id = burgers.id LEFT JOIN toppings ON burgers_toppings.topping_id = toppings.id WHERE burgers.id = %(id)s;"
        results = connectToMySQL('burgers_db').query_db( query , data )
        burger = cls( results[0] )
        for row in results:
            if not row["toppings.id"]:
                break
            topping_data = {
                "id" : row["toppings.id"],
                "name" : row["toppings.name"],
                "created_at" : row["toppings.created_at"],
                "updated_at" : row["toppings.updated_at"]
            }
            burger.toppings.append( topping.Topping( topping_data ) )
        return burger
    
    # 1.4) Get unselected Burgers from Topping
    @classmethod
    def get_unselected_burgers(cls,data):
        query = "SELECT * FROM burgers WHERE burgers.id NOT IN ( SELECT burger_id FROM burgers_toppings WHERE topping_id = %(id)s );"
        burgers = []
        results = connectToMySQL('burgers_db').query_db(query,data)
        for row in results:
            burgers.append(cls(row))
        return burgers

    # 2) CREATE OPERATIONS
    # 2.1) Create Burger
    @classmethod
    def save(cls, data):
        query = "INSERT INTO burgers (name,bun,meat,calories,restaurant_id,created_at,updated_at) VALUES (%(name)s,%(bun)s ,%(meat)s,%(calories)s,%(restaurant_id)s,NOW(),NOW());"
        # data is a dictionary that will be passed into the save method from server.py
        results = connectToMySQL("burgers_db").query_db(query, data) 
        return results
    
     # 2.2) Add Topping to Burger
    @classmethod
    def add_topping(cls,data): # add relationship in burgers_toppings table
        query = "INSERT INTO burgers_toppings (burger_id, topping_id,created_at,updated_at) VALUES (%(burger_id)s,%(topping_id)s,NOW(),NOW());"
        return connectToMySQL('burgers_db').query_db(query,data);
    
    
    # 3) UPDATE OPERATIONS
    # 3.1) Edit Burger
    @classmethod
    def update(cls, data):
        query = "UPDATE burgers SET name=%(name)s,bun=%(bun)s,meat=%(meat)s,calories=%(calories)s,restaurant_id=%(restaurant_id)s, updated_at=NOW() WHERE id = %(id)s;"
        return connectToMySQL("burgers_db").query_db(query, data)
    
    # 4) DELETE OPERATIONS
    # 4.1) Delete Burger
    @classmethod
    def destroy(cls, data):
        query = "DELETE FROM burgers WHERE id = %(id)s;"
        return connectToMySQL("burgers_db").query_db(query, data)
    
    @classmethod
    # 4.2) Remove Topping from Burger
    def remove_topping(cls,data): # remove relationship in burgers_toppings table
        query = "DELETE FROM burgers_toppings WHERE burgers_toppings.burger_id = %(burger_id)s AND burgers_toppings.topping_id=%(topping_id)s;"
        return connectToMySQL('burgers_db').query_db(query,data);

    # 5) VALIDATIOS
    # 5.1) Check valid Burger 
    @staticmethod
    def validate_burger(burger):
        is_valid = True # we assume this is true
        if len(burger['name']) < 3:
            flash("Name must be at least 3 characters.")
            is_valid = False
        if len(burger['bun']) < 3:
            flash("Bun must be at least 3 characters.")
            is_valid = False
        if int(burger['calories']) < 200:
            flash("Calories must be 200 or greater.")
            is_valid = False
        if len(burger['meat']) < 3:
            flash("Bun must be at least 3 characters.")
            is_valid = False
        if burger['restaurant_id'] == "":
            flash("Burger must have a restaurant")
            is_valid = False
        return is_valid
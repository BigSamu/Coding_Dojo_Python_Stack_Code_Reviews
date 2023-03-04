from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import burger
from flask import flash

class Topping:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.on_burgers = []

    # 1) READ OPERATIONS
    # 1.1) Get All Toppings without Burgers
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM toppings;"
        results = connectToMySQL("burgers_db").query_db(query)
        toppings = []
        for topping in results:
            toppings.append(cls(topping))
        return toppings
    
    # 1.2) Get one Topping with Burgers
    @classmethod
    def get_one_with_burgers( cls , data ):
        query = "SELECT * FROM toppings LEFT JOIN burgers_toppings ON burgers_toppings.topping_id = toppings.id LEFT JOIN burgers ON burgers_toppings.burger_id = burgers.id WHERE toppings.id = %(id)s;"
        results = connectToMySQL('burgers_db').query_db( query , data )
        topping = cls( results[0] )
        for row in results:
           
           burger_data = {
               "id" : row["burgers.id"],
               "name" : row["burgers.name"],
               "bun" : row["bun"],
               "meat": row["meat"],
               "calories" : row["calories"],
               "restaurant_id" : row["restaurant_id"],
               "created_at" : row["burgers.created_at"],
               "updated_at" : row["burgers.updated_at"]
           }
           topping.on_burgers.append( burger.Burger( burger_data ) )
        return topping
    
    # 1.3) Get unselected Toppings from Burger
    @classmethod
    def get_unselected_toppings(cls,data):
        query = "SELECT * FROM toppings WHERE toppings.id NOT IN ( SELECT topping_id FROM burgers_toppings WHERE burger_id = %(id)s );"
        results = connectToMySQL('burgers_db').query_db(query,data)
        toppings = []
        for row in results:
            toppings.append(cls(row))
        return toppings
    
    # 2) CREATE OPERATIONS
    # 2.1) Create Topping
    @classmethod
    def save( cls , data ):
        query = "INSERT INTO toppings ( name, created_at , updated_at ) VALUES (%(name)s,NOW(),NOW());"
        return connectToMySQL('burgers_db').query_db(query, data)

    # 2.2) Add Burger to Topping
    @classmethod
    def add_burger(cls,data): # add relationship in burgers_toppings table
        query = "INSERT INTO burgers_toppings (burger_id, topping_id) VALUES (%(burger_id)s,%(topping_id)s);"
        return connectToMySQL('burgers_db').query_db(query,data);

    # 3) UPDATE OPERATIONS
    # -----
    
    # 4) DELETE OPERATIONS
    # 4.1) Delete Restaurant
    @classmethod
    def destroy(cls, data):
        query = "DELETE FROM toppings WHERE id = %(id)s;"
        return connectToMySQL("burgers_db").query_db(query, data)
    
    # 4.2) Remove Burger from Topping
    @classmethod
    def remove_burger(cls,data): # remove relationship in burgers_toppings table
        query = "DELETE FROM burgers_toppings WHERE burgers_toppings.burger_id = %(burger_id)s AND burgers_toppings.topping_id=%(topping_id)s;"
        return connectToMySQL('burgers_db').query_db(query,data);

    # 5) VALIDATIOS
    # 5.1) Check valid Topping 
    @staticmethod
    def validate_topping(topping):
        is_valid = True # we assume this is true
        if len(topping['name']) < 3:
            flash("Name must be at least 3 characters.")
            is_valid = False
        return is_valid
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import burger
from flask import flash

class Restaurant:
    def __init__(self, db_data):
        self.id = db_data["id"]
        self.name = db_data["name"]
        self.created_at = db_data["created_at"]
        self.updated_at = db_data["updated_at"]
        
        self.burgers = []

    # 1) READ OPERATIONS
    # 1.1) Get All Restaurants without Burgers
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM restaurants;"
        results = connectToMySQL("burgers_db").query_db(query)
        restaurants = []
        for restaurant in results:
            restaurants.append(cls(restaurant))
        return restaurants

    # 1.2) Get One Restaurant
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM restaurants WHERE id=%(id)s;"
        results = connectToMySQL("burgers_db").query_db(query, data)
        return cls(results[0])

    # 1.3) Get One Restaurants with Burgers
    @classmethod
    def get_one_with_burgers(cls, data):
        query = "SELECT * FROM restaurants LEFT JOIN burgers ON burgers.restaurant_id = restaurants.id WHERE restaurants.id=%(id)s;"
        results = connectToMySQL("burgers_db").query_db(query, data)
        restaurant = cls(results[0])
        for row in results:
            burger_data = {
                "id": row["burgers.id"],
                "name": row["burgers.name"],
                "bun": row["bun"],
                "meat": row["meat"],
                "calories": row["calories"],
                "restaurant_id": row["restaurant_id"],
                "created_at": row["burgers.created_at"],
                "updated_at": row["burgers.updated_at"],
            }
            restaurant.burgers.append(burger.Burger(burger_data))
        return restaurant

    # 2) CREATE OPERATIONS
    # 2.1) Create Restaurant
    @classmethod
    def save(cls, data):
        query = "INSERT INTO restaurants (name, created_at, updated_at) VALUES (%(name)s,NOW(),NOW());"
        results = connectToMySQL("burgers_db").query_db(query, data)
        return results

    # 3) UPDATE OPERATIONS
    # -----

    # 4) DELETE OPERATIONS
    # 4.1) Delete Restaurant
    @classmethod
    def destroy(cls, data):
        query = "DELETE FROM restaurants WHERE id = %(id)s;"
        return connectToMySQL("burgers_db").query_db(query, data)
    
    # 5) VALIDATIOS
    # 5.1) Check valid Restaurant 
    @staticmethod
    def validate_restaurant(restaurant):
        is_valid = True # we assume this is true
        if len(restaurant['name']) < 3:
            flash("Name must be at least 3 characters.")
            is_valid = False
        return is_valid
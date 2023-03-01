# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL

# model the class after the friend table from our database
class Burger:
    def __init__(self,data):
        self.id = data["id"]
        self.name = data["name"]
        self.bun = data["bun"]
        self.meat = data["meat"]
        self.calories = data["calories"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    # 1) READ OPERATIONS
    # Get All Burgers
    @classmethod
    def get_all(cls):
        query =  "SELECT * FROM burgers;"
        results = connectToMySQL("burgers_db").query_db(query)

        burgers = []
        for burger in results:
            burgers.append(cls(burger))
        return burgers

    # Get One Burger
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM burgers WHERE id=%(id)s;"
        results = connectToMySQL("burgers_db").query_db(query, data)
        return cls(results[0])
    
    # 2) CREATE OPERATIONS
    # Create Burger
    @classmethod
    def save(cls, data):
        query = "INSERT INTO burgers (name,bun,meat,calories,created_at,updated_at) VALUES (%(name)s,%(bun)s ,%(meat)s,%(calories)s,NOW(),NOW());"
        # data is a dictionary that will be passed into the save method from server.py
        results = connectToMySQL("burgers_db").query_db(query, data) 
        return results
    
    # 3) UPDATE OPERATIONS
    # Edit Burger
    @classmethod
    def update(cls, data):
        query = "UPDATE burgers SET name=%(name)s,bun=%(bun)s,meat=%(meat)s,calories=%(calories)s,updated_at=NOW() WHERE id = %(id)s;"
        return connectToMySQL("burgers_db").query_db(query, data)
    
    # 4) DELETE OPERATIONS
    @classmethod
    def destroy(cls, data):
        query = "DELETE FROM burgers WHERE id = %(id)s;"
        return connectToMySQL("burgers_db").query_db(query, data)
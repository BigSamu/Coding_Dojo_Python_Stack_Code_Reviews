from flask_app.config.mysqlconnection import connectToMySQL
from datetime import datetime
import math

class Message:
    db_name = 'private_wall'
    def __init__(self,db_data):
        self.id = db_data['id']
        self.content = db_data['content']
        self.sender_id = db_data['sender_id']
        self.receiver_id = db_data['receiver_id']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']

        self.sender = db_data['sender']
        self.reciever = db_data['receiver']


    # 1) READ OPERATIONS
    # 1.1) Get All User Messages
    @classmethod
    def get_user_messages(cls,data):
        query = "SELECT users.first_name as sender, users2.first_name as receiver, messages.* FROM users LEFT JOIN messages ON users.id = messages.sender_id LEFT JOIN users as users2 ON users2.id = messages.receiver_id WHERE users2.id =  %(id)s"
        results = connectToMySQL(cls.db_name).query_db(query,data)
        messages = []
        for message in results:
            messages.append( cls(message) )
        return messages
    
    # 2) CREATE OPERATIONS
    # 2.1) Create Message
    @classmethod
    def save(cls,data):
        query = "INSERT INTO messages (content,sender_id,receiver_id) VALUES (%(content)s,%(sender_id)s,%(receiver_id)s);"
        results = connectToMySQL(cls.db_name).query_db(query,data)
        return results
    
    # 3) UPDATE OPERATIONS
    # -----
    
    # 4) DELETE OPERATIONS
    # 4.1) Delete Message
    @classmethod
    def destroy(cls,data):
        query = "DELETE FROM messages WHERE messages.id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query,data)
     
    # 5) Validators
    # ----
     
    # 6) AUX METHOD
    def time_span(self):
        now = datetime.now()
        delta = now - self.created_at
        print(delta.days)
        print(delta.total_seconds())
        if delta.days > 0:
            return f"{delta.days} days ago"
        elif (math.floor(delta.total_seconds() / 60)) >= 60:
            return f"{math.floor(math.floor(delta.total_seconds() / 60)/60)} hours ago"
        elif delta.total_seconds() >= 60:
            return f"{math.floor(delta.total_seconds() / 60)} minutes ago"
        else:
            return f"{math.floor(delta.total_seconds())} seconds ago"
# -------------------------------------
# Python OOP Example - Vehicle Object
# -------------------------------------

# ***********************
# A) Class Definition
# ***********************

class Motorbike:

    # I.1) Class Attributes
    vehicle_type = "motorbike"
    wheel = 2

    # II) Class Constructor
    def __init__(self, bike_name, top_speed):
        # I.2) Instance Attributes
        self.bike_name= bike_name
        self.top_speed= top_speed
        self.speed = 0

    # III) Methods
    # III.1) Instance Methods
    def type_description(self):
        print(f"This bike is a {self.bike_name} motorcycle, has {self.wheel} wheels and its top speed is {self.top_speed} km/hr")

    def accelerate(self,speed):
        self.speed += speed
        print(f"Now riding {self.bike_name} at {self.speed} km/hr")
        return self

    def deaccelerate(self,speed):
        if Motorbike.can_deaccelerate(self.speed, speed):
            self.speed -= speed
            print(f"Now riding {self.bike_name} at {self.speed} km/hr")
        return self
         
    @staticmethod
    def can_deaccelerate(actual_speed, new_speed):
        if(actual_speed>=new_speed):
            return True
        else:
            print(f"Cannot deaacelerate that amount of speed")
            return False

# ***********************
# B) Driver Code
# ***********************

bike_1 = Motorbike('Honda', 130)
bike_2 = Motorbike('BMW',150 )

bike_1.type_description()
bike_1\
    .accelerate(20)\
    .accelerate(50)\
    .deaccelerate(60)\
    .deaccelerate(20)\
    .deaccelerate(10)
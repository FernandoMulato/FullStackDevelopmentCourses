# OOP
# Class
# Declare classes in python
class Mug():
    # Attributes
    att_color = "White"
    att_menssage = None
    att_material = "Porcelain"
    att_clean = True

# Intance of a class
obj_mug_1 = Mug()
obj_mug_2 = Mug()

# Reassign values to object attributes
obj_mug_2.att_color = "White and Blue"

print(obj_mug_1.att_color)
print(obj_mug_2.att_color)

class Vehicle():
    # Attributes
    # Class attributes
    att_country_origin = "Germany"
    
    # Methods or Operations
    # Constructor
    def __init__(self, prm_color, prm_length_metres, prm_wheels):
        # Intance attributes
        self.att_color = prm_color
        self.att_length_metres = prm_length_metres
        self.att_wheels = prm_wheels
    
    # Actions
    def op_started(self):
        print("The vehicle has started.")
    
    def op_stop(self):
        print("The vehicle has stopped")
    
    # Views 
    def op_display_information(self):
        print(f"Vehicle color {self.att_color}. With a length of {self.att_length_metres} meters long. It has {self.att_wheels} wheels.\nThe country of origin is {self.att_country_origin}")

obj_vehicle_1 = Vehicle("Red", 4, 4)

# Called to methods
obj_vehicle_1.op_started()
obj_vehicle_1.op_stop()

# Add an object to the obverse
obj_vehicle_2 = Vehicle("Black", 8.25, 8)
obj_vehicle_2.att_material_spoiler = "Carbon fiber"
print(obj_vehicle_2.att_material_spoiler)

print(obj_vehicle_1.att_country_origin)
print(obj_vehicle_1.op_display_information())

# Empty class
class Example():
    pass # serves to avoid errors by being empty classes, conditionals, loops or functions
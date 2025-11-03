# Parameters with default and mandatory values
class cls_user:
    def __init__(self, prm_phone_number, prm_name="user", prm_last_names="nn", prm_age="0"):
        self.att_name = prm_name
        self.att_last_names = prm_last_names
        self.att_age = prm_age
        self.att_phone_number = prm_phone_number

    def op_describe(self):
        print(f"Name: {self.att_name}.")
        print(f"Last names: {self.att_last_names}.")
        print(f"Age: {self.att_age}.")
        print(f"Phone number: {self.att_phone_number}.")

obj_user1 = cls_user("315405497", "Paula", "Cabello Prados", "30")
obj_user1.op_describe()

obj_user2 = cls_user("315405497")
obj_user2.op_describe()

obj_user3 = cls_user("315405497", "Miriam")
obj_user3.op_describe()

obj_user4 = cls_user(prm_age="27", prm_last_names="Moran Serra", prm_phone_number="315405497",)
obj_user4.op_describe()

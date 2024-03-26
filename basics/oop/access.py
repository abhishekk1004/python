class Person:

    def __init__(self, name,age,password): 
        self.name=name
        self.age= age
        # self.gender= gender
        self.passwprd= password
    
    def set_password(self,password):
        self.__password= password

    def get_password(self):
        return self.__password

    password=property(get_password,set_password)

ram=Person("ram",19,'password')
ram.password="newpassword"
print(ram.password)
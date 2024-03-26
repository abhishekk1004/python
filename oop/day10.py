""" opp """

""" ______________________MAGIC METHOD______ """
# class House:
#     window=10
#     color="Blue"
#     door=3

#     def __init__(self,window,color,door) -> None:
#         self.window=window
#         self.color=color
#         self.door=door

#     def get_color(self):
#         return self.color
    
#     def set_color(self,color):
#         self.color= color

# ram_ko_ghar=House(
#     window=5,
#     color='Red',
#     door=2
# )

# print(ram_ko_ghar.window)
# ram_ko_ghar.set_color("red")
# print(ram_ko_ghar.get_color())

# class Pizza:
#     def dough(self):
#         print("dough")
#         return self

#     def sauce(self):
#         print("sauce")
#         return self

#     def cheese(self):
#         print("cheese")
#         return self

#     def sausage(self):
#         print("saussage")
#         return self

# pizza=Pizza()
# pizza.dough().sauce().cheese().sausage

# class Burger:
#     def salad(self):
#         print('salad')
#         return self
    
#     def  patty(self):
#         print('Patty')
#         return self
    
#     def cheese(self):
#         print('Cheese')
#         return self
    
#     def onion(self):
#         print('onion')
#         return self
    
#     def lettuce(self):
#         print( 'Lettuce')
#         return self
    
# burger=Burger()
# burger.salad().patty().cheese().onion().lettuce()

class Employee:
    def __init__(self,name, salary, ) -> None:
        self.name = name
        self.salary = salary
        
    def __eq__(self,object) -> bool:
        return self.salary==object.salary
    
    
ram=Employee('ram',900)
shyam=Employee('Shyam',850)
print(ram==shyam)                   
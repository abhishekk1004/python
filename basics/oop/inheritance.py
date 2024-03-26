""" ___________INHERITANCE___________ """
class Grandfather:
    house="Luxery house"

# single inheritance
class Mother:
    jewellary="Diamod Braclet"


# multiple  inheritance
class Father(Grandfather, Mother):
    car="Mustang"




# hybrid inheritance
class Son(Father, Grandfather, Mother):
    gaming_console="PS5"


son=Son()
print(son.gaming_console)
print(son.car)
print(son.house)
print(son.jewellary)

""" iterable """ 
# for loop le iterable linxa
# range,list, tuple, string

""" member shit operator """
# number=[1,2,3,4,5,6,7,8,9,10]
# print(1 in number)

# for i in range(10):
#     print(i)

# print(list(range(2,10,2)))

fruits=[
    'kera',
    'banana',
    'apple',
    'kiwi',
    'orange'
]
# enumerate le tuple ma change gardinca index rw valaue provide garxa...or index banauna lai
# for index,fruits in enumerate(fruits):  
    # print(index,fruits)
    # print(index+1,fruits)
    # ekchoti matra run garna lai hami break use garchau
    # if fruits=='kiwi':
    #     break
""" class work """
# name="Abhishek singh"
# for char in name:
#     print(char)

""" To create a function """ 
# function jai always call garnu parxa
# def greeting(name):
#     print(f"Hello,{name} Ram how are you!!")
#     print(f"Kaise he,{name} dalleeee")

# greeting("Ram")   
# greeting("Shyam")   
# function lai call garna () yo bracket dinu parxa
# def greeting(f_name,m_name, age):
#     print(f"Hello,{f_name} {m_name} {age} Ram how are you!!")
#     print(f"Kaise he, {f_name} {m_name} {age} dalleeee")
"""  positional argument """
# greeting("Ram", "Singh", "35")
""" keyword argument """
# greeting(m_name="Amit", f_name="Shaha",age="5")

# def sum(*numbers):
#     total=0
#     for number in numbers:
#         total+=number
#     print(total)

# sum(1,5,5,6,23,7,9,4,52,6)

def person(**attr):
    for key, value in attr.items():
        print(f"{key} : {value}")

person(name="Amit", age='35')
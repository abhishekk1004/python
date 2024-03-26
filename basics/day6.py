""" Recursion """
def number(n):
    print(n)
    if n==10:
        return
    number(n+1)

number(1)

# recreate this funtion... homework
    #  range(1,10)
# def sum(a,b):
#     return(a+b)

# print(sum(1,2))

""" Lambda function """
# it's a anonymous funciton jsko naam nai hudaina like kehi identity hudaina
# sum=lambda a,b:a+b

# print(sum(1,2))
   

# def func(n):
#     return lambda x:x*n

# doubler=func(2)
# tripler=func(3)
# fourth=func(4)
# print(doubler(10))
# print(tripler(10))
# print(fourth(5))

""" Scope """
# visibility kaha smma hunxa laike kunai file ko kaha smma access garna pauxau 
# a=20
# def hello():
#     a=10
#     print(a)

# print(a)
# hello()

# x=9
# def outer():
#     # x=10
#     def inner():
#         # x=12
#         print("inner sees x as",x)
#     inner()
#     print("outer sees x as",x)
# outer()
# print("global is sees x as",x)
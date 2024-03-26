# age=int(input("enter your age"))
# print(age)

# if age>= 18:
#     print("you are eligible for voting")

# elif age<70:
#     print(f"come with one person please because your age is greater than {age}")
# else:
#     print(f"You are not aligible {age}")

    # task
    # a and b variable banaunu and tysma user snga input magne
    #  user sng operator +,-,*,/ use kora hbe
    # and tysko result print

""" LOOOOOOPSSSSSSSSSSSS"""
# i=0
# while i<=5 :
#     i+=1
#     print(f"{i} Abhishek")


"""                  Task To make a calculator                      """
    

print("Select the operation you want to perform ")
print("press 1 for addition ")
print("press 2 for subtraction ")
print("press 3 for multiplication ")
print("press  4 for division ")

number=int(input("Enter Your operator "))
if number in (1,2,3,4):
    num1=float(input("Enter First Number "))
    num2=float(input("Enter Second Number "))


    if number== 1:
       print(f"The addition is({num1}+{num2})", num1 + num2 )
    elif number==2:
        print(f"The substraction is({num1}-{num2})", num1 - num2 )
    elif number==3:
        print(f"The multiplication is({num1}*{num2})", num1 * num2 )
    elif number==4:
        print(f"The division is({num1}/{num2})", num1 / num2 )
        if num2==0:
            print("Error! Division by zero is not allowed")
        else:
            print= num1/num2
    print("result:")
else:
    print("Invalid input")
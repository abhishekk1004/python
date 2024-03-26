# while True:
#     try:
#         a=int(input("Enter the first number : "))
#         b=int(input("Enter the second number : "))
        
#         if a==5:
#             raise Exception("Input cannnot be 5")
#         print(a/b)
#     except  ZeroDivisionError:
#         print("A number cannnot divide zero")

#     except ValueError:
#         print("is not an integer. Please enter an integer.")

#     except Exception as e:
#         print(f"something went wromg")

""" classwork """
movies=[
    'Bahubali',
    'KGF',
    'SAlar',
    'Money Heist',
    'Narcos',
]
total_index=len(movies)-1
# print(movies)
while True:
        try:
            index = int(input(f"enter a number between o to {total_index}"))
            print(movies[index])

        except  IndexError:
              print(f"Invalid input number must be lesser or equal to {total_index}")

        except ValueError:
              print(f" invalid Value please enter a valid value")
        

                            
        
#             index = int(input('Enter movie name to search :'))
#             if index <0 or index>=len(movies):
#                 raise IndexError("Invalid input, please enter a valid number ")
#         except IndexError:
#             print("Please Enter a Valid Number")
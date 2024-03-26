# try:
#     f=open("hello.txt")

#     print(f.readlines())
#     f.close()
# except Exception as e:
#     print(e)


""" append mode """
# try:
#     f=open("hello.txt","w")

#     f.write("\n Hello this is Profession")
#     f.close()
# except Exception as e:
#     print(e)

""" to remove file """
# suruma import os rakhne ani tala os.remove("fle ko naam")
# ekxin paxi delete garna lai
# from time import sleep ani remove vanda mathi sleep(yaha time rakhne)

# task
# user sng input magerw tyo file banaunu paryo
# file vitra content user sng input magerw
# read garnuparyo
# input mew add garnu
# last file delete garne pani user input
""" TASK """
import os
from time  import sleep

while  True :
    try:
        user_input = input("Enter the name of a file: ")
        f=open(user_input,"r+") #r+ means that we can both read and write in the file
        
    except FileNotFoundError:
        print ("File not found.")
        # contents = f.read() # it  will give all the content of the file
        # print(contents)
        user_input = input("Please enter again\n Enter the name of a file: ")
        while True:
            f=open(user_input, "r" ) 
            print(f.read())
            f.write(input('provide  some text:\n'))
            f=open(user_input,"a")
            f.write(input("What you want to add: "))

            f=open(user_input,'w')
            f.write('Opps ! I have deleted everything.\n')
            print ('Do You Want To Continue? (yes/no): ')
        
            if input()=='no':
                break

            input("Do you want to remove file: y/n")
            if 'y'==input():
             sleep(5)
             os.remove(user_input)
            else:
                print("File remains there")
# else:
#     while True:
#         ch=input('Do you want to continue? Y/N')
#         if ch=="Y":
#             print(contents)
#         elif ch=="N":
#             break

            f.close()
    except Exception as e:
        print(e)




""" homework  APP BANAUNE"""
# make a tudolist
# title rw descriptoin magnu paryo
# tudolist ko list banu
# global data base hunuparyo>>>>>> store 


# app banaune
# user sng data magne... append
# insert.. data.. show hunu parne 
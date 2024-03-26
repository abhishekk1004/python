#  first to take input from user
# user sng input magerw tyo file banaunu paryo
# file vitra content user sng input magerw
# read garnuparyo
# input mew add garnu
# last file delete garne pani user input

# import os
# f= open(input("Enter File Name you Want to Make: "), "x")
# print("Now Enter the Content You want in Your File : ")
# content = input ("\n")
# f.write(content)
# f.close()
# print("\n Do you Want To Add More Lines ? \n Press Y  For Yes And N For No : ")
# if (input (""))==('Y'):
#     f=open(input("Enter The File Name Where You Want To Add More Lines : "),"a")
#     print("\n Now Enter The New Line You Want To Add In That File : ")
#     new_line = input ("\n")
#     f.write('\n'+new_line)
#     print("\n Data Added Successfully !!!")
# f.close()

import os
from time import sleep

def create_file(filename):
    try:
        f=open(filename,"x")
        # with open(filename,'x') as file:
        print(f"File created successfully.")
    except FileNotFoundError :
        print("Error ! Could not find or access the specified file.")
        f.close()

def write_to_file(filename, content):
    try:
        f= open(filename,"a")
        f.write(f"\n{content}")
        print(" Data Added Successfully")
    except FileNotFoundError:
        print("Error!!! File Not Found. ")
    except Exception as e:
        print(e)
        f.close()

def read_file(filename):
    try:
        f=open(filename,"r")
        print("File Content")
        print(f.read())
    except FileNotFoundError:
        print("Error!!! File Not Found... ")
       
def delete_file(filename):
    try:
        sleep(5)
        os.remove(filename)
        print("File Deleted Successfully...😎")

    except FileNotFoundError:
        print("Error....!!!!!!!!!!!!🤦‍♂️")
    except  PermissionError:
        print('Acesssss Denied..!!🐱‍👤')

def remove_word(filename, word):
    try:
        f=open(filename, 'r')
        lines=f.readlines()
        f=open(filename, 'w')
        for  line in lines:
            f.write(line.replace(word,''))
        print ("Word Removed Successfully!")
    except FileNotFoundError:
        print("Error!!! File not found...😒")

def main():
    filename = input("Enter Filename: ")

    while True:
        print("\n1.create file\n 2. Write what the content \n3. Read file \n4. Delete file \n5. only Remove WORD FROM FILE \n6. EXIT")
        choice= input("Enter your CHOICE😃👍")

        if choice=='1':
            create_file(filename)
        elif choice== '2':
            content  = input("Enter the text you want to add: ")
            write_to_file(filename,content)
        elif choice == '3':
            read_file(filename)
        elif choice == '4':
            delete_file(filename)
        elif choice == '5':
            word = input( "Enter Word To Remove : ")
            remove_word(filename, word)
        elif choice == '6':
            break
        else:
            print("Invalid Choice..🙄...Please Enter Again.🤐")

if  __name__=="__main__":
    main()
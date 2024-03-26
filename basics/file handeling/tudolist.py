# to make a tudolist app
# class TodoList:
#     def __init__(self):
#         self.tasks = []

#     def add_task(self, task):
#         self.tasks.append(task)
#         print("Task added successfully.")

#     def display_tasks(self):
#         if self.tasks:
#             print("Your to-do list:")
#             for i, task in enumerate(self.tasks, start=1):
#                 print(f"{i}. {task}")
#         else:
#             print("Your to-do list is empty.")

# def main():
#     todo_list = TodoList()

#     while True:
#         print("\n1. Add task\n2. Remove task\n3. Display tasks\n4. Exit")
#         choice = input("Enter your choice: ")

#         if choice == '1':

# if __name__ == "__main__":
#     main()
class TudoList:
    def __init__(self):
        self.task = []

    def  add_task(self,task):
        task.append(task)
        print(f"Task '{task}' added SUCCESSFULLY...😚😚")

    def remove_task(self,task):
     
        if task in self.tasks:
            self.tasks.remove(task)
            print("Task Removed Successfully..!!!🥱🥱")
        else:
            print('Task Not Found In list...🙄🙄🙄')
 
    def  display_tasks(self):
        if self.tasks:
            print("Your to-do list:")
            for i, task in enumerate(self.tasks, start=1):
                print(f"{i}. {task}")
        else:
            print("Your to-do list is empty.")

# if __name__ == "__main__":
# create a loop to run a app
def main():
    tudo_list = TudoList()
    # print("Wlc to TO DO list : ")

    while True:
        print("Please Select One of The Following: ")
        print('\n1. Add Task \n2. Remove Task \n3. Display Task \n4. EXIT..ING ')
        
        choice = input('ENter your Choice: ')

        if (choice == '1'):
            task = input('Enter the Task:')
            tudo_list.add_task(task)

        elif (choice == '2'):
            task = input("Enter the task to remove:")
            tudo_list.remove_task(task)
    
        elif (choice == '3'):
            tudo_list.display_tasks()
           
        elif (choice == '4'):
            print('Exiting....🥱')
            break
        else:
            print("\n Invalid Input.....  Please  Try Again \n")
if __name__ == "__main__":
    main()


""" ------------------LETS DIVE IN AGAIN 3RD ATTEMPT--------------------- """

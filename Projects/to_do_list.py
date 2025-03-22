def task():
    tasks=[]
    print("Welcome to TO-Do list...You can use this as todo list\nThis is made by SAMIR ALI")
    task_number=int(input(f"Enter how many task you want: "))
    for i in range(1,task_number+1): #starts from 1 and end at the number user addded
        task_name=input(f"Enter task name {i}= ")
        tasks.append(task_name) #adds the task into list
    print(f"Your task is:{tasks}") #dispalyas the task
    while True:
        try:
            op=int(input("Enter 1 for add\nEnter 2 for delete\nEnter 3 for update\nEnter 4 for View\nEnter 5 for exit\nEnter what do you wanto to do:"))#user's input
            if op==1 : #for adding new value
                add_value=input("Enter new task you want to add: ")
                tasks.append(add_value)
                print(f"Your new task {add_value} has been aded succesfully.")
            elif op==2:
                del_value=input("Enter the task name you want to delete: ")#for deleting a value that exist in the list
                if del_value in tasks:   #checks if the value exist or not
                    ind=tasks.index(del_value) #find the value in index
                    del  tasks[ind]  #deletes that task
                    print(f"Your task {del_value} has been deleted")  
                else:
                    print(f"No task exist in {del_value} name ")
            elif op==3:
                up_value=input("Enter the task name you want to update: ") #updating an existing task from the list
                if up_value in tasks: #checks if value is there
                    up=input("Enter what do you want to update: ") #new vlaue you want to add
                    ind=tasks.index(up_value) #finds the value
                    tasks[ind]=up #replace with new one
                    print(f"Your {up_value} is changed to {up}")       
                else:
                    print("No task found")
            elif op==4:
                print(f"Your tasks is {tasks}")
            elif op==5:
                print("Exiting TO-Do app.......\nThanks For Using 😊 💕") #the user want to stop the program
                break
            else:
                print("Invalid number....Please try again")   #user added wrong value..It must be within 1-5
        except ValueError:
            print("Invalid value...Please try again")         
task()




#












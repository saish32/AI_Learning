
import os
file_name="task.txt"

def load_task():
    tasks={}
    if os.path.exists(file_name):
        with open(file_name,"r")as file:
            for line in file:
                task_id,title,status=line.strip().split(" | ")
                tasks[int(task_id)]={"title":title,"status":status}
    return tasks

def save_task(tasks):
    with open(file_name,"w")as file:
        for task_id,task in tasks.items():
            file.write(f"{task_id} | {task['title']} | {task['status']}\n")

def add_task(tasks,title):
    task_id=max(tasks.keys(),default=0)+1
    tasks[task_id]={"title":title,"status":"incomplete"}
    print(f"Task '{title}' added with ID {task_id}.")
    deadline=input("Enter the deadline for the task (YYYY-MM-DD): ")
    tasks[task_id]["deadline"]=deadline
    priority=input("Enter the priority for the task (low, medium, high): ")
    tasks[task_id]["priority"]=priority

def view_tasks(tasks):
    if not tasks:
        print("no tasks found.")
    else:
        print("tasks:")
        for task_id,task in  tasks.items():
            print(f"{task_id}:{task['title']}-{task['status']} Deadline: {task.get('deadline','N/A')} Priority: {task.get('priority','N/A')}")

def mark_task_complete(tasks,task_id):
    if task_id in tasks:
        tasks[task_id]["status"]="complete"
        print(f"Task {task_id} marked as complete.")
    else:
        print(f"Task {task_id} not found.")

def delete_task(tasks,task_id):
    if task_id in tasks:
        del tasks[task_id]
        print(f"Task {task_id} deleted.")
    else:
        print(f"Task {task_id} not found.")

#Main 
def main():
    tasks=load_task()
    while True:
        print("\nTask Manager")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task Complete")
        print("4. Delete Task")
        print("5. Exit")

        choice=input("Enter your choice: ")
        if choice=="1":
            title=input("Enter the task title: ")
            add_task(tasks,title)
            save_task(tasks)
        elif choice=="2":
            view_tasks(tasks)
        elif choice=="3":
            task_id=int(input("Enter the task ID to mark as complete: "))
            mark_task_complete(tasks,task_id)
            save_task(tasks)
        elif choice=="4":
            task_id=int(input("Enter the task ID to delete: "))
            delete_task(tasks,task_id)
            save_task(tasks)
        elif choice=="5":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__=="__main__":
    main()
        

# from functools import reduce
# import os

# print(os.getcwd())



# numbers=[1,2,3,4]
# product=reduce(lambda x,y:x*y,numbers) #reduce function
# print(product)
# even=filter(lambda x:x%2==0,numbers) #filter function
# print(list(even))
# squares=map(lambda x:x**2,numbers) #map function
# print(list(squares))



# evens=[x for x in range(100) if x%2==0] #lines comphrensive
# print(evens)
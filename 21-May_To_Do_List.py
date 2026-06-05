import tkinter as tk

from tkinter import simpledialog, messagebox
root = tk.Tk()
root.title("TO DO LIST of Khushi Agrawal")
root.iconphoto(False,tk.PhotoImage(file=r"C:\Users\agraw\PycharmProjects\PythonProject3\17866343.png"))
root.geometry("400x500")
root.resizable(False,False)

def do(x):
    if x == "1":
        enter_task = simpledialog.askstring("Input", "Enter your task:")

        if enter_task:
            with open("To_Do_List.txt", "a") as f:
                f.write(enter_task + "\n")
    elif x == "2":
        try:
            with open("To_Do_List.txt", "r") as f:
                data = f.read()

            if data.strip() == "":
                messagebox.showinfo("Your Tasks", "No tasks found!")
            else:
                messagebox.showinfo("Your Tasks", data)

        except:
            messagebox.showinfo("Error", "Empty file!!")

    elif x == "3":
        try:
            with open("To_Do_List.txt", "r") as f:
                tasks = f.readlines()

            delete_task = simpledialog.askstring("Delete", "Enter task to delete:")

            if delete_task + "\n" in tasks:
                tasks.remove(delete_task + "\n")

                with open("To_Do_List.txt", "w") as f:
                    f.writelines(tasks)

                messagebox.showinfo("Success", "Task deleted successfully!")
            else:
                messagebox.showinfo("Error", "Task not found!")

        except:
            messagebox.showinfo("Error", "No task to delete!")
    elif x == "4":
        root.destroy()
    else:
        messagebox.showinfo("Error", "Invalid input!")

l1 =tk.Label(root, width= 50,text =  "this is your to do list.",font=("Arial", 10, "bold"), bg="black", fg="white")
l1.grid(row=0,column=0,columnspan=8,padx=3,pady=3, sticky="NSEW")
l1.configure(background="grey", justify="center")
l2=tk.Label(root, width= 50,text =" please enter your choice from below choices!!!" ,font=("Arial", 10, "bold"), bg="black", fg="white")
l2.grid(row=1,column=0,columnspan=8,padx=3,pady=3, sticky="NSEW")
l2.configure(background="grey", justify="center")
l3 =tk.Label(root, width= 50,text = " 1. Enter your task!!",font=("Arial", 10, "bold"), bg="black", fg="white")
l3.grid(row=2,column=0,columnspan=8,padx=3,pady=3, sticky="NSEW")
l3.configure(background="grey", justify="center")
l4 =tk.Label(root, width= 50,text = "2. Show the task!!",font=("Arial", 10, "bold"), bg="black", fg="white")
l4.grid(row=3,column=0,columnspan=8,padx=3,pady=3, sticky="NSEW")
l4.configure(background="grey", justify="center")
l5 =tk.Label(root, width= 50,text = "3. Delete the task!!",font=("Arial", 10, "bold"), bg="black", fg="white")
l5.grid(row=4,column=0,columnspan=8,padx=3,pady=3, sticky="NSEW")
l5.configure(background="grey", justify="center")
l6 =tk.Label(root, width= 50,text = "4. Exit",font=("Arial", 10, "bold"), bg="black", fg="white")
l6.grid(row=5,column=0,columnspan=8,padx=3,pady=3, sticky="NSEW")
l6.configure(background="grey", justify="center")
list_of_buttons = [("1",6,2),("2",6,4),("3",7,2),("4",7,4)]
for (item, row, column) in list_of_buttons:
    button = tk.Button(root,text=item,bg="white",fg="black",font=("Arial", 20, "bold"),width=5,height=1,relief="raised",bd=2,cursor="hand2", command= lambda x=item: do(x))
    button.grid(row=row,column=column,sticky="nsew",padx=1,pady=0)
for i in range(8):
    root.grid_columnconfigure(i, weight=1)
for i in range(19):
    root.grid_rowconfigure(i, weight=1)
root.mainloop()
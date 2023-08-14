
from tkinter import *
from tkinter import messagebox
 

tasks_list = []
counter = 1
 

def inputError() :
     
    if enterTaskField.get() == "" :
        messagebox.showerror("Input Error")
        return 0
    return 1
 

def clear_taskNumberField() :
    taskNumberField.delete(0.0, END)
 
def clear_taskField() :
    enterTaskField.delete(0, END)
     
def insertTask():
    global counter
    value = inputError()
    if value == 0 :
        return
    content = enterTaskField.get() + "\n"

    tasks_list.append(content)
    TextArea.insert('end -1 chars', "[ " + str(counter) + " ] " + content)

    counter += 1
 
    clear_taskField()


def edit():
      enterTaskField1.insert(root.END, TextArea.get('1.0',END))
 
def delete():
     
    global counter
    if len(tasks_list) == 0 :
        messagebox.showerror("No task")
        return
 
    number = taskNumberField.get(1.0, END)
 
    
    if number == "\n" :
        messagebox.showerror("input error")
        return
     
    else :
        task_no = int(number)

    clear_taskNumberField()
     
    tasks_list.pop(task_no - 1)
 
    counter -= 1
     

    TextArea.delete(1.0, END)
 



    for i in range(len(tasks_list)) :
        TextArea.insert('end -1 chars', "[ " + str(i + 1) + " ] " + tasks_list[i])
     
 

if __name__ == "__main__" :
 

    root = Tk()
 

    root.configure(background = "lightblue")
 
    
    root.title("ToDo list")
 
    
    root.geometry("350x400")

    enterTask = Label(root, text = "Add items :",font=15)
    enterTask.grid(row = 0, column = 2)

    
    enterTaskField = Entry(root)
    enterTaskField.grid(row = 1, column = 2, ipadx = 60)
 
    Submit = Button(root, text = "Submit", fg = "white", bg = "black", command = insertTask)
    Submit.grid(row = 1, column = 3,pady=5)
         
    
    TextArea = Text(root, height = 5, width = 25, font = "lucida 13")
    TextArea.grid(row = 3, column = 2, padx = 10, sticky = W)
    
    taskNumber = Label(root, text = "Delete Task Number:")
    taskNumber.grid(row = 4, column = 2, pady = 5,padx=5)
    
    taskNumberField = Text(root, height = 1, width = 25)
    taskNumberField.grid(row = 5, column = 2)
    
    delete = Button(root, text = "Delete", fg = "white", bg = "black", command = delete)
    delete.grid(row = 5, column = 3, pady = 5)
    
    taskNumber1 = Label(root, text = "edit Task Number:")
    taskNumber1.grid(row = 6, column = 2, pady = 5,padx=5)

    taskNumberField1 = Text(root, height = 1, width = 25)
    taskNumberField1.grid(row = 7, column = 2)
    
    Edit = Button(root, text = "Edit", fg = "white", bg = "black",width=5,command = edit)
    Edit.grid(row = 7, column = 3)
    root.mainloop()

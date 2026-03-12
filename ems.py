from customtkinter import *
from PIL import Image
from tkinter import ttk
from tkinter import messagebox
import database
#Functions
def delete_all():
    result=messagebox.askyesno('Confirm','Do you want to delete all data?')
    if result:
        database.deleteall_records()
    else:
        pass

def show_all():
    treeview_data()
    searchEntry.delete(0,END)
    searchBox.set('Search By')

def search_employee():
    if searchEntry.get()=='':
        messagebox.showerror("Error","Enter value to search")
    elif searchBox.get()=='Search By':
        messagebox.showerror("Error","Please select an option")
    else:
        searched_data=database.search(searchBox.get(),searchEntry.get())
        tree.delete(*tree.get_children())
        for employee in searched_data:
            tree.insert('',END,values=employee)

def delete_employee():
    selected_item=tree.selection()
    if not selected_item:
        messagebox.showerror("Error", "Select an item to delete")
    else:
        database.delete(idEntry.get())
        treeview_data()
        clear()
        messagebox.showinfo('Success','Data deleted successfully')

def upadate_employee():
    selcted_item=tree.selection()
    if not selcted_item:
        messagebox.showerror("Error","Select data to update")
    else:
        database.update(idEntry.get(),nameEntry.get(),phoneEntry.get(),roleBox.get(),genderBox.get(),salaryEntry.get())
        treeview_data()
        clear()
        messagebox.showinfo("Success","Data updated successfully")

def selection(event):
    selected_item=tree.selection()
    if selected_item:
        row=tree.item(selected_item)['values']
        clear()
        idEntry.insert(0,row[0])
        nameEntry.insert(0,row[1])
        phoneEntry.insert(0,row[2])
        roleBox.set(row[3])
        genderBox.set(row[4])
        salaryEntry.insert(0,row[5])

def treeview_data():
    employees=database.fetch_employees()
    tree.delete(*tree.get_children())
    for employee in employees:
        tree.insert('',END,values=employee)

def clear(value=False):
    if value:
        tree.selection_remove(tree.focus())
    idEntry.delete(0,END)
    nameEntry.delete(0,END)
    phoneEntry.delete(0,END)
    roleBox.set('Manager')
    genderBox.set('Male')
    salaryEntry.delete(0,END)

def add_employee():
    if idEntry.get()=='' or phoneEntry.get()=='' or nameEntry.get()=='' or salaryEntry.get()=='':
        messagebox.showerror("Error", "Please fill all fields")
    elif database.id_exists(idEntry.get()):
        messagebox.showerror("Error", "Employee ID already exists")
    else:
        database.insert(idEntry.get(),nameEntry.get(),phoneEntry.get(),roleBox.get(),genderBox.get(),salaryEntry.get())
        treeview_data()
        clear()
        messagebox.showinfo("Success", "Data added successfully")

window=CTk()
window.title("Employee Management System")
window.geometry('930x580+100+100')
window.resizable(0, 0)
window.configure(fg_color='#161C30')

logo=CTkImage(Image.open('Emsimg2.jpg'),size=(930,158))
logolabel=CTkLabel(window,image=logo,text='')
logolabel.grid(row=0,column=0,columnspan=2)

leftFrame=CTkFrame(window,fg_color='#161C30')
leftFrame.grid(row=1,column=0)

idlabel=CTkLabel(leftFrame,text='ID',font=('Arial',18,'bold'),text_color='white')
idlabel.grid(row=0,column=0,padx=(0,20),pady=(15,0),sticky='w')
idEntry=CTkEntry(leftFrame,font=('Arial',15,'bold'),width=180)
idEntry.grid(row=0,column=1)

nameLabel=CTkLabel(leftFrame,text='Name',font=('Arial',18,'bold'),text_color='white')
nameLabel.grid(row=1,column=0,padx=(0,20),pady=(15,0),sticky='w')
nameEntry=CTkEntry(leftFrame,font=('Arial',15,'bold'),width=180)
nameEntry.grid(row=1,column=1)

phoneLabel=CTkLabel(leftFrame,text='Phone',font=('Arial',18,'bold'),text_color='white')
phoneLabel.grid(row=2,column=0,padx=(0,20),pady=(15,0),sticky='w')
phoneEntry=CTkEntry(leftFrame,font=('Arial',15,'bold'),width=180)
phoneEntry.grid(row=2,column=1)

roleLabel=CTkLabel(leftFrame,text='Role',font=('Arial',18,'bold'),text_color='white')
roleLabel.grid(row=3,column=0,padx=(0,20),pady=(15,0),sticky='w')

role_options = ["Manager", "Web Developer", "Designer", "Tester", "HR","Software Developer", "Data Analyst", "System Administrator", "Network Engineer", "Database Administrator","UI/UX Designer", "Project Manager", "Business Analyst", "DevOps Engineer", "Security Analyst"]
roleBox=CTkComboBox(leftFrame,values=role_options,width=180,font=('arial',15,'bold'),state='readonly')
roleBox.grid(row=3,column=1)
roleBox.set(role_options[0])  # Set default value to the first option

genderLabel=CTkLabel(leftFrame,text='Gender',font=('Arial',18,'bold'),text_color='white')
genderLabel.grid(row=4,column=0,padx=(0,20),pady=(15,0),sticky='w')

gender_options=['Male','Female']
genderBox=CTkComboBox(leftFrame,values=gender_options,width=180,font=('Arial',15,'bold'),state='readonly')
genderBox.grid(row=4,column=1)
genderBox.set(gender_options[0]) 

salaryLabel=CTkLabel(leftFrame,text='Salary',font=('Arial',18,'bold'),text_color='white')
salaryLabel.grid(row=5,column=0,padx=(0,20),pady=(15,0),sticky='w')
salaryEntry=CTkEntry(leftFrame,font=('Arial',15,'bold'),width=180)
salaryEntry.grid(row=5,column=1)

rightFrame=CTkFrame(window)
rightFrame.grid(row=1,column=1)

search_options = ["ID", "Name", "Phone", "Role","Gender", "Salary"]
searchBox=CTkComboBox(rightFrame,values=search_options,state='readonly')
searchBox.grid(row=0,column=0)
searchBox.set('Search By')

searchEntry=CTkEntry(rightFrame)
searchEntry.grid(row=0,column=1)

searchButton=CTkButton(rightFrame,text='Search',width=100,command=search_employee)
searchButton.grid(row=0,column=2)

showallButton=CTkButton(rightFrame,text='Show All',width=100,command=show_all)
showallButton.grid(row=0,column=3,pady=5)

tree=ttk.Treeview(rightFrame,height=13)
tree.grid(row=1,column=0,columnspan=4)
tree['columns']=('ID','Name','Phone','Role','Gender','Salary')

tree.heading("ID", text="ID")
tree.heading("Name", text="Name")
tree.heading("Phone", text="Phone")
tree.heading("Role", text="Role")
tree.heading("Gender", text="Gender")
tree.heading("Salary",text="Salary")

tree.configure(show='headings')
tree.column("ID", width=80)
tree.column("Name",width=130)
tree.column("Phone",width=130)
tree.column("Role",width=180)
tree.column("Gender",width=100)
tree.column("Salary",width=130)

style=ttk.Style()
style.configure('Treeview.Heading',font=('aerial',18,'bold'))
style.configure('Treeview',font=('aerial',13,'bold'))

buttonFrame=CTkFrame(window,fg_color='#161C30')
buttonFrame.grid(row=2,column=0,columnspan=2)

newButton=CTkButton(buttonFrame,text='New Employee',font=('aerial',15,'bold'),width=160,corner_radius=15,command=lambda: clear(True))
newButton.grid(row=0,column=0,pady=5)

addButton=CTkButton(buttonFrame,text='Add Employee',font=('aerial',15,'bold'),width=160,corner_radius=15,command=add_employee)
addButton.grid(row=0,column=1,pady=5,padx=5)

updateButton=CTkButton(buttonFrame,text='Update Employee',font=('aerial',15,'bold'),width=160,corner_radius=15,command=upadate_employee)
updateButton.grid(row=0,column=2,pady=5,padx=5)

DeleteButton=CTkButton(buttonFrame,text='Delete Employee',font=('aerial',15,'bold'),width=160,corner_radius=15,command=delete_employee)
DeleteButton.grid(row=0,column=3,pady=5,padx=5)

DeleteallButton=CTkButton(buttonFrame,text='Delete all Employee',font=('aerial',15,'bold'),width=160,corner_radius=15,command=delete_all)
DeleteallButton.grid(row=0,column=4,pady=5)

scrollbar=ttk.Scrollbar(rightFrame,orient='vertical',command=tree.yview)
scrollbar.grid(row=1,column=4,sticky='ns')

tree.config(yscrollcommand=scrollbar.set)

treeview_data()
window.bind('<ButtonRelease>',selection)

window.mainloop()
from customtkinter import *
from PIL import Image
from tkinter import messagebox

def login():
    if usernameEntry.get()=='' or passwordEntry.get()=='':
         messagebox.showerror('Error','All fields are required')
    elif usernameEntry.get()=='Pranjal' and passwordEntry.get()=='Pranjal@2005':
        messagebox.showinfo('Success','Login Successful')
        root.destroy()
        import ems
    else:
        messagebox.showerror('Error','Invalid username or password')

root=CTk()
root.geometry('930x478')
root.resizable(0,0)
root.title('Login page')
image=CTkImage(Image.open('cover2.jpg'),size=(930,478))
imagelabel=CTkLabel(root,image=image, text='')
imagelabel.place(x=0,y=0)
headinglabel=CTkLabel(root,text='Employee Management System',bg_color='#f2fafd',font=('Arial',15,'bold'),text_color='#0d6efd')
headinglabel.place(x=20,y=100)
usernameEntry=CTkEntry(root,placeholder_text='Username',width=200,height=40,border_width=2,border_color='#0d6efd',fg_color='#f2fafd',text_color='#0d6efd',font=('Arial',12))
usernameEntry.place(x=20,y=150)
passwordEntry=CTkEntry(root,placeholder_text='Password',width=200,height=40,border_width=2,border_color='#0d6efd',fg_color='#f2fafd',text_color='#0d6efd',font=('Arial',12),show='*')
passwordEntry.place(x=20,y=200)
loginbutton=CTkButton(root,text='Login',width=200,height=40,border_width=2,border_color='#0d6efd',fg_color='#0d6efd',text_color='#f2fafd',font=('Arial',12),cursor='hand2',command=login)
loginbutton.place(x=20,y=250)



root.mainloop()

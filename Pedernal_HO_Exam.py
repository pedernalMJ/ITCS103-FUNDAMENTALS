import tkinter as tk
# from tkinter import PhotoImage

window = tk.Tk()
window.geometry("600x600")
window.title("Pedernal HO Exam")

user_data = {"username": "","password":""}

def open_register():
    t = tk.Toplevel(window)
    t.geometry("300x300")
    t.title("Register")
    t.configure(bg="green")

    ul = tk.Label(t,text="username")
    ul.grid(row=0,column=0)
    ue = tk.Entry(t)
    ue.grid(row=0,column=1)
    
    up = tk.Label(t,text="password")
    up.grid(row=1,column=0)
    upe = tk.Entry(t,show="*")
    upe.grid(row=1,column=1)


    def see_pass():
         check = check_val.get()
         if check == 1:
            upe["show"] = ""

    check_val = tk.IntVar() 
    ck = tk.Checkbutton(t,text="show password",variable=check_val,onvalue=1,command= see_pass)
    ck.grid(row=2,column=1,columnspan=2,padx=5)

    

    result = tk.Label(t,text="",fg="red")
    result.grid(column=1,row=3,columnspan=2)

    

    def register():
        username = ue.get()
        password = upe.get()

        if username == "" or password == "":
            result.config(text="Register properly",fg="red")
        else:
            user_data["username"] = username
            user_data["password"] = password
            result.config(text="Successfuly Registered",fg="green")

        

    bt = tk.Button(t,text="Register",command=register).grid(row=4, column=1, pady=10)

def opem_login():
     t = tk.Toplevel(window)
     t.geometry("300x300")
     t.title("Login")
     t.configure(bg="red")

     ul = tk.Label(t,text="username")
     ul.grid(row=0,column=0)
     ue = tk.Entry(t)
     ue.grid(row=0,column=1)
    
     up = tk.Label(t,text="password")
     up.grid(row=1,column=0)
     upe = tk.Entry(t,show="*")
     upe.grid(row=1,column=1)


     def see_pass():
         check = check_val.get()
         if check == 1:
            upe["show"] = ""

     check_val = tk.IntVar() 
     ck = tk.Checkbutton(t,text="show password",variable=check_val,onvalue=1,command= see_pass)
     ck.grid(row=2,column=1,columnspan=2,padx=5)

     result = tk.Label(t,text="",fg="red")
     result.grid(column=1,row=3,columnspan=2)

     def login():
         username = ue.get()
         password = upe.get() 

         if (user_data["username"] == username and user_data["password"]==password):
            result.config(text=f"Welcome {username}",fg="green")
            
         else:
            result.config(text="Invalid login!", fg="red")

     bt =tk.Button(t,text="Login",command= login ).grid(row=4, column=1, pady=10)

frame = tk.Frame(window, bd=2)
frame.pack()

wel = tk.Label(frame,text="welcome!",width=30 ,anchor="c")
wel.grid(row=0,column=0)

register = tk.Button(frame, text="register",bg= "blue", command=open_register,width=30 ,anchor="c")
register.grid(row=1, column=0)

login = tk.Button(frame, text="Login",bg="green", command=opem_login,width=30 ,anchor="c")
login.grid(row=2, column=0)

window.mainloop()
#  if check_val.get() == 1:
#         labe2 = tk.Label(window,text="rememeber me is clicked")
#         labe2.pack()
#     else:
#         labe2 = tk.Label(window,text="rememeber me is not clicked")
#         labe2.pack()
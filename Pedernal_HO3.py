import tkinter as tk 

window = tk.Tk()
window.geometry("400x400")
window.title("Simple Calculator")
window.resizable(True,True)
window.configure(bg="white")

top_label = tk.Label(window,text="calculate")
top_label.pack()

frame1 = tk.Frame(window,height= 700,width=1080,bg="blue")
frame1.pack()

f1 = tk.Label(frame1,text="Enter First number",bg="white")
f1.grid(row=0,column=0,padx=10,pady=5,sticky="w")
entry1 = tk.Entry(frame1)
entry1.grid(row=0,column=1)

f2=  tk.Label(frame1,text="Enter Second number",bg="white")
f2.grid(row=1,column=0,padx=10,pady=5,sticky="w")
entry2 = tk.Entry(frame1)
entry2.grid(row=1,column=1)

def add ():
    num1 =  float (entry1.get())
    num2 =  float (entry2.get())
    result = num1 + num2 
    top_label ["text"] = f" The sum of {num1} + {num2} is {result}"

def minus ():
    num1 =  float (entry1.get())
    num2 =  float (entry2.get())
    result = num1 - num2 
    top_label ["text"] = f" The sum of {num1} - {num2} is {result}"

def multi ():
    num1 =  float (entry1.get())
    num2 =  float (entry2.get())
    result = num1 * num2 
    top_label ["text"] = f" The sum of {num1} x {num2} is {result}"

def div ():
    num1 =  float (entry1.get())
    num2 =  float (entry2.get())
    result = num1 / num2 
    top_label ["text"] = f" The sum of {num1} x {num2} is {result}"



addb = tk.Button(frame1,text="add",command = add)
addb.grid(row=3,column=0)
addc = tk.Button(frame1,text="minus",command = minus)
addc.grid(row=4,column=0)
addd = tk.Button(frame1,text="multiply",command = minus)
addd.grid(row=3,column=1)
adde = tk.Button(frame1,text="divide",command = div)
adde.grid(row=4,column=1)


# entry1 =
window.mainloop()



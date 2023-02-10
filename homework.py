from tkinter import *
from tkinter import messagebox
root = Tk()
root.title('калькулятор')
root.geometry('500x300')
def function1():
    messagebox.showinfo('Результат', int(entry1.get()) + int(entry2.get()))
def function2():
    messagebox.showinfo('Результат', int(entry1.get()) - int(entry2.get()))
def function3():
    messagebox.showinfo('Результат', int(entry1.get()) * int(entry2.get()))
def function4():
    messagebox.showinfo('Результат', int(entry1.get()) / int(entry2.get()))
def function5():
    messagebox.showinfo('Результат', int(entry1.get()) // int(entry2.get()))
def function6():
    messagebox.showinfo('Результат', int(entry1.get()) % int(entry2.get()))
entry1 = Entry(root, width = 30, bg = 'gray', fg = 'cyan')
entry2 = Entry(root, width = 30, bg = 'gray', fg = 'cyan')
button1 = Button(root, width = 10, height = 3, text='+',command = function1)
button2 = Button(root, width = 10, height = 3, text='-',command = function2)
button3 = Button(root, width = 10, height = 3, text='*',command = function3)
button4 = Button(root, width = 10, height = 3, text='/',command = function4)
button5 = Button(root, width = 10, height = 3, text='//',command = function5)
button6 = Button(root, width = 10, height = 3, text='%',command = function6)
entry1.pack()
entry2.pack()
button1.pack()
button2.pack()
button3.pack()
button4.pack()
button5.pack()
button6.pack()
root.mainloop()
from tkinter import *

root = Tk()
root.title('Books project')

root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=1)

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)
root.columnconfigure(3, weight=1)
root.columnconfigure(4, weight=1)
root.columnconfigure(5, weight=1)

def cat_oper_window():
    global top
    global e
    global text_list

    top=Toplevel()
    top.title('Categories operations')

    top.columnconfigure(0, weight=1)
    top.columnconfigure(1, weight=1)
    top.columnconfigure(2, weight=1)
    top.columnconfigure(3, weight=1)
    top.rowconfigure(0, weight=1)

    e=Entry(top, width=50)
    e.grid(row=0, column=0, sticky='ew')

    add_in_e=Button(top, text='Add category', command=add_to_list)
    add_in_e.grid(row=0, column=1, padx=10, pady=10, sticky='ew')

    delete_in_e = Button(top, text='Delete category', command=delete_from_list)
    delete_in_e.grid(row=0, column=2, padx=10, pady=10, sticky='ew')

    text_list = Listbox(top, width=60, height=20)
    text_list.grid(row=2, column=0, padx=10, pady=10, sticky='nsew')

    text_list_label = Label(top, text='List of categories:')
    text_list_label.grid(row=1, column=0, padx=10, pady=10, sticky='nsew')

    button_quit = Button(top, text='Close window', command=top.destroy)
    button_quit.grid(row=3, column=5)

def add_to_list():
    global text
    text = e.get()
    if text not in text_list.get(0, END):
        text_list.insert(END, text)
        e.delete(0, END)

def delete_from_list():
    size = text_list.size()
    if size > 0:
        text_list.delete(size -1)


myButton1 = Button(root, text='Categories operations', fg='blue', command=cat_oper_window)
myButton1.grid(row=0, column=3, padx=10, pady=10, sticky='ew')

myButton2 = Button(root, text='Authors operations', fg='red')
myButton2.grid(row=1, column=3, padx=10, pady=10, sticky='ew')

myButton3 = Button(root, text='Titles operations', fg='brown')
myButton3.grid(row=2, column=3, padx=10, pady=10, sticky='ew')

button_quit = Button(root, text='Close window', command=root.quit)
button_quit.grid(row=3, column=5)

root.mainloop()
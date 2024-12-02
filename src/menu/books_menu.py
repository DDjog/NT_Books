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

    delete_in_e = Button(top, text='Delete category', command=delete_selected)
    delete_in_e.grid(row=0, column=2, padx=10, pady=10, sticky='ew')

    text_list = Listbox(top, width=60, height=15)
    text_list.grid(row=2, column=0, padx=10, pady=10, sticky='nsew')

    text_list_label = Label(top, text='List of categories:')
    text_list_label.grid(row=1, column=0, padx=10, pady=10, sticky='nsew')

    button_quit = Button(top, text='Close', command=top.destroy)
    button_quit.grid(row=3, column=2)

def aut_oper_window():
    global top
    global e
    global text_list

    top=Toplevel()
    top.title('Authors operations')

    top.columnconfigure(0, weight=1)
    top.columnconfigure(1, weight=1)
    top.columnconfigure(2, weight=1)
    top.columnconfigure(3, weight=1)
    top.rowconfigure(0, weight=1)

    e=Entry(top, width=50)
    e.grid(row=0, column=0, sticky='ew')

    add_in_e=Button(top, text='Add author', command=add_to_list)
    add_in_e.grid(row=0, column=1, padx=10, pady=10, sticky='ew')

    delete_in_e = Button(top, text='Delete author', command=delete_selected)
    delete_in_e.grid(row=0, column=2, padx=10, pady=10, sticky='ew')

    text_list = Listbox(top, width=60, height=15)
    text_list.grid(row=2, column=0, padx=10, pady=10, sticky='nsew')

    text_list_label = Label(top, text='List of authors:')
    text_list_label.grid(row=1, column=0, padx=10, pady=10, sticky='nsew')

    button_quit = Button(top, text='Close', command=top.destroy)
    button_quit.grid(row=3, column=2)

def tit_oper_window():
    global top
    global e
    global text_list

    top=Toplevel()
    top.title('Titles operations')

    top.columnconfigure(0, weight=1)
    top.columnconfigure(1, weight=1)
    top.columnconfigure(2, weight=1)
    top.columnconfigure(3, weight=1)
    top.rowconfigure(0, weight=1)

    e=Entry(top, width=50)
    e.grid(row=0, column=0, sticky='ew')

    add_in_e=Button(top, text='Add title', command=add_to_list)
    add_in_e.grid(row=0, column=1, padx=10, pady=10, sticky='ew')

    delete_in_e = Button(top, text='Delete title', command=delete_selected)
    delete_in_e.grid(row=0, column=2, padx=10, pady=10, sticky='ew')

    text_list = Listbox(top, width=60, height=15)
    text_list.grid(row=2, column=0, padx=10, pady=10, sticky='nsew')

    text_list_label = Label(top, text='List of titles:')
    text_list_label.grid(row=1, column=0, padx=10, pady=10, sticky='nsew')

    button_quit = Button(top, text='Close', command=top.destroy)
    button_quit.grid(row=3, column=2)

def add_to_list():
    global text
    text = e.get()
    if text not in text_list.get(0, END):
        text_list.insert(END, text)
        e.delete(0, END)

def selected_to_be_deleted():
    global selected_indicates
    selected_indicates= text_list.curselection()

    if selected_indicates:
        return selected_indicates[0]
    else:
        return None

def delete_selected():
    selected_index = text_list.curselection()

    if selected_index:
        text_list.delete(selected_index)
    else:
        print('No record to be deleted')

myButton1 = Button(root, text='Categories operations', fg='blue', command=cat_oper_window)
myButton1.grid(row=0, column=3, padx=10, pady=10, sticky='ew')

myButton2 = Button(root, text='Authors operations', fg='red', command=aut_oper_window)
myButton2.grid(row=1, column=3, padx=10, pady=10, sticky='ew')

myButton3 = Button(root, text='Titles operations', fg='brown', command= tit_oper_window)
myButton3.grid(row=2, column=3, padx=10, pady=10, sticky='ew')

button_quit = Button(root, text='Close', command=root.quit)
button_quit.grid(row=2, column=5)

root.mainloop()
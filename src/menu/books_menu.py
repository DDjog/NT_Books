from tkinter import *

from src.operations.category_operations import add_category, get_categories_list, delete_category
from src.operations.author_operations import add_author, delete_author
from src.operations.title_operations import add_title, delete_title
from src.operations.language_operations import add_language, get_languages_list, delete_language
from src.operations.tag_operations import add_tag, get_tags_list, delete_tag
from src.tests.test_delete_author import author_surname
from src.tests.test_is_author_in_db import author_name

root = Tk()
root.title('Books project')

root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=1)
root.rowconfigure(3, weight=1)
root.rowconfigure(4, weight=1)
root.rowconfigure(5, weight=1)

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
    top.grab_set()

    top.title('Categories operations')

    top.columnconfigure(0, weight=1)
    top.columnconfigure(1, weight=1)
    top.columnconfigure(2, weight=1)
    top.columnconfigure(3, weight=1)
    top.rowconfigure(0, weight=1)

    e=Entry(top, width=50)
    e.grid(row=0, column=0, sticky='ew')

    add_in_e=Button(top, text='Add category', command=add_category_to_list)
    add_in_e.grid(row=0, column=1, padx=10, pady=10, sticky='ew')

    delete_in_e = Button(top, text='Delete category', command=delete_selected_category)
    delete_in_e.grid(row=0, column=2, padx=10, pady=10, sticky='ew')

    text_list = Listbox(top, width=60, height=15)
    text_list.grid(row=2, column=0, padx=10, pady=10, sticky='nsew')

    l=get_categories_list()
    for i in l:
        text_list.insert(END, i.category_name)

    text_list_label = Label(top, text='List of categories:')
    text_list_label.grid(row=1, column=0, padx=10, pady=10, sticky='nsew')

    button_quit = Button(top, text='Close', command=top.destroy)
    button_quit.grid(row=3, column=2)

def aut_oper_window():
    global top
    global e
    global text_list

    top=Toplevel()
    top.grab_set()
    top.title('Authors operations')

    top.columnconfigure(0, weight=1)
    top.columnconfigure(1, weight=1)
    top.columnconfigure(2, weight=1)
    top.columnconfigure(3, weight=1)
    top.rowconfigure(0, weight=1)

    e=Entry(top, width=50)
    e.grid(row=0, column=0, sticky='ew')

    add_in_e=Button(top, text='Add author', command=add_author_to_list)
    add_in_e.grid(row=0, column=1, padx=10, pady=10, sticky='ew')

    delete_in_e = Button(top, text='Delete author', command=delete_selected_author)
    delete_in_e.grid(row=0, column=2, padx=10, pady=10, sticky='ew')

    text_list = Listbox(top, width=60, height=15)
    text_list.grid(row=2, column=0, padx=10, pady=10, sticky='nsew')

    # l = get_authors_list()
    # for i in l:
    #     text_list.insert(END, i.auth)

    text_list_label = Label(top, text='List of authors:')
    text_list_label.grid(row=1, column=0, padx=10, pady=10, sticky='nsew')

    button_quit = Button(top, text='Close', command=top.destroy)
    button_quit.grid(row=3, column=2)

def tit_oper_window():
    global top
    global e
    global text_list

    top=Toplevel()
    top.grab_set()
    top.title('Titles operations')

    top.columnconfigure(0, weight=1)
    top.columnconfigure(1, weight=1)
    top.columnconfigure(2, weight=1)
    top.columnconfigure(3, weight=1)
    top.rowconfigure(0, weight=1)

    e=Entry(top, width=50)
    e.grid(row=0, column=0, sticky='ew')

    add_in_e=Button(top, text='Add title', command=add_title_to_list)
    add_in_e.grid(row=0, column=1, padx=10, pady=10, sticky='ew')

    delete_in_e = Button(top, text='Delete title', command=delete_selected_title)
    delete_in_e.grid(row=0, column=2, padx=10, pady=10, sticky='ew')

    text_list = Listbox(top, width=60, height=15)
    text_list.grid(row=2, column=0, padx=10, pady=10, sticky='nsew')

    # l = get_titles_list()
    # for i in l:
    #     text_list.insert(END, i)

    text_list_label = Label(top, text='List of titles:')
    text_list_label.grid(row=1, column=0, padx=10, pady=10, sticky='nsew')

    button_quit = Button(top, text='Close', command=top.destroy)
    button_quit.grid(row=3, column=2)

def lang_oper_window():
    global top
    global e
    global text_list

    top=Toplevel()
    top.grab_set()

    top.title('Languages operations')

    top.columnconfigure(0, weight=1)
    top.columnconfigure(1, weight=1)
    top.columnconfigure(2, weight=1)
    top.columnconfigure(3, weight=1)
    top.rowconfigure(0, weight=1)

    e=Entry(top, width=50)
    e.grid(row=0, column=0, sticky='ew')

    add_in_e=Button(top, text='Add language', command=add_language_to_list)
    add_in_e.grid(row=0, column=1, padx=10, pady=10, sticky='ew')

    delete_in_e = Button(top, text='Delete language', command=delete_selected_language)
    delete_in_e.grid(row=0, column=2, padx=10, pady=10, sticky='ew')

    text_list = Listbox(top, width=60, height=15)
    text_list.grid(row=2, column=0, padx=10, pady=10, sticky='nsew')

    l=get_languages_list()
    for i in l:
        text_list.insert(END, i.language)

    text_list_label = Label(top, text='List of languages:')
    text_list_label.grid(row=1, column=0, padx=10, pady=10, sticky='nsew')

    button_quit = Button(top, text='Close', command=top.destroy)
    button_quit.grid(row=3, column=2)

def tag_oper_window():
    global top
    global e
    global text_list

    top=Toplevel()
    top.grab_set()

    top.title('Tags operations')

    top.columnconfigure(0, weight=1)
    top.columnconfigure(1, weight=1)
    top.columnconfigure(2, weight=1)
    top.columnconfigure(3, weight=1)
    top.rowconfigure(0, weight=1)

    e=Entry(top, width=50)
    e.grid(row=0, column=0, sticky='ew')

    add_in_e=Button(top, text='Add tag', command=add_tag_to_list)
    add_in_e.grid(row=0, column=1, padx=10, pady=10, sticky='ew')

    delete_in_e = Button(top, text='Delete tag', command=delete_selected_tag)
    delete_in_e.grid(row=0, column=2, padx=10, pady=10, sticky='ew')

    text_list = Listbox(top, width=60, height=15)
    text_list.grid(row=2, column=0, padx=10, pady=10, sticky='nsew')

    l=get_tags_list()
    for i in l:
        text_list.insert(END, i.tag)

    text_list_label = Label(top, text='List of tags:')
    text_list_label.grid(row=1, column=0, padx=10, pady=10, sticky='nsew')

    button_quit = Button(top, text='Close', command=top.destroy)
    button_quit.grid(row=3, column=2)

def add_category_to_list():
    global text
    text = e.get()
    if text not in text_list.get(0, END):
        add_category(text)
        text_list.insert(END, text)
        e.delete(0, END)

def add_author_to_list():
    global text
    text = e.get()
    if text not in text_list.get(0, END):
        add_author(text[0], text[1])
        text_list.insert(END, text)
        e.delete(0, END)

def add_title_to_list():
    global text
    text = e.get()
    if text not in text_list.get(0, END):
        add_title(text)
        text_list.insert(END, text)
        e.delete(0, END)

def add_language_to_list():
    global text
    text = e.get()
    if text not in text_list.get(0, END):
        add_language(text)
        text_list.insert(END, text)
        e.delete(0, END)

def add_tag_to_list():
    global text
    text = e.get()
    if text not in text_list.get(0, END):
        add_tag(text)
        text_list.insert(END, text)
        e.delete(0, END)

def selected_to_be_deleted():
    global selected_indicate
    selected_indicate= text_list.curselection()

    if selected_indicate:
        return selected_indicate[0]
    else:
        return None

def delete_selected_category():
    selected_index = text_list.curselection()

    if selected_index:
        delete_category(text_list.get(selected_index))
        text_list.delete(selected_index)
    else:
        print('No record to be deleted')

def delete_selected_author():

    selected = text_list.curselection()

    if not selected:
        print('No record to be deleted')
        
    selected = selected[0]
    selected_author =  text_list.get(selected)
    parts = selected_author.split()
    author_name = parts[0]
    author_surname = parts[1]

    delete_author(author_name, author_surname)
    text_list.delete(selected)



def delete_selected_title():
    selected_index = text_list.curselection()

    if selected_index:
        delete_title(text_list.get(selected_index))
        text_list.delete(selected_index)
    else:
        print('No record to be deleted')

def delete_selected_language():
    selected_index = text_list.curselection()

    if selected_index:
        delete_language(text_list.get(selected_index))
        text_list.delete(selected_index)
    else:
        print('No record to be deleted')

def delete_selected_tag():
    selected_index = text_list.curselection()

    if selected_index:
        delete_tag(text_list.get(selected_index))
        text_list.delete(selected_index)
    else:
        print('No record to be deleted')

myButton1 = Button(root, text='Categories operations', fg='blue', command=cat_oper_window)
myButton1.grid(row=0, column=3, padx=10, pady=10, sticky='ew')

myButton2 = Button(root, text='Authors operations', fg='red', command=aut_oper_window)
myButton2.grid(row=1, column=3, padx=10, pady=10, sticky='ew')

myButton3 = Button(root, text='Titles operations', fg='brown', command= tit_oper_window)
myButton3.grid(row=2, column=3, padx=10, pady=10, sticky='ew')

myButton4 = Button(root, text='Languages operations', fg='green', command= lang_oper_window)
myButton4.grid(row=3, column=3, padx=10, pady=10, sticky='ew')

myButton5 = Button(root, text='Tags operations', fg='purple', command= tag_oper_window)
myButton5.grid(row=4, column=3, padx=10, pady=10, sticky='ew')

button_quit = Button(root, text='Close', command=root.quit)
button_quit.grid(row=4, column=5)

root.mainloop()
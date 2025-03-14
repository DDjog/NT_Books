from tkinter import *

import logging

from src.constans import OPER_GET_LIST_SUCCEEDED
from src.operations.category_operations import add_category, get_categories_list, delete_category
from src.operations.author_operations import add_author, delete_author, get_authors_list, update_author
from src.operations.title_operations import add_title, delete_title, get_titles_list
from src.operations.language_operations import add_language, get_languages_list, delete_language
from src.operations.tag_operations import add_tag, get_tags_list, delete_tag

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

    operation_status, l=get_categories_list()
    if operation_status == OPER_GET_LIST_SUCCEEDED:
        for i in l:
            text_list.insert(END, i.category_name)


    text_list_label = Label(top, text='List of categories:')
    text_list_label.grid(row=1, column=0, padx=10, pady=10, sticky='nsew')

    button_update = Button(top, text='Update category', command=update_category_window)
    button_update.grid(row=1, column=1, padx=10, pady=10, sticky='nsew')

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

    button_update = Button(top, text='Update author', command=update_author_window)
    button_update.grid(row=1, column=1, padx=10, pady=10, sticky='nsew')

    operation_status, l = get_authors_list()
    if operation_status == OPER_GET_LIST_SUCCEEDED:
        for i in l:
            text_list.insert(END, f'{i.author_name} {i.author_surname}')

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

    button_update = Button(top, text='Update title', command=update_title_window)
    button_update.grid(row=1, column=1, padx=10, pady=10, sticky='nsew')

    operation_status, l = get_titles_list()
    if operation_status == OPER_GET_LIST_SUCCEEDED:
        for i in l:
            text_list.insert(END, i.title)

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

    button_update = Button(top, text='Update language', command=update_language_window)
    button_update.grid(row=1, column=1, padx=10, pady=10, sticky='nsew')

    operation_status, l = get_languages_list()
    if operation_status == OPER_GET_LIST_SUCCEEDED:
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

    button_update = Button(top, text='Update tag', command=update_tag_window)
    button_update.grid(row=1, column=1, padx=10, pady=10, sticky='nsew')

    operation_status, l = get_tags_list()
    if operation_status == OPER_GET_LIST_SUCCEEDED:
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
        logging.info('Category added to the list')
    else:
        logging.info('Category is already on the list')
        return None

def add_author_to_list():
    global text
    text = e.get()
    if text not in text_list.get(0, END):
        add_author(text[0], text[1])
        text_list.insert(END, text)
        e.delete(0, END)
        logging.info('Author added to the list')
    else:
        logging.info('Author is already on the list')
        return None

def add_title_to_list():
    global text
    text = e.get()
    if text not in text_list.get(0, END):
        add_title(text)
        text_list.insert(END, text)
        e.delete(0, END)
        logging.info('Title added to the list')
    else:
        logging.info('Title is already on the list')
        return None

def add_language_to_list():
    global text
    text = e.get()
    if text not in text_list.get(0, END):
        add_language(text)
        text_list.insert(END, text)
        e.delete(0, END)
        logging.info('Language added to the list')
    else:
        logging.info('Language is already on the list')
        return None

def add_tag_to_list():
    global text
    text = e.get()
    if text not in text_list.get(0, END):
        add_tag(text)
        text_list.insert(END, text)
        e.delete(0, END)
        logging.info('Tag added to the list')
    else:
        logging.info('Tag is already on the list')
        return None

def selected_to_be_deleted():
    global selected_indicate
    selected_indicate= text_list.curselection()

    if selected_indicate:
        logging.info('Selected to be deleted')
        return selected_indicate[0]
    else:
        logging.info('Nothing to be deleted')
        return None

def delete_selected_category():
    selected = text_list.curselection()

    if not selected:
        logging.info('No record to be deleted')
        return None

    selected = selected[0]
    delete_category(text_list.get(selected))
    text_list.delete(selected)
    logging.info('Category deleted')

def delete_selected_author():

    selected = text_list.curselection()

    if not selected:
        logging.info('No record to be deleted')

    selected = selected[0]
    selected_author =  text_list.get(selected)
    parts = selected_author.split()
    author_name = parts[0]
    author_surname = parts[1]

    delete_author(author_name, author_surname)
    text_list.delete(selected)
    logging.info('Author deleted')

def delete_selected_title():
    selected = text_list.curselection()

    if selected:
        delete_title(text_list.get(selected))
        text_list.delete(selected)
        logging.info('Title deleted')
    else:
        logging.info('No record to be deleted')

def delete_selected_language():
    selected = text_list.curselection()

    if selected:
        delete_language(text_list.get(selected))
        text_list.delete(selected)
        logging.info('Language deleted')
    else:
        logging.info('No record to be deleted')

def delete_selected_tag():
    selected = text_list.curselection()

    if selected:
        delete_tag(text_list.get(selected))
        text_list.delete(selected)
        logging.info('Tag deleted')
    else:
        logging.info('No record to be deleted')


def update_category_window():
    global old_category_name
    global new_category_name
    global selected_category

    top = Toplevel()
    top.grab_set()

    top.columnconfigure(0, weight=1)
    top.columnconfigure(1, weight=1)
    top.columnconfigure(2, weight=1)
    top.columnconfigure(3, weight=1)
    top.rowconfigure(0, weight=1)

    top.title('Update category')
    selected_category = text_list.curselection()

    old_category_name = Entry(top, width=50)
    old_category_name.grid(row=0, column=1, sticky='ew')
    if selected_category:
        selected_index = selected_category[0]
        selected_category_content = text_list.get(selected_index)
        old_category_name.insert(0, selected_category_content)

    new_category_name = Entry(top, width=50)
    new_category_name.grid(row=1, column=1, sticky='ew')

    old_category_label = Label(top, text='from')
    old_category_label.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')

    new_category_label = Label(top, text='to')
    new_category_label.grid(row=1, column=0, padx=10, pady=10, sticky='nsew')

    button_update = Button(top, text='Press to update', command=lambda: update_category(new_category_name, selected_index))
    button_update.grid(row=2, column=1, padx=10, pady=10)

    button_close = Button(top, text='Close', command=top.destroy)
    button_close.grid(row=2, column=2, padx=10, pady=10)

def update_category(new_category_name, selected_index):

    updated_category = new_category_name.get()
    if not updated_category:
        logging.info("No category indicated for an update")
        return None

    selected_category_text = text_list.get(selected_index)
    delete_category(selected_category_text)

    categories_list = []
    for item in text_list.get(0, END):
        categories_list.append(item.strip())
    if updated_category in categories_list:
        logging.info('Category is already on categories list')
        return None
    add_category(updated_category)

    text_list.delete(selected_index)
    text_list.insert(selected_index, updated_category)
    logging.info('Category updated')

def update_author_window():
    global old_author_
    global new_author
    global selected_author

    top = Toplevel()
    top.grab_set()

    top.columnconfigure(0, weight=1)
    top.columnconfigure(1, weight=1)
    top.columnconfigure(2, weight=1)
    top.columnconfigure(3, weight=1)
    top.rowconfigure(0, weight=1)

    top.title('Update author')
    selected_author = text_list.curselection()

    old_author = Entry(top, width=50)
    old_author.grid(row=0, column=1, sticky='ew')
    if selected_author:
        selected_index = selected_author[0]
        selected_author_content = text_list.get(selected_index)
        old_author.insert(0, selected_author_content)

    new_author = Entry(top, width=50)
    new_author.grid(row=1, column=1, sticky='ew')

    old_author_label = Label(top, text='from')
    old_author_label.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')

    new_author_label = Label(top, text='to')
    new_author_label.grid(row=1, column=0, padx=10, pady=10, sticky='nsew')

    button_update = Button(top, text='Press to update', command=lambda: update_author(new_author, selected_index))
    button_update.grid(row=2, column=1, padx=10, pady=10)

    button_close = Button(top, text='Close', command=top.destroy)
    button_close.grid(row=2, column=2, padx=10, pady=10)

def update_author(new_author, selected_index):

    updated_author = new_author.get()
    if not updated_author:
        logging.info("No author indicated for an update")
        return None

    selected_author_text = text_list.get(selected_index)
    delete_author(selected_author_text)

    authors_list = text_list.get(0, END)
    if updated_author in authors_list:
        logging.info('Author is already on authors list')
        return None
    add_category(updated_author)

    text_list.delete(selected_index)
    text_list.insert(selected_index, updated_author)
    logging.info('Author updated')

def update_title_window():
    global old_title
    global new_title
    global selected_title

    top = Toplevel()
    top.grab_set()

    top.columnconfigure(0, weight=1)
    top.columnconfigure(1, weight=1)
    top.columnconfigure(2, weight=1)
    top.columnconfigure(3, weight=1)
    top.rowconfigure(0, weight=1)

    top.title('Update title')
    selected_title = text_list.curselection()

    old_title = Entry(top, width=50)
    old_title.grid(row=0, column=1, sticky='ew')
    if selected_title:
        selected_index = selected_title[0]
        selected_title_content = text_list.get(selected_index)
        old_title.insert(0, selected_title_content)

    new_title = Entry(top, width=50)
    new_title.grid(row=1, column=1, sticky='ew')

    old_title_label = Label(top, text='from')
    old_title_label.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')

    new_title_label = Label(top, text='to')
    new_title_label.grid(row=1, column=0, padx=10, pady=10, sticky='nsew')

    button_update = Button(top, text='Press to update', command=lambda: update_title(new_title, selected_index))
    button_update.grid(row=2, column=1, padx=10, pady=10)

    button_close = Button(top, text='Close', command=top.destroy)
    button_close.grid(row=2, column=2, padx=10, pady=10)

def update_title(new_title, selected_index):

    updated_title = new_title.get()
    if not updated_title:
        logging.info("No title indicated for an update")
        return None

    selected_title_text = text_list.get(selected_index)
    delete_title(selected_title_text)

    authors_list = text_list.get(0, END)
    if updated_title in authors_list:
        logging.info('Title is already on authors list')
        return None
    add_title(updated_title)

    text_list.delete(selected_index)
    text_list.insert(selected_index, updated_title)
    logging.info('Title updated')

def update_language_window():
    global old_language
    global new_language
    global selected_language

    top = Toplevel()
    top.grab_set()

    top.columnconfigure(0, weight=1)
    top.columnconfigure(1, weight=1)
    top.columnconfigure(2, weight=1)
    top.columnconfigure(3, weight=1)
    top.rowconfigure(0, weight=1)

    top.title('Update language')
    selected_language = text_list.curselection()

    old_language = Entry(top, width=50)
    old_language.grid(row=0, column=1, sticky='ew')
    if selected_language:
        selected_index = selected_language[0]
        selected_language_content = text_list.get(selected_index)
        old_language.insert(0, selected_language_content)

    new_language = Entry(top, width=50)
    new_language.grid(row=1, column=1, sticky='ew')

    old_language_label = Label(top, text='from')
    old_language_label.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')

    new_language_label = Label(top, text='to')
    new_language_label.grid(row=1, column=0, padx=10, pady=10, sticky='nsew')

    button_update = Button(top, text='Press to update', command=lambda: update_language(new_language, selected_index))
    button_update.grid(row=2, column=1, padx=10, pady=10)

    button_close = Button(top, text='Close', command=top.destroy)
    button_close.grid(row=2, column=2, padx=10, pady=10)

def update_language(new_languge, selected_index):

    updated_language = new_language.get()
    if not updated_language:
        logging.info("No language indicated for an update")
        return None

    selected_language_text = text_list.get(selected_index)
    delete_language(selected_language_text)

    languages_list = text_list.get(0, END)
    if updated_language in languages_list:
        logging.info('Language is already on authors list')
        return None
    add_title(updated_language)

    text_list.delete(selected_index)
    text_list.insert(selected_index, updated_language)
    logging.info('Language updated')

def update_tag_window():
    global old_tag
    global new_tag
    global selected_tag

    top = Toplevel()
    top.grab_set()

    top.columnconfigure(0, weight=1)
    top.columnconfigure(1, weight=1)
    top.columnconfigure(2, weight=1)
    top.columnconfigure(3, weight=1)
    top.rowconfigure(0, weight=1)

    top.title('Update tag')
    selected_tag = text_list.curselection()

    old_tag = Entry(top, width=50)
    old_tag.grid(row=0, column=1, sticky='ew')
    if selected_tag:
        selected_index = selected_tag[0]
        selected_tag_content = text_list.get(selected_index)
        old_tag.insert(0, selected_tag_content)

    new_tag = Entry(top, width=50)
    new_tag.grid(row=1, column=1, sticky='ew')

    old_tag_label = Label(top, text='from')
    old_tag_label.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')

    new_tag_label = Label(top, text='to')
    new_tag_label.grid(row=1, column=0, padx=10, pady=10, sticky='nsew')

    button_update = Button(top, text='Press to update', command=lambda: update_tag(new_tag, selected_index))
    button_update.grid(row=2, column=1, padx=10, pady=10)

    button_close = Button(top, text='Close', command=top.destroy)
    button_close.grid(row=2, column=2, padx=10, pady=10)

def update_tag(new_tag, selected_index):

    updated_tag = new_tag.get()
    if not updated_tag:
        logging.info("No tag indicated for an update")
        return None

    selected_tag_text = text_list.get(selected_index)
    delete_tag(selected_tag_text)

    tags_list = text_list.get(0, END)
    if updated_tag in tags_list:
        logging.info('Tag is already on authors list')
        return None
    add_title(updated_tag)

    text_list.delete(selected_index)
    text_list.insert(selected_index, updated_tag)
    logging.info('Title updated')


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
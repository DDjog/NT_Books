from operator import length_hint
from os.path import split
from tkinter import *
from PIL import Image, ImageTk
import pygame
import logging
import time
import io
from tkinter import ttk
from tkinter import messagebox

from sqlalchemy.exc import OperationalError
from sqlalchemy.sql.operators import filter_op

from src.database.db import session
from src.database.models import Author, Category, Tag, Title, Language, Book


from sqlalchemy import column

import src.logging_to_file

from src.constans import *
from src.operations.category_operations import add_category, get_categories_list, delete_category, update_category
from src.operations.author_operations import add_author, delete_author, get_authors_list, update_author
from src.operations.title_operations import add_title, delete_title, get_titles_list
from src.operations.language_operations import add_language, get_languages_list, delete_language
from src.operations.tag_operations import add_tag, get_tags_list, delete_tag
from src.operations.cover_page_operations import add_cover_page, delete_cover_page, get_cover_page, get_cover_page_list
from src.tests_author.test_delete_author import author_surname
from src.tests_author.test_is_author_in_db import author_name
from src.tests_book.test_add_book import operation_status, new_author_surname, new_category
from src.tests_book.test_update_book import new_author_name, new_title
from src.tests_category.test_get_categories_list import categories_list
from src.tests_title.test_get_titles_list import titles_list

root = Tk()
clock_label = None
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
    global c_text_list
    global e_category

    top=Toplevel()
    top.grab_set()
    top.title('Categories operations')

    top.columnconfigure(0, weight=1)
    top.columnconfigure(1, weight=1)
    top.columnconfigure(2, weight=1)
    top.columnconfigure(3, weight=1)
    top.rowconfigure(0, weight=1)

    e_category=Entry(top, width=50)
    e_category.grid(row=0, column=0, sticky='ew')

    add_in_e=Button(top, text='Add category', command=add_category_to_db)
    add_in_e.grid(row=0, column=1, padx=10, pady=10, sticky='ew')

    delete_in_e = Button(top, text='Delete category', command=delete_selected_category)
    delete_in_e.grid(row=0, column=2, padx=10, pady=10, sticky='ew')

    c_text_list = Listbox(top, width=60, height=15)
    c_text_list.grid(row=2, column=0, padx=10, pady=10, sticky='nsew')

    operation_status, l=get_categories_list()
    if operation_status == OPER_GET_LIST_SUCCEEDED:
        for i in l:
            c_text_list.insert(END, i.category_name)


    c_text_list_label = Label(top, text='List of categories:')
    c_text_list_label.grid(row=1, column=0, padx=10, pady=10, sticky='nsew')

    button_update = Button(top, text='Update category', command=update_category_window)
    button_update.grid(row=1, column=1, padx=10, pady=10, sticky='nsew')

    button_quit = Button(top, text='Close', command=top.destroy)
    button_quit.grid(row=3, column=2)

def aut_oper_window():
    global e
    global a_text_list

    a_top=Toplevel()
    a_top.grab_set()
    a_top.title('Authors operations')

    a_top.columnconfigure(0, weight=1)
    a_top.columnconfigure(1, weight=1)
    a_top.columnconfigure(2, weight=1)
    a_top.columnconfigure(3, weight=1)
    a_top.rowconfigure(0, weight=1)

    e=Entry(a_top, width=50)
    e.grid(row=0, column=0, sticky='ew')

    add_in_e=Button(a_top, text='Add author', command=add_author_to_db)
    add_in_e.grid(row=0, column=1, padx=10, pady=10, sticky='ew')

    delete_in_e = Button(a_top, text='Delete author', command=delete_selected_author)
    delete_in_e.grid(row=0, column=2, padx=10, pady=10, sticky='ew')

    a_text_list = Listbox(a_top, width=60, height=15)
    a_text_list.grid(row=2, column=0, padx=10, pady=10, sticky='nsew')

    button_update = Button(a_top, text='Update author', command=update_author_window)
    button_update.grid(row=1, column=1, padx=10, pady=10, sticky='nsew')

    operation_status, l = get_authors_list()
    if operation_status == OPER_GET_LIST_SUCCEEDED:
        for i in l:
            a_text_list.insert(END, f'{i.author_name} {i.author_surname}')

    a_text_list_label = Label(a_top, text='List of authors:')
    a_text_list_label.grid(row=1, column=0, padx=10, pady=10, sticky='nsew')

    button_quit = Button(a_top, text='Close', command=a_top.destroy)
    button_quit.grid(row=3, column=2)

def tit_oper_window():
    global t_text_list
    global e_title

    t_top=Toplevel()
    t_top.grab_set()
    t_top.title('Titles operations')

    t_top.columnconfigure(0, weight=1)
    t_top.columnconfigure(1, weight=1)
    t_top.columnconfigure(2, weight=1)
    t_top.columnconfigure(3, weight=1)
    t_top.rowconfigure(0, weight=1)
    t_top.rowconfigure(1, weight=1)
    t_top.rowconfigure(2, weight=1)
    t_top.rowconfigure(3, weight=1)


    e_title=Entry(t_top, width=50)
    e_title.grid(row=0, column=0, sticky='ew')

    add_in_e=Button(t_top, text='Add title', command=add_title_to_db)
    add_in_e.grid(row=0, column=1, padx=10, pady=10, sticky='ew')

    delete_in_e = Button(t_top, text='Delete title', command=delete_selected_title)
    delete_in_e.grid(row=0, column=3, padx=10, pady=10, sticky='ew')



    button_update = Button(t_top, text='Update title', command=update_title_window)
    button_update.grid(row=1, column=1, padx=10, pady=10, sticky='nsew')

    operation_status, t = get_titles_list()
    if operation_status == OPER_GET_LIST_SUCCEEDED:
        for i in t:
            t_text_list.insert(END, i.title)

    t_text_list_label = Label(t_top, text='List of titles:')
    t_text_list_label.grid(row=1, column=0, padx=10, pady=10, sticky='nsew')

    button_quit = Button(t_top, text='Close', command=t_top.destroy)
    button_quit.grid(row=3, column=2)

def lang_oper_window():
    global l_text_list
    global e

    l_top=Toplevel()
    l_top.grab_set()

    l_top.title('Languages operations')

    l_top.columnconfigure(0, weight=1)
    l_top.columnconfigure(1, weight=1)
    l_top.columnconfigure(2, weight=1)
    l_top.columnconfigure(3, weight=1)
    l_top.rowconfigure(0, weight=1)

    e=Entry(l_top, width=50)
    e.grid(row=0, column=0, sticky='ew')

    add_in_e=Button(l_top, text='Add language', command=add_language_to_db)
    add_in_e.grid(row=0, column=1, padx=10, pady=10, sticky='ew')

    delete_in_e = Button(l_top, text='Delete language', command=delete_selected_language)
    delete_in_e.grid(row=0, column=2, padx=10, pady=10, sticky='ew')

    l_text_list = Listbox(l_top, width=60, height=15)
    l_text_list.grid(row=2, column=0, padx=10, pady=10, sticky='nsew')

    button_update = Button(l_top, text='Update language', command=update_language_window)
    button_update.grid(row=1, column=1, padx=10, pady=10, sticky='nsew')

    operation_status, l = get_languages_list()
    if operation_status == OPER_GET_LIST_SUCCEEDED:
        for i in l:
            l_text_list.insert(END, i.language)

    l_text_list_label = Label(l_top, text='List of languages:')
    l_text_list_label.grid(row=1, column=0, padx=10, pady=10, sticky='nsew')

    button_quit = Button(l_top, text='Close', command=l_top.destroy)
    button_quit.grid(row=3, column=2)

def tag_oper_window():
    global ta_text_list
    global e

    ta_top=Toplevel()
    ta_top.grab_set()

    ta_top.title('Tags operations')

    ta_top.columnconfigure(0, weight=1)
    ta_top.columnconfigure(1, weight=1)
    ta_top.columnconfigure(2, weight=1)
    ta_top.columnconfigure(3, weight=1)
    ta_top.rowconfigure(0, weight=1)

    e=Entry(ta_top, width=50)
    e.grid(row=0, column=0, sticky='ew')

    add_in_e=Button(ta_top, text='Add tag', command=add_tag_to_db)
    add_in_e.grid(row=0, column=1, padx=10, pady=10, sticky='ew')

    delete_in_e = Button(ta_top, text='Delete tag', command=delete_selected_tag)
    delete_in_e.grid(row=0, column=2, padx=10, pady=10, sticky='ew')

    ta_text_list = Listbox(ta_top, width=60, height=15)
    ta_text_list.grid(row=2, column=0, padx=10, pady=10, sticky='nsew')

    button_update = Button(ta_top, text='Update tag', command=update_tag_window)
    button_update.grid(row=1, column=1, padx=10, pady=10, sticky='nsew')

    operation_status, l = get_tags_list()
    if operation_status == OPER_GET_LIST_SUCCEEDED:
        for i in l:
            ta_text_list.insert(END, i.tag)

    ta_text_list_label = Label(ta_top, text='List of tags:')
    ta_text_list_label.grid(row=1, column=0, padx=10, pady=10, sticky='nsew')

    button_quit = Button(ta_top, text='Close', command=ta_top.destroy)
    button_quit.grid(row=3, column=2)

def cover_page_oper_window():
    global cp_text_list
    global e

    cp_top=Toplevel()
    cp_top.grab_set()

    cp_top.title('Cover page operations')

    cp_top.columnconfigure(0, weight=1)
    cp_top.columnconfigure(1, weight=1)
    cp_top.columnconfigure(2, weight=1)
    cp_top.columnconfigure(3, weight=1)
    cp_top.rowconfigure(0, weight=1)

    e_cover_page_text_list=Entry(cp_top, width=50)
    e_cover_page_text_list.grid(row=0, column=0, sticky='ew')

    add_in_e=Button(cp_top, text='Add cover page', command=add_cover_page_to_list)
    add_in_e.grid(row=0, column=1, padx=10, pady=10, sticky='ew')

    delete_in_e = Button(cp_top, text='Delete cover page', command=delete_selected_cover_page)
    delete_in_e.grid(row=0, column=2, padx=10, pady=10, sticky='ew')

    cp_text_list = Listbox(cp_top, width=60, height=15)
    cp_text_list.grid(row=2, column=0, padx=10, pady=10, sticky='nsew')

    button_update = Button(cp_top, text='Update cover page', command=update_cover_page_window)
    button_update.grid(row=1, column=1, padx=10, pady=10, sticky='nsew')

    operation_status, cover_pages = get_cover_page_list()
    if operation_status == OPER_GET_LIST_SUCCEEDED:
        for cp in cover_pages:
            cp_text_list.insert(END, cp.cover_page)

    cp_text_list_label = Label(cp_top, text='List of cover pages:')
    cp_text_list_label.grid(row=1, column=0, padx=10, pady=10, sticky='nsew')

    button_quit = Button(cp_top, text='Close', command=cp_top.destroy)
    button_quit.grid(row=3, column=2)

def books_oper_window():
    global book_text_list
    global e_titles_list
    global e_authors_list
    global e_languages_list
    global e_categories_list
    global e_tags_list
    global e_author
    global b_top
    global e_category
    global e_title
    global e_language
    global e_tag



    b_top = Toplevel()
    b_top.grab_set()

    b_top.title('Books operations')

    b_top.columnconfigure(0, weight=1)
    b_top.columnconfigure(1, weight=1)
    b_top.columnconfigure(2, weight=1)
    b_top.columnconfigure(3, weight=1)
    b_top.rowconfigure(0, weight=1)


    operation_status, titles = get_titles_list()
    titles_list=[]
    if operation_status == OPER_GET_LIST_SUCCEEDED:
        for t in titles:
            titles_list.append(t.title)

    e_titles_list = ttk.Combobox(b_top, values=titles_list, width =47)
    e_titles_list.set('---Choose title from the list---')
    e_titles_list.grid(row=0, column=0, padx=10, pady=10, sticky='ew')

    add_in_e_titles_list = Button(b_top, text='Add title', command=add_title_to_book_text_list)
    add_in_e_titles_list.grid(row=0, column=1, padx=10, pady=10, sticky='ew')

    e_title = Entry(b_top, width=50)
    e_title.grid(row=1, column=0, sticky='ew')

    add_in_e_nt = Button(b_top, text='Add new title', command=add_new_title_to_db)
    add_in_e_nt.grid(row=1, column=1, padx=10, pady=10, sticky='ew')

    book_text_list = Listbox(b_top, width=60, height=15)
    book_text_list.grid(row=12, column=0, padx=10, pady=10, sticky='nsew')

    book_text_list_label = Label(b_top, text='Press button - Add book - to add book with the below parameters to database')
    book_text_list_label.grid(row=11, column=0, padx=10, pady=10, sticky='nsew')

    operation_status, authors_list = get_authors_list()
    authors_names = []
    if operation_status == OPER_GET_LIST_SUCCEEDED:
        for a in authors_list:
            authors_names.append(f'{a.author_name} {a.author_surname}')

    e_authors_list = ttk.Combobox(b_top, values=authors_names, width=47)
    e_authors_list.set('---Choose author from the list---')
    e_authors_list.grid(row=2, column=0, padx=10, pady=10, sticky='ew')

    add_in_e_authors_list = Button(b_top, text='Add author', command=add_author_to_book_text_list)
    add_in_e_authors_list.grid(row=2, column=1, padx=10, pady=10, sticky='ew')

    e_author = Entry(b_top, width=50)
    e_author.grid(row=3, column=0, sticky='ew')

    add_in_e_nt = Button(b_top, text='Add new author', command=lambda: add_new_author_to_db(new_author_name, new_author_surname))
    add_in_e_nt.grid(row=3, column=1, padx=10, pady=10, sticky='ew')

    operation_status, languages = get_languages_list()
    languages_list=[]
    if operation_status == OPER_GET_LIST_SUCCEEDED:
        for l in languages:
            languages_list.append(l.language)

    e_languages_list = ttk.Combobox(b_top, values=languages_list, width =47)
    e_languages_list.set('---Choose language from the list---')
    e_languages_list.grid(row=4, column=0, padx=10, pady=10, sticky='ew')

    add_in_e_languages_list = Button(b_top, text='Add language', command=add_language_to_book_text_list)
    add_in_e_languages_list.grid(row=4, column=1, padx=10, pady=10, sticky='ew')

    e_language = Entry(b_top, width=50)
    e_language.grid(row=5, column=0, sticky='ew')

    add_in_e_nt = Button(b_top, text='Add new language', command=add_new_language_to_db)
    add_in_e_nt.grid(row=5, column=1, padx=10, pady=10, sticky='ew')

    delete_in_e_languages_list = Button(b_top, text='Delete book', command=delete_book)
    delete_in_e_languages_list.grid(row=12, column=2, padx=10, pady=10, sticky='ew')

    operation_status, categories = get_categories_list()
    categories_list = []
    if operation_status == OPER_GET_LIST_SUCCEEDED:
        for c in categories:
            categories_list.append(c.category_name)

    e_categories_list = ttk.Combobox(b_top, values=categories_list, width=47)
    e_categories_list.set('---Choose category from the list---')
    e_categories_list.grid(row=6, column=0, padx=10, pady=10, sticky='ew')

    add_in_e_categories_list = Button(b_top, text='Add category', command=add_category_to_book_text_list)
    add_in_e_categories_list.grid(row=6, column=1, padx=10, pady=10, sticky='ew')

    e_category = Entry(b_top, width=50)
    e_category.grid(row=7, column=0, sticky='ew')

    add_in_e_nt = Button(b_top, text='Add new category', command=add_new_category_to_db)
    add_in_e_nt.grid(row=7, column=1, padx=10, pady=10, sticky='ew')


    operation_status, tags = get_tags_list()
    tags_list = []
    if operation_status == OPER_GET_LIST_SUCCEEDED:
        for t in tags:
            tags_list.append(t.tag)

    e_tags_list = ttk.Combobox(b_top, values=tags_list, width=47)
    e_tags_list.set('---Choose tag from the list---')
    e_tags_list.grid(row=9, column=0, padx=10, pady=10, sticky='ew')

    add_in_e_tags_list = Button(b_top, text='Add tag', command=add_tag_to_book_text_list)
    add_in_e_tags_list.grid(row=9, column=1, padx=10, pady=10, sticky='ew')

    e_tag = Entry(b_top, width=50)
    e_tag.grid(row=10, column=0, sticky='ew')

    add_in_e_nt = Button(b_top, text='Add new tag', command=add_new_tag_to_db)
    add_in_e_nt.grid(row=10, column=1, padx=10, pady=10, sticky='ew')

    add_book = Button(b_top, text='Add book', command=lambda:add_book)
    add_book.grid(row=12, column=1, padx=10, pady=10, sticky='ew')

    button_quit = Button(b_top, text='Close', command=b_top.destroy)
    button_quit.grid(row=13, column=2)


def message_window_empty_data():
    e_d_top = Toplevel()
    e_d_top.grab_set()
    top_label = Label(e_d_top, text='No data/wrong data format entered')
    top_label.grid(row=0, column=0, padx=10, pady=10)

    button_close = Button(e_d_top, text='Close', command=e_d_top.destroy)
    button_close.grid(row=1, column=0, padx=10, pady=10)

def message_window_data_exists():
    d_e_top = Toplevel()
    d_e_top.grab_set()
    top_label = Label(d_e_top, text='Data exists already in the database')
    top_label.grid(row=0, column=0, padx=10, pady=10)

    button_close = Button(d_e_top, text='Close', command=d_e_top.destroy)
    button_close.grid(row=1, column=0, padx=10, pady=10)

##############***********####################

def add_category_to_book_text_list():
    global choosen_category
    choosen_category = e_categories_list.get()
    if not choosen_category.strip():
        message_window_empty_data()
        return None
    else:
        if choosen_category and choosen_category != '---Choose category from the list---':
            book_text_list.insert(END, f"Category: {choosen_category}")
            e_category.delete(0, END)
            e_categories_list.set('---Choose category from the list---')
            logging.info('Category added to the list')
            category_add_successfull_window()
            return None
        else:
            logging.info('Category is already on the list')
            return None

def add_category_to_db():
    global c_text_list
    global e_categories_list

    text = e_categories_list.get()
    if not text.strip():
        message_window_empty_data()
        return None
    else:
        formatted_text = f'Category: {text}'
        if text not in c_text_list.get(0, END):
            book_text_list.insert(END, formatted_text)
            e_categories_list.delete(0, END)
            category_add_successfull_window()
            e_categories_list.set('---Choose category from the list---')

            logging.info('Category added to the book')
            return None
        else:
            logging.info('Category was already added to the book')
            return None

def add_new_category_to_db():
    global book_text_list
    global c_text_list
    global e_category
    global b_top

    new_category = e_category.get()
    print(f"print {new_category}")
    if not new_category in book_text_list.get(0, END):
        session.add(Category(category_name=new_category))
        session.commit()
        category_add_successfull_window()
        e_category.delete(0, END)
        logging.info('Category was added to the database')
        return None
    else:
        logging.info('Category is already in the database')
        return None

def category_add_successfull_window():
    c_win_top = Toplevel()
    c_win_top.grab_set()
    top_label = Label(c_win_top, text='Category addition successfull.')
    top_label.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')

    button_close = Button(c_win_top, text='Close', command=c_win_top.destroy)
    button_close.grid(row=1, column=0, padx=10, pady=10)


###################**********###################

def add_author_to_db():
    global e_authors_list
    text = e_authors_list.get()
    if not text.strip():
        message_window_empty_data()
        return None
    else:
        split_text = text.split()
        if len(split_text) < 2:
            message_window_empty_data()
            return None
        else:
            author_name = split_text[0]
            author_surname = split_text[1]
            if text not in e_authors_list.get(0, END):
                add_author(author_name, author_surname)
                e_authors_list.insert(END, text)
                e.delete(0, END)
                logging.info('Author added to the list')
                author_add_successfull_window()
                return None
            else:
                logging.info('Author is already on the list')
                return None

def add_author_to_book_text_list():
    global e_authors_list
    global choosen_author
    choosen_author = e_authors_list.get()
    if not choosen_author.strip():
        message_window_empty_data()
        return None
    else:
        split_text = choosen_author.split()
        if len(split_text) < 2:
            message_window_empty_data()
            return None
        else:
            if f'Author: {choosen_author}' and choosen_author!= '---Choose author from the list---':
                formatted_text=f'Author: {choosen_author}'
                book_text_list.insert(END, formatted_text)
                e_authors_list.delete(0, END)
                author_add_successfull_window()
                e_authors_list.set('---Choose author from the list---')
                logging.info('Author added to the book')
                return None
            else:
                logging.info('Author was already added')
                return None

def add_new_author_to_db(new_author_name, new_author_surname):
    global e_author
    global book_text_list

    new_author = e_author.get().strip()
    new_author_split = new_author.split()
    new_author_name = new_author_split[0]
    new_author_surname = new_author_split[1]
    author = session.query(Author).filter_by(
        author_name=new_author_name,
        author_surname=new_author_surname
    ).first()

    if not author:
        new_author = Author(author_name=new_author_name, author_surname=new_author_surname)

        formatted_author = f'Author: {new_author_name} {new_author_surname}'
        session.add(new_author)
        session.commit()
        author_add_successfull_window()
        e_author.delete(0, END)
        logging.info('New author added to the database')
        return None
    else:
        logging.info('Author is already in the database')
        return None

def author_add_successfull_window():
    a_win_top = Toplevel()
    a_win_top.grab_set()
    top_label = Label(a_win_top, text='Author addition successfull.')
    top_label.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')

    button_close = Button(a_win_top, text='Close', command=a_win_top.destroy)
    button_close.grid(row=1, column=0, padx=10, pady=10)

##############***********####################

def add_title_to_book_text_list():
    global choosen_title
    choosen_title = e_titles_list.get()
    if choosen_title and choosen_title != '---Choose title from the list---':
        book_text_list.insert(END, f"Title: {choosen_title}")
        e_titles_list.set('---Choose title from the list---')
        title_add_successfull_window()



def add_new_title_to_db():
    global t_text_list
    global b_top
    global e_title
    # e_title = Entry(b_top, width=50)

    new_title = e_title.get()
    print(f"print {new_title}")
    if not new_title in titles_list:
        # formatted_title = f'Title: {new_title}'
        # t_text_list.insert(END, formatted_title)
        # add_title(new_title)
        session.add(Title(title=new_title))
        session.commit()
        title_add_successfull_window()
        e_title.delete(0, END)
        logging.info('Title was added to the database')
        return None
    else:
        logging.info('Title is already in the database')
        return None

def add_title_to_db():
    global book_text_list
    global e_titles_list

    text = e_titles_list.get()
    if not text.strip():
        message_window_empty_data()
        return None
    else:
        formatted_text = f'Title: {text}'
        if formatted_text not in book_text_list.get(0, END):
            add_title(text)
            book_text_list.insert(END, formatted_text)
            e_titles_list.delete(0, END)
            title_add_successfull_window()
            e_titles_list.set('---Choose title from the list---')
            logging.info('Title added to the book')
            return None
        else:
            logging.info('Title was already added to the book')
            return None


def title_add_successfull_window():
    t_win_top = Toplevel()
    t_win_top.grab_set()
    top_label = Label(t_win_top, text='Title addition successfull.')
    top_label.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')

    button_close = Button(t_win_top, text='Close', command=t_win_top.destroy)
    button_close.grid(row=1, column=0, padx=10, pady=10)

#############********##################

def add_language_to_book_text_list():
    global choosen_language
    choosen_language = e_languages_list.get()
    if not choosen_language.strip():
        message_window_empty_data()
        return None
    else:
        if choosen_language and choosen_language != '---Choose language from the list---':
            book_text_list.insert(END, f"Language: {choosen_language}")
            e_language.delete(0, END)
            e_languages_list.set('---Choose language from the list---')
            language_add_successfull_window()
            logging.info('Language added to the list')
            return None
        else:
            logging.info('Language is already on the list')
            return None

def add_language_to_db():
    global book_text_list
    global e_languages_list

    text = e_languages_list.get()
    if not text.strip():
        message_window_empty_data()
        return None
    else:
        formatted_text = f'Language: {text}'
        if formatted_text not in book_text_list.get(0, END):
            book_text_list.insert(END, formatted_text)
            e_languages_list.delete(0, END)
            language_add_successfull_window()
            e_languages_list.set('---Choose language from the list---')
            logging.info('Language added to the book')
            return None
        else:
            logging.info('Language was already added to the book')
            return None

def add_new_language_to_db():
    global book_text_list
    global e_language

    new_language = e_language.get()
    print(f"print {new_language}")
    if not new_language in book_text_list.get(0, END):
        formatted_language = f'Language: {new_language}'
        session.add(Language(language=new_language))
        session.commit()
        language_add_successfull_window()
        e_language.delete(0, END)
        logging.info('Language was added to the database')
        return None
    else:
        logging.info('Language is already in the database')
        return None

def language_add_successfull_window():
    l_win_top = Toplevel()
    l_win_top.grab_set()
    top_label = Label(l_win_top, text='Language addition successfull.')
    top_label.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')

    button_close = Button(l_win_top, text='Close', command=l_win_top.destroy)
    button_close.grid(row=1, column=0, padx=10, pady=10)

############**********##################

def add_tag_to_book_text_list():
    global choosen_tag
    choosen_tag = e_tags_list.get()
    if not choosen_tag.strip():
        message_window_empty_data()
        return None
    else:
        if choosen_tag and choosen_tag != '---Choose tag from the list---':
            book_text_list.insert(END, f"Tag: {choosen_tag}")
            e_tag.delete(0, END)
            e_tags_list.set('---Choose tag from the list---')
            tag_add_successfull_window()
            logging.info('Tag added to the list')
            return None
        else:
            logging.info('Tag is already on the list')
            return None

def add_tag_to_book():
    global book_text_list
    global e_tags_list

    text = e_tags_list.get()
    if not text.strip():
        message_window_empty_data()
        return None
    else:
        formatted_text = f'Tag: {text}'
        if formatted_text not in book_text_list.get(0, END):
            book_text_list.insert(END, formatted_text)
            e_tags_list.delete(0, END)
            tag_add_successfull_window()
            e_tags_list.set('---Choose tag from the list---')
            logging.info('Tag added to the book')
            return None
        else:
            logging.info('Tag was already added to the book')
            return None

def add_new_tag_to_db():
    global book_text_list
    global e_tag
    global b_top

    new_tag = e_tag.get()
    if not new_tag in book_text_list.get(0, END):
        session.add(Tag(tag=new_tag))
        session.commit()
        category_add_successfull_window()
        e_tags_list.insert(0, new_tag)
        e_tag.delete(0, END)
        logging.info('Tag was added to the database')
        return None
    else:
        logging.info('Tag is already in the database')
        return None

def tag_add_successfull_window():
    ta_win_top = Toplevel()
    ta_win_top.grab_set()
    top_label = Label(ta_win_top, text='Tag addition successfull.')
    top_label.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')

    button_close = Button(ta_win_top, text='Close', command=ta_win_top.destroy)
    button_close.grid(row=1, column=0, padx=10, pady=10)

##################**********###################

def add_cover_page_to_list():
    text = e.get()
    if not text.strip():
        message_window_empty_data()
        return None
    else:
        if text not in cp_text_list.get(0, END):
            add_cover_page(text)
            cp_text_list.insert(END, text)
            e.delete(0, END)
            logging.info('Cover page added to the list')
            category_add_successfull_window()
            return None
        else:
            logging.info('Cover page is already on the list')
            return None

def cover_page__add_successfull_window():
    cp_win_top = Toplevel()
    cp_win_top.grab_set()
    top_label = Label(cp_win_top, text='Cover page addition successfull.')
    top_label.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')

    button_close = Button(cp_win_top, text='Close', command=cp_win_top.destroy)
    button_close.grid(row=1, column=0, padx=10, pady=10)

#################**********#################

def category_add_successfull_window():
    c_win_top = Toplevel()
    c_win_top.grab_set()
    top_label = Label(c_win_top, text='Category addition successfull.')
    top_label.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')

    button_close = Button(c_win_top, text='Close', command=c_win_top.destroy)
    button_close.grid(row=1, column=0, padx=10, pady=10)

#############*********#################

def selected_to_be_deleted():
    global selected_indicate
    selected_indicate= text_list.curselection()
    if selected_indicate:
        logging.info('Selected to be deleted')
        return selected_indicate[0]
    else:
        logging.info('Nothing to be deleted')
        return None

def delete_for_sure(callback_function):
    d_f_s_top = Toplevel()
    d_f_s_top.grab_set()
    top_label = Label(d_f_s_top, text='Are you sure you want to delete it?')
    top_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky='nsew')

    button_yes = Button(d_f_s_top, text='Yes', command= lambda: [callback_function(), d_f_s_top.destroy()])
    button_yes.grid(row=1, column=0, padx=10, pady=10)
    button_no = Button(d_f_s_top, text='No', command=d_f_s_top.destroy)
    button_no.grid(row=1, column=1, padx=10, pady=10)

############*********###############

def delete_selected_category():
    delete_for_sure(_delete_selected_category)
    return None

def _delete_selected_category():
    selected = text_list.curselection()
    if selected:
        delete_category(text_list.get(selected))
        text_list.delete(selected)
        category_delete_successfull_window()
        logging.info('Category deleted')
        return None
    else:
        logging.info('No record to be deleted')
        return None

def category_delete_successfull_window():
    c_d_win_top = Toplevel()
    c_d_win_top.grab_set()
    top_label = Label(c_d_win_top, text='Category delete successfull.')
    top_label.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')

    button_close = Button(c_d_win_top, text='Close', command=c_d_win_top.destroy)
    button_close.grid(row=1, column=0, padx=10, pady=10)

#############*********###############

def delete_selected_author():
    delete_for_sure(_delete_selected_author)
    return None

def _delete_selected_author():
    selected = a_text_list.curselection()
    if not selected:
        logging.info('No record to be deleted')
        return None
    else:
        selected = selected[0]
        selected_author =  a_text_list.get(selected)
        parts = selected_author.split()
        author_name = parts[0]
        author_surname = parts[1]
        delete_author(author_name, author_surname)
        author_delete_successfull_window()
        a_text_list.delete(selected)
        logging.info('Author deleted')
        return None

def author_delete_successfull_window():
    a_d_win_top = Toplevel()
    a_d_win_top.grab_set()
    top_label = Label(a_d_win_top, text='Author delete successfull.')
    top_label.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')

    button_close = Button(a_d_win_top, text='Close', command=a_d_win_top.destroy)
    button_close.grid(row=1, column=0, padx=10, pady=10)

###########******###############

def delete_selected_title():
    delete_for_sure(_delete_selected_title)
    return None

def _delete_selected_title():
    selected = t_text_list.curselection()
    if selected:
        delete_title(a_text_list.get(selected))
        a_text_list.delete(selected)
        title_delete_successfull_window()
        logging.info('Title deleted')
        return None
    else:
        logging.info('No record to be deleted')
        return None

def title_delete_successfull_window():
    t_d_win_top = Toplevel()
    t_d_win_top.grab_set()
    top_label = Label(t_d_win_top, text='Title delete successfull.')
    top_label.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')

    button_close = Button(t_d_win_top, text='Close', command=t_d_win_top.destroy)
    button_close.grid(row=1, column=0, padx=10, pady=10)

###########********##############

def delete_selected_language():
    delete_for_sure(_delete_selected_language)
    return None

def _delete_selected_language():
    selected = l_text_list.curselection()
    if selected:
        delete_language(l_text_list.get(selected))
        l_text_list.delete(selected)
        language_delete_successfull_window()
        logging.info('Language deleted')
        return None
    else:
        logging.info('No record to be deleted')
        return None

def language_delete_successfull_window():
    l_d_win_top = Toplevel()
    l_d_win_top.grab_set()
    top_label = Label(l_d_win_top, text='Language delete successfull.')
    top_label.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')

    button_close = Button(l_d_win_top, text='Close', command=l_d_win_top.destroy)
    button_close.grid(row=1, column=0, padx=10, pady=10)

##############********#############

def delete_selected_tag():
    delete_for_sure(_delete_selected_tag)
    return None

def _delete_selected_tag():
    selected = ta_text_list.curselection()
    if selected:
        delete_tag(ta_text_list.get(selected))
        ta_text_list.delete(selected)
        tag_delete_successfull_window()
        logging.info('Tag deleted')
        return None
    else:
        logging.info('No record to be deleted')
        return None

def tag_delete_successfull_window():
    t_d_win_top = Toplevel()
    t_d_win_top.grab_set()
    top_label = Label(t_d_win_top, text='Tag delete successfull.')
    top_label.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')

    button_close = Button(t_d_win_top, text='Close', command=t_d_win_top.destroy)
    button_close.grid(row=1, column=0, padx=10, pady=10)

############**********#############

def delete_selected_cover_page():
    delete_for_sure(_delete_selected_cover_page)
    return None

def _delete_selected_cover_page():
    selected = cp_text_list.curselection()
    if selected:
        delete_cover_page(cp_text_list.get(selected))
        cp_text_list.delete(selected)
        cover_page_delete_successfull_window()
        logging.info('Cover page deleted')
        return None
    else:
        logging.info('No record to be deleted')
        return None

def cover_page_delete_successfull_window():
    cp_d_win_top = Toplevel()
    cp_d_win_top.grab_set()
    top_label = Label(cp_d_win_top, text='Cover page delete successfull.')
    top_label.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')

    button_close = Button(cp_d_win_top, text='Close', command=cp_d_win_top.destroy)
    button_close.grid(row=1, column=0, padx=10, pady=10)

###########************###################

def delete_book():
    global ta_text_list
    selected = book_text_list.curselection()
    if selected:
        book_text_list.delete(selected)
        delete_successfull_window()

        selected_area = ta_text_list.curselection()
        if selected_area:
            ta_text_list.set('---Choose tag from the list---')
            logging.info('Tag deleted from the book')
        else:
            logging.info('No tag selected to be deleted')

        selected_area = t_text_list.curselection()
        if selected_area:
            t_text_list.set('---Choose title from the list---')
            logging.info('Title deleted from the book')
        else:
            logging.info('No title selected to be deleted')

        selected_area = a_text_list.curselection()
        if selected_area:
            a_text_list.set('---Choose author from the list---')
            logging.info('Author deleted from the book')
        else:
            logging.info('No author selected to be deleted')

        selected_area = l_text_list.curselection()
        if selected_area:
            l_text_list.set('---Choose language from the list---')
            logging.info('Language deleted from the book')
        else:
            logging.info('No language selected to be deleted')

        selected_area = c_text_list.curselection()
        if selected_area:
            c_text_list.set('---Choose category from the list---')
            logging.info('Category deleted from the book')
        else:
            logging.info('No category selected to be deleted')

def delete_book():
    selected = book_text_list.curselection()
    if not selected:
        logging.info('No book selected for deletion.')
        return

    selected_text = book_text_list.get(selected[0])
    logging.info(f"Attempting to delete book entry: {selected_text}")

    # Extract components from the list entries
    title = None
    author_name = None
    author_surname = None
    language = None
    category = None
    tag = None

    for i in range(book_text_list.size()):
        line = book_text_list.get(i)
        if line.startswith("Title: "):
            title = line.replace("Title: ", "").strip()
        elif line.startswith("Author: "):
            parts = line.replace("Author: ", "").strip().split()
            if len(parts) >= 2:
                author_name, author_surname = parts[0], parts[1]
        elif line.startswith("Language: "):
            language = line.replace("Language: ", "").strip()
        elif line.startswith("Category: "):
            category = line.replace("Category: ", "").strip()
        elif line.startswith("Tag: "):
            tag = line.replace("Tag: ", "").strip()

    if not all([title, author_name, author_surname, language, category, tag]):
        logging.warning("Book data incomplete. Aborting deletion.")
        message_window_empty_data()
        return

    # Look up corresponding database objects
    title_obj = session.query(Title).filter_by(title=title).first()
    author_obj = session.query(Author).filter_by(author_name=author_name, author_surname=author_surname).first()
    language_obj = session.query(Language).filter_by(language=language).first()
    category_obj = session.query(Category).filter_by(category_name=category).first()
    tag_obj = session.query(Tag).filter_by(tag=tag).first()

    if not all([title_obj, author_obj, language_obj, category_obj, tag_obj]):
        logging.warning("One or more related entities not found in DB.")
        message_window_empty_data()
        return

    # Find the book
    book = session.query(Book).filter_by(title_id=title_obj.id, language_id=language_obj.id).first()
    if book and author_obj in book.authors and category_obj in book.categories and tag_obj in book.tags:
        # Remove relations first
        book.authors.remove(author_obj)
        book.categories.remove(category_obj)
        book.tags.remove(tag_obj)
        session.delete(book)
        session.commit()

        # Update UI
        book_text_list.delete(0, END)
        delete_successfull_window()
        logging.info(f"Book '{title}' deleted successfully.")
    else:
        logging.info("Book not found or associations mismatched.")
        message_window_empty_data()


def delete_successfull_window():
    global b_top
    global l_t_win_t
    d_win_top = Toplevel()
    d_win_top.grab_set()
    top_label = Label(d_win_top, text='Delete successfull.')
    top_label.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')

    button_close = Button(d_win_top, text='Close', command=d_win_top.destroy)
    button_close.grid(row=1, column=0, padx=10, pady=10)

###########********##############

def update_category_window():
    global old_category_name
    global new_category_name
    global selected_category
    global selected_index
    global top

    top = Toplevel()
    top.grab_set()

    top.columnconfigure(0, weight=1)
    top.columnconfigure(1, weight=1)
    top.columnconfigure(2, weight=1)
    top.columnconfigure(3, weight=1)
    top.rowconfigure(0, weight=1)

    top.title('Update category')
    selected_category = text_list.curselection()
    selected_index = selected_category[0]

    old_category_name = Entry(top, width=50)
    old_category_name.grid(row=0, column=1, sticky='ew')
    if selected_category:
        selected_index = selected_category[0]
        selected_category_content = text_list.get(selected_index)
        old_category_name.insert(0, selected_category_content)
        return None

    new_category_name = Entry(top, width=50)
    new_category_name.grid(row=1, column=1, sticky='ew')

    old_category_label = Label(top, text='from')
    old_category_label.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')

    new_category_label = Label(top, text='to')
    new_category_label.grid(row=1, column=0, padx=10, pady=10, sticky='nsew')

    button_update = Button(top, text='Press to update', command=update_category_button_to_click)
    button_update.grid(row=2, column=1, padx=10, pady=10)

    button_close = Button(top, text='Close', command=top.destroy)
    button_close.grid(row=2, column=2, padx=10, pady=10)

def update_category_button_to_click():
    global top
    old_category_selected = c_text_list.curselection()

    if not old_category_selected:
        logging.info('No category selected for an update')
    else:
        selected_index = old_category_selected[0]
        old_category = c_text_list.get(selected_index)
        new_category = new_category_name.get()
        if new_category in c_text_list.get(0,END):
            logging.info('Category is already on the categories list ')
        else:
            operation_status, category_id = update_category(old_category, new_category)
            if operation_status == OPER_UPDATE_SUCCEEDED:
                c_text_list.delete(selected_index)
                c_text_list.insert(selected_index, new_category)
                top.destroy()
                category_update_successfull_window()
                logging.info('Category was updated')
            else:
                logging.info('Category update failed')
                return None

def category_update_successfull_window():
    c_u_win_top = Toplevel()
    c_u_win_top.grab_set()
    c_u_win_top.lift()
    c_u_win_top.after(10, lambda: c_u_win_top.attributes('-topmost', False))
    top_label = Label(c_u_win_top, text='Category update successfull.')
    top_label.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')

    button_close = Button(c_u_win_top, text='Close', command=c_u_win_top.destroy)
    button_close.grid(row=1, column=0, padx=10, pady=10)

############*********##############

def update_author_window():
    global top

    top = Toplevel()
    top.grab_set()

    top.columnconfigure(0, weight=1)
    top.columnconfigure(1, weight=1)
    top.columnconfigure(2, weight=1)
    top.columnconfigure(3, weight=1)
    top.rowconfigure(0, weight=1)

    top.title('Update author')
    selected_author = a_text_list.curselection()
    selected_index = selected_author[0]

    old_author = Entry(top, width=50)
    old_author.grid(row=0, column=1, sticky='ew')
    if selected_author:
        selected_index = selected_author[0]
        selected_author_content = a_text_list.get(selected_index)
        old_author.insert(0, selected_author_content)

    new_author = Entry(top, width=50)
    new_author.grid(row=1, column=1, sticky='ew')

    old_author_label = Label(top, text='from')
    old_author_label.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')

    new_author_label = Label(top, text='to')
    new_author_label.grid(row=1, column=0, padx=10, pady=10, sticky='nsew')

    button_update = Button(top, text='Press to update', command=lambda: update_author_button_to_click(new_author, selected_index))
    button_update.grid(row=2, column=1, padx=10, pady=10)

    button_close = Button(top, text='Close', command=top.destroy)
    button_close.grid(row=2, column=2, padx=10, pady=10)

def update_author_button_to_click(new_author, selected_index):
    old_author = a_text_list.get(selected_index)
    if not old_author:
        logging.info('No author selected for an update')
    else:
        parts = old_author.split()

        old_author_name = parts[0]
        old_author_surname = parts[1]
        new_author_value = new_author.get()
        new_author_value_split = new_author_value.split()
        new_author_name = new_author_value_split[0]
        new_author_surname = new_author_value_split[1]


        if new_author_value in a_text_list.get(0, END):
            logging.info('Author is already on the authors list ')
            message_window_data_exists()
            top.destroy()
            return None
        else:
            operation_status, author_id = update_author(old_author_name, new_author_name, old_author_surname,
                                                        new_author_surname)
            if operation_status == OPER_UPDATE_SUCCEEDED:
                a_text_list.delete(selected_index)
                a_text_list.insert(selected_index, f'{new_author_name} {new_author_surname}')
                logging.info(f'Author: {old_author_name} {old_author_surname} was updated to {new_author_name} {new_author_surname}')
                top.destroy()
                author_update_successfull_window()
                return None
            else:
                logging.info('Author update failed')
                return None

def author_update_successfull_window():
    win_top = Toplevel()
    top_label = Label(win_top, text='Author update successfull.')
    top_label.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')

    button_close = Button(win_top, text='Close', command=win_top.destroy)
    button_close.grid(row=1, column=0, padx=10, pady=10)

###############*******###############

def update_title_window():
    global top

    top = Toplevel()
    top.grab_set()

    top.columnconfigure(0, weight=1)
    top.columnconfigure(1, weight=1)
    top.columnconfigure(2, weight=1)
    top.columnconfigure(3, weight=1)
    top.rowconfigure(0, weight=1)

    top.title('Update title')
    selected_title = t_text_list.curselection()

    old_title = Entry(top, width=50)
    old_title.grid(row=0, column=1, sticky='ew')
    if selected_title:
        selected_index = selected_title[0]
        selected_title_content = t_text_list.get(selected_index)
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
    global top
    updated_title = new_title.get()
    if not updated_title:
        logging.info("No title indicated for an update")
    else:
        selected_title_text = t_text_list.get(selected_index)
        delete_title(selected_title_text)

        authors_list = t_text_list.get(0, END)
        if not updated_title in authors_list:
            add_title(updated_title)
            t_text_list.delete(selected_index)
            t_text_list.insert(selected_index, updated_title)
            top.destroy()
            title_update_successfull_window()
            logging.info('Title updated')
        else:
            logging.info('Title is already on authors list')
            message_window_data_exists()
            top.destroy()
            return None


def title_update_successfull_window():
    t_u_win_top = Toplevel()
    t_u_win_top.grab_set()
    t_u_win_top.lift()
    t_u_win_top.after(10, lambda: t_u_win_top.attributes('-topmost', False))
    top_label = Label(t_u_win_top, text='Title update successfull.')
    top_label.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')

    button_close = Button(t_u_win_top, text='Close', command=t_u_win_top.destroy)
    button_close.grid(row=1, column=0, padx=10, pady=10)

#############********#############

def update_language_window():
    global top

    top = Toplevel()
    top.grab_set()

    top.columnconfigure(0, weight=1)
    top.columnconfigure(1, weight=1)
    top.columnconfigure(2, weight=1)
    top.columnconfigure(3, weight=1)
    top.rowconfigure(0, weight=1)

    top.title('Update language')
    selected_language = l_text_list.curselection()

    old_language = Entry(top, width=50)
    old_language.grid(row=0, column=1, sticky='ew')
    if selected_language:
        selected_index = selected_language[0]
        selected_language_content = l_text_list.get(selected_index)
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

def update_language(new_language, selected_index):

    updated_language = new_language.get()
    if not updated_language:
        logging.info("No language indicated for an update")
        return None
    else:
        selected_language_text = l_text_list.get(selected_index)
        delete_language(selected_language_text)

        languages_list = l_text_list.get(0, END)
        if not updated_language in languages_list:
            add_language(updated_language)
            l_text_list.delete(selected_index)
            l_text_list.insert(selected_index, updated_language)
            top.destroy()
            language_update_successfull_window()
            logging.info('Language updated')
        else:
            logging.info('Language is already on authors list')
            message_window_data_exists()
            top.destroy()
            return None


def language_update_successfull_window():
    l_u_win_top = Toplevel()
    l_u_win_top.grab_set()
    l_u_win_top.lift()
    l_u_win_top.after(10, lambda: l_u_win_top.attributes('-topmost', False))
    top_label = Label(l_u_win_top, text='Language update successfull.')
    top_label.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')

    button_close = Button(l_u_win_top, text='Close', command=l_u_win_top.destroy)
    button_close.grid(row=1, column=0, padx=10, pady=10)

############**********#############

def update_tag_window():
    global top

    top = Toplevel()
    top.grab_set()

    top.columnconfigure(0, weight=1)
    top.columnconfigure(1, weight=1)
    top.columnconfigure(2, weight=1)
    top.columnconfigure(3, weight=1)
    top.rowconfigure(0, weight=1)

    top.title('Update tag')
    selected_tag = ta_text_list.curselection()

    old_tag = Entry(top, width=50)
    old_tag.grid(row=0, column=1, sticky='ew')
    if selected_tag:
        selected_index = selected_tag[0]
        selected_tag_content = ta_text_list.get(selected_index)
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
    global top
    updated_tag = new_tag.get()
    if not updated_tag:
        logging.info("No tag indicated for an update")
        return None
    else:
        selected_tag_text = ta_text_list.get(selected_index)
        delete_tag(selected_tag_text)

        tags_list = ta_text_list.get(0, END)
        if not updated_tag in tags_list:
            add_tag(updated_tag)

            ta_text_list.delete(selected_index)
            ta_text_list.insert(selected_index, updated_tag)
            top.destroy()
            tag_update_successfull_window()
            logging.info('Title updated')

        else:
            logging.info('Tag is already on authors list')
            message_window_data_exists()
            top.destroy()
            return None

def tag_update_successfull_window():
    t_u_win_top = Toplevel()
    t_u_win_top.grab_set()
    t_u_win_top.lift()
    t_u_win_top.after(10, lambda: t_u_win_top.attributes('-topmost', False))
    top_label = Label(t_u_win_top, text='Tag update successfull.')
    top_label.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')

    button_close = Button(t_u_win_top, text='Close', command=t_u_win_top.destroy)
    button_close.grid(row=1, column=0, padx=10, pady=10)

#############********#############

def update_cover_page_window():
    global top

    top = Toplevel()
    top.grab_set()

    top.columnconfigure(0, weight=1)
    top.columnconfigure(1, weight=1)
    top.columnconfigure(2, weight=1)
    top.columnconfigure(3, weight=1)
    top.rowconfigure(0, weight=1)

    top.title('Update cover page')
    selected_cover_page = text_list.curselection()

    old_cover_page = Entry(top, width=50)
    old_cover_page.grid(row=0, column=1, sticky='ew')
    if selected_cover_page:
        selected_index = selected_cover_page[0]
        selected_cover_page = text_list.get(selected_index)
        old_cover_page.insert(0, selected_cover_page)

    new_cover_page = Entry(top, width=50)
    new_cover_page.grid(row=1, column=1, sticky='ew')

    old_cover_page = Label(top, text='from')
    old_cover_page.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')

    new_cover_page_label = Label(top, text='to')
    new_cover_page_label.grid(row=1, column=0, padx=10, pady=10, sticky='nsew')

    button_update = Button(top, text='Press to update', command=lambda: update_language(new_cover_page, selected_index))
    button_update.grid(row=2, column=1, padx=10, pady=10)

    button_close = Button(top, text='Close', command=top.destroy)
    button_close.grid(row=2, column=2, padx=10, pady=10)

def update_cover_page(new_cover_page, selected_index):

    updated_cover_page = new_cover_page.get()
    if not updated_cover_page:
        logging.info("No cover page indicated for an update")
        return None
    else:
        selected_cover_page_text = cp_text_list.get(selected_index)
        delete_cover_page(selected_cover_page_text)

        cover_page_list = cp_text_list.get(0, END)
        if not updated_cover_page in cover_page_list:
            add_cover_page(updated_cover_page)
            cp_text_list.delete(selected_index)
            cp_text_list.insert(selected_index, updated_cover_page)
            top.destroy()
            cover_page_update_successfull_window()
            logging.info('Cover page updated')
        else:
            logging.info('Cover page is already on authors list')
            message_window_data_exists()
            top.destroy()
            return None


def cover_page_update_successfull_window():
    cp_u_win_top = Toplevel()
    cp_u_win_top.grab_set()
    cp_u_win_top.lift()
    cp_u_win_top.after(10, lambda: cp_u_win_top.attributes('-topmost', False))
    top_label = Label(cp_u_win_top, text='Cover page update successfull.')
    top_label.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')

    button_close = Button(cp_u_win_top, text='Close', command=cp_u_win_top.destroy)
    button_close.grid(row=1, column=0, padx=10, pady=10)

def add_book():

    new_book = Book()

    try:
        title_text = book_text_list.get()
        title_obj = session.query(Title).filter_by(title=title_text).first()
        if title_text.startswith("Title:"):
            existing_book = session.query(Book).filter_by(title_id=title_obj.id).first()
            if existing_book:
                message_window_empty_data()
                return

            new_book = Book(title=title_obj)

        language_text = e_languages_list.get()
        language_obj = session.query(Language).filter_by(language=language_text).first()
        if language_text.startswith("Language:"):
            new_book.languages.append(language_obj)

        author_text = e_authors_list.get()
        author_parts = author_text.strip().split()
        if len(author_parts) < 2:
            messagebox.showerror("Error: Enter author name and surname")
            return

        author_name = author_parts[0]
        author_surname = " ".join(author_parts[1:])
        author_obj = session.query(Author).filter_by(author_name=author_name, author_surname=author_surname).first()
        if author_text.startswith("Author:"):
            new_book.authors.append(author_obj)

        category_text = e_categories_list.get()
        category_obj = session.query(Category).filter_by(category_name=category_text).first()
        if category_text.startswith("Category:"):
            new_book.categories.append(category_obj)

        tag_text = e_tags_list.get()
        tag_obj = session.query(Tag).filter_by(tag=tag_text).first()
        if tag_text.startswith("Tag:"):
            new_book.tags.append(tag_obj)

    except OperationalError as e:
        message_window_empty_data()
        return

    session.add(new_book)
    session.commit()



myButton1 = Button(root, text='Categories operations', fg='blue', command=cat_oper_window)
myButton1.grid(row=0, column=0, padx=10, pady=10, sticky='ew')

myButton2 = Button(root, text='Authors operations', fg='red', command=aut_oper_window)
myButton2.grid(row=1, column=0, padx=10, pady=10, sticky='ew')

myButton3 = Button(root, text='Titles operations', fg='brown', command= tit_oper_window)
myButton3.grid(row=2, column=0, padx=10, pady=10, sticky='ew')

myButton4 = Button(root, text='Languages operations', fg='green', command= lang_oper_window)
myButton4.grid(row=3, column=0, padx=10, pady=10, sticky='ew')

myButton5 = Button(root, text='Tags operations', fg='purple', command= tag_oper_window)
myButton5.grid(row=4, column=0, padx=10, pady=10, sticky='ew')

myButton5 = Button(root, text='Cover pages operations', fg='black', command= cover_page_oper_window)
myButton5.grid(row=5, column=0, padx=10, pady=10, sticky='ew')

myButton6 = Button(root, text='Books operations', fg='black', highlightbackground='orange', command= books_oper_window, width=20, height=3)
myButton6.grid(row=1, column=1, padx=10, pady=10, sticky='ew')

digit_clock_label = Label(root, font=('Calibri', 20), fg='orange', bg='grey')
digit_clock_label.grid(row=2, column=1, padx=10, pady=10, sticky='nsew')

logo_label = Label(root)
logo_label.grid(row=3, column=1, padx=10, pady=10, sticky='nsew')

button_quit = Button(root, text='Close', command=root.quit)
button_quit.grid(row=5, column=3)

# digital clock display

def digit_clock():

    current_time = time.strftime("%H:%M")
    digit_clock_label.config(text=current_time)
    root.after(1000, digit_clock)

digit_clock()

def show_logo(logo):
    global logo_img
    image = Image.open(io.BytesIO(logo))
    image = image.resize((100, 120))
    logo_img = ImageTk.PhotoImage(image)
    logo_label.config(image=logo_img)

with open("../images/logo.png", 'rb') as f:
    logo=f.read()
show_logo(logo)



root.mainloop()
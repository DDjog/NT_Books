
from tkinter import *
from PIL import Image, ImageTk
import logging
import time
import io
from tkinter import ttk
from tkinter import filedialog


from src.database.db import session
from src.database.models import Author, Category, Tag, Title, Language, Book, Isbn, Cover_page, Publisher, \
    ShelfSignature

from src.constans import *
from src.operations.category_operations import add_category, get_categories_list, delete_category, update_category
from src.operations.author_operations import add_author, delete_author, get_authors_list, update_author
from src.operations.isbn_operations import get_isbn_list, add_isbn, delete_isbn, update_isbn
from src.operations.title_operations import add_title, delete_title, get_titles_list
from src.operations.language_operations import add_language, get_languages_list, delete_language
from src.operations.tag_operations import add_tag, get_tags_list, delete_tag
from src.operations.cover_page_operations import add_cover_page, delete_cover_page, get_cover_page, get_cover_page_list
from src.operations.publisher_operations import add_publisher, delete_publisher, get_publishers_list, update_publisher
from src.operations.shelf_signature_operations import add_shelf_signature, delete_shelf_signature, update_shelf_signature, get_shelf_signatures_list


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

e_categories_list = None

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
    global e_author
    global a_text_list

    a_top=Toplevel()
    a_top.grab_set()
    a_top.title('Authors operations')

    a_top.columnconfigure(0, weight=1)
    a_top.columnconfigure(1, weight=1)
    a_top.columnconfigure(2, weight=1)
    a_top.columnconfigure(3, weight=1)
    a_top.rowconfigure(0, weight=1)

    e_author=Entry(a_top, width=50)
    e_author.grid(row=0, column=0, sticky='ew')

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
    delete_in_e.grid(row=0, column=2, padx=10, pady=10, sticky='ew')

    t_text_list = Listbox(t_top, width=60, height=15)
    t_text_list.grid(row=2, column=0, padx=10, pady=10, sticky='nsew')

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
    global e_language

    l_top=Toplevel()
    l_top.grab_set()

    l_top.title('Languages operations')

    l_top.columnconfigure(0, weight=1)
    l_top.columnconfigure(1, weight=1)
    l_top.columnconfigure(2, weight=1)
    l_top.columnconfigure(3, weight=1)
    l_top.rowconfigure(0, weight=1)

    e_language=Entry(l_top, width=50)
    e_language.grid(row=0, column=0, sticky='ew')

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
    global e_tag

    ta_top=Toplevel()
    ta_top.grab_set()

    ta_top.title('Tags operations')

    ta_top.columnconfigure(0, weight=1)
    ta_top.columnconfigure(1, weight=1)
    ta_top.columnconfigure(2, weight=1)
    ta_top.columnconfigure(3, weight=1)
    ta_top.rowconfigure(0, weight=1)

    e_tag=Entry(ta_top, width=50)
    e_tag.grid(row=0, column=0, sticky='ew')

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

def isbn_oper_window():
    global i_text_list
    global e_isbn

    top=Toplevel()
    top.grab_set()
    top.title('Isbn operations')

    top.columnconfigure(0, weight=1)
    top.columnconfigure(1, weight=1)
    top.columnconfigure(2, weight=1)
    top.columnconfigure(3, weight=1)
    top.rowconfigure(0, weight=1)
    top.rowconfigure(1, weight=1)
    top.rowconfigure(2, weight=1)

    e_isbn=Entry(top, width=50)
    e_isbn.grid(row=0, column=0, sticky='ew')

    add_in_e_isbn=Button(top, text='Add isbn', command=add_isbn_to_db)
    add_in_e_isbn.grid(row=0, column=1, padx=10, pady=10, sticky='ew')

    delete_in_e_isbn = Button(top, text='Delete isbn', command=delete_selected_isbn)
    delete_in_e_isbn.grid(row=0, column=2, padx=10, pady=10, sticky='ew')

    i_text_list = Listbox(top, width=60, height=15)
    i_text_list.grid(row=2, column=0, padx=10, pady=10, sticky='nsew')

    operation_status, isbns =get_isbn_list()
    if operation_status == OPER_GET_LIST_SUCCEEDED:
        for i in isbns:
            i_text_list.insert(END, i.isbn_name)


    i_text_list_label = Label(top, text='List of isbns:')
    i_text_list_label.grid(row=1, column=0, padx=10, pady=10, sticky='nsew')

    button_update = Button(top, text='Update isbn', command=update_isbn_window)
    button_update.grid(row=1, column=1, padx=10, pady=10, sticky='nsew')

    button_quit = Button(top, text='Close', command=top.destroy)
    button_quit.grid(row=3, column=2)

def cover_page_oper_window():
    global cp_text_list
    global e_cover_page
    global cp_top
    global cover_page_images
    global cover_image_label

    cp_top=Toplevel()
    cp_top.grab_set()

    cp_top.title('Cover page operations')

    cp_top.columnconfigure(0, weight=1)
    cp_top.columnconfigure(1, weight=1)
    cp_top.columnconfigure(2, weight=1)
    cp_top.columnconfigure(3, weight=1)
    cp_top.rowconfigure(0, weight=1)
    cp_top.rowconfigure(1, weight=1)
    cp_top.rowconfigure(2, weight=1)
    cp_top.rowconfigure(3, weight=1)

    e_cover_page=Entry(cp_top, width=50)
    e_cover_page.grid(row=0, column=0, sticky='ew')

    add_in_e=Button(cp_top, text='Add cover page', command=add_cover_page_to_list)
    add_in_e.grid(row=0, column=1, padx=10, pady=10, sticky='ew')

    delete_in_e = Button(cp_top, text='Delete cover page', command=delete_selected_cover_page)
    delete_in_e.grid(row=0, column=2, padx=10, pady=10, sticky='ew')

    cp_text_list = Listbox(cp_top, width=60, height=15)
    cp_text_list.grid(row=2, column=0, padx=10, pady=10, sticky='nsew')

    button_update = Button(cp_top, text='Update cover page', command=update_cover_page_window)
    button_update.grid(row=1, column=1, padx=10, pady=10, sticky='nsew')

    button_select_file = Button(cp_top, text='Select file', command=lambda:select_file_from_disc(e_cover_page))
    button_select_file.grid(row=1, column=2, padx=10, pady=10, sticky='nsew')

    cover_page_images = {}
    operation_status, cover_pages = get_cover_page_list()
    if operation_status == OPER_GET_LIST_SUCCEEDED:
        for cp in cover_pages:
            cp_text_list.insert(END, cp.id)

    cp_text_list_label = Label(cp_top, text='List of cover pages:')
    cp_text_list_label.grid(row=1, column=0, padx=10, pady=10, sticky='nsew')

    cover_image_label = Label(cp_top, text='Image')
    cover_image_label.grid(row=2, column=1, padx=10, pady=10, sticky='nsew')

    button_quit = Button(cp_top, text='Close', command=cp_top.destroy)
    button_quit.grid(row=3, column=2)

def publisher_oper_window():
    global p_text_list
    global e_publisher

    top=Toplevel()
    top.grab_set()
    top.title('Publisher operations')

    top.columnconfigure(0, weight=1)
    top.columnconfigure(1, weight=1)
    top.columnconfigure(2, weight=1)
    top.columnconfigure(3, weight=1)
    top.rowconfigure(0, weight=1)
    top.rowconfigure(1, weight=1)
    top.rowconfigure(2, weight=1)

    e_publisher=Entry(top, width=50)
    e_publisher.grid(row=0, column=0, sticky='ew')

    add_in_e_publisher=Button(top, text='Add publisher', command=add_publisher_to_db)
    add_in_e_publisher.grid(row=0, column=1, padx=10, pady=10, sticky='ew')

    delete_in_e_publisher = Button(top, text='Delete publisher', command=delete_selected_publisher)
    delete_in_e_publisher.grid(row=0, column=2, padx=10, pady=10, sticky='ew')

    p_text_list = Listbox(top, width=60, height=15)
    p_text_list.grid(row=2, column=0, padx=10, pady=10, sticky='nsew')

    operation_status, publishers =get_publishers_list()
    if operation_status == OPER_GET_LIST_SUCCEEDED:
        for i in publishers:
            p_text_list.insert(END, i.publisher)


    p_text_list_label = Label(top, text='List of publishers:')
    p_text_list_label.grid(row=1, column=0, padx=10, pady=10, sticky='nsew')

    button_update = Button(top, text='Update publisher', command=update_publisher_window)
    button_update.grid(row=1, column=1, padx=10, pady=10, sticky='nsew')

    button_quit = Button(top, text='Close', command=top.destroy)
    button_quit.grid(row=3, column=2)

def shelf_signature_oper_window():
    global ss_text_list
    global e_ss

    top=Toplevel()
    top.grab_set()
    top.title('Shelf signature operations')

    top.columnconfigure(0, weight=1)
    top.columnconfigure(1, weight=1)
    top.columnconfigure(2, weight=1)
    top.columnconfigure(3, weight=1)
    top.rowconfigure(0, weight=1)
    top.rowconfigure(1, weight=1)
    top.rowconfigure(2, weight=1)

    e_ss=Entry(top, width=50)
    e_ss.grid(row=0, column=0, sticky='ew')

    add_in_e_ss=Button(top, text='Add self signature', command=add_ss_to_db)
    add_in_e_ss.grid(row=0, column=1, padx=10, pady=10, sticky='ew')

    delete_in_e_ss = Button(top, text='Delete shelf signature', command=delete_selected_ss)
    delete_in_e_ss.grid(row=0, column=2, padx=10, pady=10, sticky='ew')

    ss_text_list = Listbox(top, width=60, height=15)
    ss_text_list.grid(row=2, column=0, padx=10, pady=10, sticky='nsew')

    operation_status, shelf_signatures =get_shelf_signatures_list()
    if operation_status == OPER_GET_LIST_SUCCEEDED:
        for i in shelf_signatures:
            ss_text_list.insert(END, i.shelf_signature)


    ss_text_list_label = Label(top, text='List of shelf signatures:')
    ss_text_list_label.grid(row=1, column=0, padx=10, pady=10, sticky='nsew')

    button_update = Button(top, text='Update shelf signature', command=update_shelf_signature_window)
    button_update.grid(row=1, column=1, padx=10, pady=10, sticky='nsew')

    button_quit = Button(top, text='Close', command=top.destroy)
    button_quit.grid(row=3, column=2)

def books_oper_window():
    global book_text_list
    global e_titles_list
    global e_authors_list
    global e_languages_list
    global e_categories_list
    global e_tags_list
    global e_isbns_list
    global e_publishers_list
    global e_ss_list
    global e_author
    global b_top
    global e_category
    global e_title
    global e_language
    global e_tag
    global e_isbn
    global e_publisher
    global e_ss



    b_top = Toplevel()
    b_top.grab_set()

    b_top.title('Books operations')

    b_top.columnconfigure(0, weight=1)
    b_top.columnconfigure(1, weight=1)
    b_top.columnconfigure(2, weight=1)
    b_top.columnconfigure(3, weight=1)
    b_top.rowconfigure(0, weight=1)
    b_top.rowconfigure(1, weight=1)
    b_top.rowconfigure(2, weight=1)
    b_top.rowconfigure(3, weight=1)
    b_top.rowconfigure(4, weight=1)
    b_top.rowconfigure(5, weight=1)
    b_top.rowconfigure(6, weight=1)
    b_top.rowconfigure(7, weight=1)
    b_top.rowconfigure(8, weight=1)
    b_top.rowconfigure(9, weight=1)
    b_top.rowconfigure(10, weight=1)
    b_top.rowconfigure(11, weight=1)
    b_top.rowconfigure(12, weight=1)
    b_top.rowconfigure(13, weight=1)
    b_top.rowconfigure(14, weight=1)
    b_top.rowconfigure(15, weight=1)
    b_top.rowconfigure(16, weight=1)
    b_top.rowconfigure(17, weight=1)
    b_top.rowconfigure(18, weight=1)
    b_top.rowconfigure(19, weight=1)
    b_top.rowconfigure(20, weight=1)
    b_top.rowconfigure(21, weight=1)
    b_top.rowconfigure(22, weight=1)








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

    book_text_list = Listbox(b_top, width=60, height=10)
    book_text_list.grid(row=18, column=0, padx=10, pady=10, sticky='nsew')

    book_text_list_label = Label(b_top, text='Press button - Add book - to add book with the below parameters to database')
    book_text_list_label.grid(row=17, column=0, padx=10, pady=10, sticky='nsew')

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

    add_in_e_nt = Button(b_top, text='Add new author', command= add_new_author_to_db)
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
    delete_in_e_languages_list.grid(row=18, column=2, padx=10, pady=10, sticky='ew')

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

    operation_status, isbns = get_isbn_list()
    isbns_list = []
    if operation_status == OPER_GET_LIST_SUCCEEDED:
        for i in isbns:
            isbns_list.append(i.isbn_name)

    e_isbns_list = ttk.Combobox(b_top, values=isbns_list, width=47)
    e_isbns_list.set('---Choose isbn from the list---')
    e_isbns_list.grid(row=11, column=0, padx=10, pady=10, sticky='ew')

    add_in_e_isbn_list = Button(b_top, text='Add isbn', command=add_isbn_to_book_text_list)
    add_in_e_isbn_list.grid(row=11, column=1, padx=10, pady=10, sticky='ew')

    e_isbn = Entry(b_top, width=50)
    e_isbn.grid(row=12, column=0, sticky='ew')

    add_in_e_ni = Button(b_top, text='Add new isbn', command=add_new_isbn_to_db)
    add_in_e_ni.grid(row=12, column=1, padx=10, pady=10, sticky='ew')

    operation_status, publishers = get_publishers_list()
    publishers_list = []
    if operation_status == OPER_GET_LIST_SUCCEEDED:
        for i in publishers:
            publishers_list.append(i.publisher)

    e_publishers_list = ttk.Combobox(b_top, values=publishers_list, width=47)
    e_publishers_list.set('---Choose publisher from the list---')
    e_publishers_list.grid(row=13, column=0, padx=10, pady=10, sticky='ew')

    add_in_e_publishers_list = Button(b_top, text='Add publisher', command=add_publisher_to_book_text_list)
    add_in_e_publishers_list.grid(row=13, column=1, padx=10, pady=10, sticky='ew')

    e_publisher = Entry(b_top, width=50)
    e_publisher.grid(row=14, column=0, sticky='ew')

    add_in_e_np = Button(b_top, text='Add new publisher', command=add_new_publisher_to_db)
    add_in_e_np.grid(row=14, column=1, padx=10, pady=10, sticky='ew')

    operation_status, shelf_signatures = get_shelf_signatures_list()
    shelf_signatures_list = []
    if operation_status == OPER_GET_LIST_SUCCEEDED:
        for i in shelf_signatures:
            shelf_signatures_list.append(i.shelf_signature)

    e_ss_list = ttk.Combobox(b_top, values=shelf_signatures_list, width=47)
    e_ss_list.set('---Choose shelf signature from the list---')
    e_ss_list.grid(row=15, column=0, padx=10, pady=10, sticky='ew')

    add_in_e_ss_list = Button(b_top, text='Add shelf signature', command=add_ss_to_book_text_list)
    add_in_e_ss_list.grid(row=15, column=1, padx=10, pady=10, sticky='ew')

    e_ss = Entry(b_top, width=50)
    e_ss.grid(row=16, column=0, sticky='ew')

    add_in_e_nss = Button(b_top, text='Add new shelf signature', command=add_new_ss_to_db)
    add_in_e_nss.grid(row=16, column=1, padx=10, pady=10, sticky='ew')

    add_book = Button(b_top, text='Add book', command=add_book_to_db)
    add_book.grid(row=18, column=1, padx=10, pady=10, sticky='ew')

    button_quit = Button(b_top, text='Close', command=b_top.destroy)
    button_quit.grid(row=19, column=2)

    print(type(book_text_list))


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
    global e_categories_list

    choosen_category = e_categories_list.get()
    if not choosen_category and choosen_category == '---Choose category from the list---':
        return

    for index, line in enumerate(book_text_list.get(0, END)):
        if line.startswith('Category'):
            book_text_list.delete(index)

    book_text_list.insert(0, f"Category: {choosen_category}")
    e_categories_list.set('---Choose category from the list---')


def add_category_to_db():
    global c_text_list
    global e_categories_list

    text = e_category.get()
    if not text.strip():
        message_window_empty_data()
        return None
    else:
        if text not in c_text_list.get(0, END):
            add_category(text)
            c_text_list.insert(END, text)
            # category_add_successfull_window()
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
    if not new_category in book_text_list.get(0, END):
        session.add(Category(category_name=new_category))
        session.commit()
        # category_add_successfull_window()
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
    global a_text_list
    text = e_author.get()
    if not text:
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
            if text not in a_text_list.get(0, END):
                add_author(author_name, author_surname)
                a_text_list.insert(END, text)
                e_author.delete(0, END)
                logging.info('Author added to the list')
                # author_add_successfull_window()
                return None
            else:
                logging.info('Author is already on the list')
                return None

def add_author_to_book_text_list():
    global e_authors_list
    global choosen_author

    choosen_author = e_authors_list.get()
    if not choosen_author and choosen_author == '---Choose author from the list---':
        return
    else:
        split_text = choosen_author.split()
        if len(split_text) < 2:
            message_window_empty_data()
            return None
        else:
            for index, line in enumerate(book_text_list.get(0, END)):
                if line.startswith('Author'):
                    book_text_list.delete(index)

            book_text_list.insert(0, f"Author: {choosen_author}")
            e_authors_list.set('---Choose author from the list---')
            # author_add_successfull_window()

def add_new_author_to_db():
    global e_author
    global book_text_list

    new_author = e_author.get().strip()
    new_author_split = new_author.split()
    new_author_name = new_author_split[0]
    new_author_surname = new_author_split[1]
    existing_author = session.query(Author).filter(
        Author.author_name==new_author_name,
        Author.author_surname==new_author_surname
    ).first()

    if not existing_author:

        session.add(Author(author_name=new_author_name, author_surname=new_author_surname))
        session.commit()
        tmp_list = list(e_authors_list['values'])
        tmp_list.append(new_author)
        e_authors_list['values'] = tmp_list
        # author_add_successfull_window()
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
    if not choosen_title and choosen_title == '---Choose title from the list---':
        return

    for index, line in enumerate (book_text_list.get(0, END)):
        if line.startswith('Title'):
                book_text_list.delete(index)

    book_text_list.insert(0, f"Title: {choosen_title}")
    e_titles_list.set('---Choose title from the list---')
    # title_add_successfull_window()

def add_new_title_to_db():
    global e_titles_list
    global b_top
    global e_title
    # e_title = Entry(b_top, width=50)

    new_title = e_title.get()
    existing_title = session.query(Title).filter_by(title=new_title).first()
    if not existing_title:
        session.add(Title(title=new_title))
        session.commit()
        # title_add_successfull_window()
        tmp_list =  list(e_titles_list['values'])
        tmp_list.append(new_title)
        e_titles_list['values']=tmp_list
        e_title.delete(0, END)
        logging.info('Title was added to the database')
        return None
    else:
        logging.info('Title is already in the database')
        return None

def add_title_to_db():
    global book_text_list
    global e_titles_list

    text = e_title.get()
    if not text.strip():
        message_window_empty_data()
    else:
        if text not in t_text_list.get(0, END):
            add_title(text)
            t_text_list.insert(END, text)
            e_title.delete(0, END)
            # title_add_successfull_window()
            logging.info('Title added to the book')
            return
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
    global e_languages_list

    choosen_language = e_languages_list.get()
    if not choosen_language and choosen_language == '---Choose language from the list---':
        return

    for index, line in enumerate(book_text_list.get(0, END)):
        if line.startswith('Language'):
            book_text_list.delete(index)

    book_text_list.insert(0, f"Language: {choosen_language}")
    e_languages_list.set('---Choose language from the list---')
    # language_add_successfull_window()


def add_language_to_db():
    global book_text_list
    global e_languages_list

    text = e_language.get()
    if not text.strip():
        message_window_empty_data()
        return
    else:
        if text not in l_text_list.get(0, END):
            add_language(text)
            l_text_list.insert(END, text)
            e_language.delete(0, END)
            # language_add_successfull_window()
            logging.info('Language added to the book')
            return
        else:
            logging.info('Language was already added to the book')
            return None

def add_new_language_to_db():
    global book_text_list
    global e_language

    new_language = e_language.get()
    existing_language = session.query(Language).filter_by(language=new_language).first()
    if not existing_language:
        session.add(Language(language=new_language))
        session.commit()
        tmp_list = list(e_languages_list['values'])
        tmp_list.append(new_language)
        e_languages_list['values'] = tmp_list
        # language_add_successfull_window()
        e_language.delete(0, END)
        logging.info('Language was added to the database')
        return None
    else:
        logging.info('Language is already in the database')
        return OPER_ADD_FAILED_DATA_EXISTS

def language_add_successfull_window():
    l_win_top = Toplevel()
    l_win_top.grab_set()
    top_label = Label(l_win_top, text='Language addition successfull.')
    top_label.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')

    button_close = Button(l_win_top, text='Close', command=l_win_top.destroy)
    button_close.grid(row=1, column=0, padx=10, pady=10)

############**********##################

def add_tag_to_book_text_list():
    global choosen_category
    global e_categories_list

    choosen_tag = e_tags_list.get()
    if not choosen_tag and choosen_tag == '---Choose tag from the list---':
        return

    for index, line in enumerate(book_text_list.get(0, END)):
        if line.startswith('Tag'):
            book_text_list.delete(index)

    book_text_list.insert(0, f"Tag: {choosen_tag}")
    e_tags_list.set('---Choose tag from the list---')
    # tag_add_successfull_window()


def add_tag_to_db():

    text = e_tag.get()
    if not text.strip():
        message_window_empty_data()
        return
    else:
        if text not in ta_text_list.get(0, END):
            add_tag(text)
            ta_text_list.insert(END, text)
            e_tag.delete(0, END)
            # tag_add_successfull_window()
            logging.info('Tag added to db')
            return
        else:
            logging.info('Tag was already added to db')
            return None

def add_new_tag_to_db():
    global book_text_list
    global e_tag
    global b_top

    new_tag = e_tag.get()
    existing_tag = session.query(Tag).filter(Tag.tag == new_tag).first()
    if not existing_tag:
        session.add(Tag(tag=new_tag))
        session.commit()
        tmp_list = list(e_tags_list['values'])
        tmp_list.append(new_tag)
        e_tags_list['values'] = tmp_list
        # category_add_successfull_window()
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

def add_isbn_to_book_text_list():
    global choosen_isbn
    global e_isbns_list

    choosen_isbn = e_isbns_list.get()
    if not choosen_isbn and choosen_isbn == '---Choose isbn from the list---':
        return

    for index, line in enumerate(book_text_list.get(0, END)):
        if line.startswith('Isbn'):
            book_text_list.delete(index)

    book_text_list.insert(0, f"Isbn: {choosen_isbn}")
    e_isbns_list.set('---Choose isbn from the list---')
    # isbn_add_successfull_window()


def add_isbn_to_db():

    text = e_isbn.get()
    if not text.strip():
        message_window_empty_data()
        return None
    else:
        if text not in i_text_list.get(0, END):
            add_isbn(text)
            i_text_list.insert(END, text)
            e_isbn.delete(0, END)
            # isbn_add_successfull_window()
            logging.info('Isbn added to the list')
            return None
        else:
            logging.info('Isbn is already on the list')
            return None

def add_new_isbn_to_db():
    global book_text_list
    global e_isbn

    new_isbn = e_isbn.get()
    existing_isbn = session.query(Isbn).filter(Isbn.isbn_name == new_isbn).first()
    if not existing_isbn:
        session.add(Isbn(isbn_name=new_isbn))
        session.commit()
        tmp_list = list(e_isbns_list['values'])
        tmp_list.append(new_isbn)
        e_isbns_list['values'] = tmp_list
        # isbn_add_successfull_window()
        e_isbn.delete(0, END)
        logging.info('Isbn was added to the db')
        return None
    else:
        logging.info('Isbn is already in the db')
        return None

def isbn_add_successfull_window():
    i_win_top = Toplevel()
    i_win_top.grab_set()
    top_label = Label(i_win_top, text='Isbn addition successfull.')
    top_label.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')

    button_close = Button(i_win_top, text='Close', command=i_win_top.destroy)
    button_close.grid(row=1, column=0, padx=10, pady=10)
###############**********####################

def add_cover_page_to_list():
    text = e_cover_page.get()
    if not text.strip():
        message_window_empty_data()
        return None
    else:
        if text not in cp_text_list.get(0, END):
            r=add_cover_page(text)
            if r[0] == OPER_ADD_SUCCEEDED:
                cp_text_list.insert(END, r[1] )
                e_cover_page.delete(0, END)
                logging.info('Cover page added to the list')
                # cover_page_add_successfull_window()
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

def add_publisher_to_book_text_list():
    global choosen_publisher
    global e_publishers_list

    choosen_publisher = e_publishers_list.get()
    if not choosen_publisher and choosen_publisher == '---Choose publisher from the list---':
        return

    for index, line in enumerate(book_text_list.get(0, END)):
        if line.startswith('Publisher'):
            book_text_list.delete(index)

    book_text_list.insert(0, f"Publisher: {choosen_publisher}")
    e_publishers_list.set('---Choose publisher from the list---')



def add_publisher_to_db():

    text = e_publisher.get()
    text_split = text.split(',')
    publisher = text_split[0]
    publication_year = text_split[1]
    address_id = text_split[2]

    if not text.strip():
        message_window_empty_data()
        return None
    else:
        if text not in p_text_list.get(0, END):
            add_publisher(publisher, publication_year, address_id)
            p_text_list.insert(END, f"{publisher}, {publication_year}, {address_id}")
            e_publisher.delete(0, END)
            logging.info('Publisher added to the list')
            return None
        else:
            logging.info('Publisher is already on the list')
            return None

def add_new_publisher_to_db():
    global book_text_list
    global e_publisher

    new_publisher = e_publisher.get()
    existing_publisher = session.query(Publisher).filter(Publisher.publisher == new_publisher).first()
    if not existing_publisher:
        session.add(Publisher(publisher=new_publisher))
        session.commit()
        tmp_list = list(e_publishers_list['values'])
        tmp_list.append(new_publisher)
        e_publishers_list['values'] = tmp_list
        e_publisher.delete(0, END)
        logging.info('Publisher was added to the db')
        return None
    else:
        logging.info('Publisher is already in the db')
        return None

##################**********###################

def add_ss_to_book_text_list():
    global choosen_ss
    global e_ss_list

    choosen_ss = e_ss_list.get()
    if not choosen_ss and choosen_ss == '---Choose shelf signature from the list---':
        return

    for index, line in enumerate(book_text_list.get(0, END)):
        if line.startswith('Shelf signature'):
            book_text_list.delete(index)

    book_text_list.insert(0, f"Shelf signature: {choosen_ss}")
    e_ss_list.set('---Choose shelf signature from the list---')

def add_ss_to_db():

    text = e_ss.get()
    if not text.strip():
        message_window_empty_data()
        return None
    else:
        if text not in ss_text_list.get(0, END):
            add_shelf_signature(text)
            ss_text_list.insert(END, text)
            e_ss.delete(0, END)
            logging.info('Shelf signature added to the list')
            return None
        else:
            logging.info('Shelf signature is already on the list')
            return None

def add_new_ss_to_db():
    global book_text_list
    global e_ss

    new_ss = e_ss.get()
    existing_ss = session.query(ShelfSignature).filter(ShelfSignature.shelf_signature == new_ss).first()
    if not existing_ss:
        session.add(ShelfSignature(shelf_signature=new_ss))
        session.commit()
        tmp_list = list(e_ss_list['values'])
        tmp_list.append(new_ss)
        e_ss_list['values'] = tmp_list
        e_ss.delete(0, END)
        logging.info('Shelf signature was added to the db')
        return None
    else:
        logging.info('Shelf signature is already in the db')
        return None


#############*********#################

def selected_to_be_deleted():
    global selected_indicate
    selected_indicate= book_text_list.curselection()
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
    selected = c_text_list.curselection()
    if selected:
        delete_category(c_text_list.get(selected))
        c_text_list.delete(selected)
        # category_delete_successfull_window()
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
        # author_delete_successfull_window()
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
        delete_title(t_text_list.get(selected))
        t_text_list.delete(selected)
        # title_delete_successfull_window()
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
        # language_delete_successfull_window()
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
        # tag_delete_successfull_window()
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

def delete_selected_isbn():
    delete_for_sure(_delete_selected_isbn)
    return None


def _delete_selected_isbn():
    selected = i_text_list.curselection()
    if selected:
        delete_isbn(i_text_list.get(selected))
        i_text_list.delete(selected)
        # isbn_delete_successfull_window()
        logging.info('Isbn deleted')
        return None
    else:
        logging.info('No record to be deleted')
        return None


def isbn_delete_successfull_window():
    i_d_win_top = Toplevel()
    i_d_win_top.grab_set()
    top_label = Label(i_d_win_top, text='Isbn delete successfull.')
    top_label.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')

    button_close = Button(i_d_win_top, text='Close', command=i_d_win_top.destroy)
    button_close.grid(row=1, column=0, padx=10, pady=10)

##############**********##############

def delete_selected_cover_page():
    delete_for_sure(_delete_selected_cover_page)
    return None

def _delete_selected_cover_page():
    selected = cp_text_list.curselection()
    if selected:
        delete_cover_page(cp_text_list.get(selected))
        cp_text_list.delete(selected)
        # cover_page_delete_successfull_window()
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

def delete_selected_publisher():
    delete_for_sure(_delete_selected_publisher)
    return None

def _delete_selected_publisher():
    selected = p_text_list.curselection()
    if not selected:
        logging.info('No record to be deleted')
        return None

    selected_publisher = p_text_list.get(selected[0])
    parts = [p.strip() for p in selected_publisher.split(',') if p.strip()]

    publisher = parts[0] if parts else None
    publication_year_local = parts[1] if len(parts) > 1 else None
    address_id_local = parts[2] if len(parts) > 2 else None

    if not publisher:
        message_window_empty_data()
        return None

    if publication_year_local is None or address_id_local is None:
        row = session.query(Publisher).filter_by(publisher=publisher).first()
        if not row:
            logging.info('Publisher not found in db')
            message_window_empty_data()
            return None
        if publication_year_local is None:
            publication_year_local = getattr(row, 'publication_year', None)
        if address_id_local is None:
            address_id_local = getattr(row, 'address_id', None)

    delete_publisher(publisher, publication_year_local)

    p_text_list.delete(selected[0])
    logging.info('Publisher deleted')
    return None


def publisher_delete_successfull_window():
    p_d_win_top = Toplevel()
    p_d_win_top.grab_set()
    top_label = Label(p_d_win_top, text='Publisher delete successfull.')
    top_label.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')

    button_close = Button(p_d_win_top, text='Close', command=p_d_win_top.destroy)
    button_close.grid(row=1, column=0, padx=10, pady=10)

###########************###################

def delete_book():

    selected_title = selected_isbn = selected_language = None

    for i in range(book_text_list.size()):
        line = book_text_list.get(i)
        if line.startswith("Title: "):
            selected_title = line.replace("Title: ", "").strip()
        elif line.startswith("Isbn: "):
            selected_isbn = line.replace("Isbn: ", "").strip()
        elif line.startswith("Language: "):
            selected_language = line.replace("Language: ", "").strip()

    if not all([selected_title, selected_isbn, selected_language]):
        logging.warning("Book data incomplete")
        return

    title_obj = session.query(Title).filter_by(title=selected_title).first()
    isbn_obj = session.query(Isbn).filter_by(isbn_name=selected_isbn).first()
    language_obj = session.query(Language).filter_by(language=selected_language).first()

    existing_book = session.query(Book).filter_by(title=title_obj, isbn=isbn_obj, language = language_obj).first()

    if not existing_book:
        logging.info("Book not found in database")
        message_window_empty_data()
        return

    session.delete(existing_book)
    session.commit()

    book_text_list.delete(0, END)
    # delete_successfull_window()
    logging.info(f"Book '{title_obj}' deleted successfully")

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
    global e_category

    top = Toplevel()
    top.grab_set()

    top.columnconfigure(0, weight=1)
    top.columnconfigure(1, weight=1)
    top.columnconfigure(2, weight=1)
    top.columnconfigure(3, weight=1)
    top.rowconfigure(0, weight=1)

    top.title('Update category')
    selected_category = c_text_list.curselection()
    selected_index = selected_category[0]

    old_category_name = Entry(top, width=50)
    old_category_name.grid(row=0, column=1, sticky='ew')

    new_category_name = Entry(top, width=50)
    new_category_name.grid(row=1, column=1, sticky='ew')

    c_entry_content = e_category.get()

    if selected_category:
        selected_index = selected_category[0]
        selected_category_content = c_text_list.get(selected_index)
        old_category_name.insert(0, selected_category_content)
        new_category_name.insert(0, c_entry_content)



    old_category_label = Label(top, text='from')
    old_category_label.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')

    new_category_label = Label(top, text='to')
    new_category_label.grid(row=1, column=0, padx=10, pady=10, sticky='nsew')

    button_update = Button(top, text='Press to update', command=lambda:update_category_button_to_click(new_category_name, selected_index))
    button_update.grid(row=2, column=1, padx=10, pady=10)

    button_close = Button(top, text='Close', command=top.destroy)
    button_close.grid(row=2, column=2, padx=10, pady=10)

def update_category_button_to_click(new_category_name, selected_index):
    updated_category = new_category_name.get()
    if not updated_category:
        logging.info("No category update indicated")
        return None
    else:
        selected_category_text = c_text_list.get(selected_index)
        delete_category(selected_category_text)

        categories_list = c_text_list.get(0, END)
        if not updated_category in categories_list:
            add_category(updated_category)
            c_text_list.delete(selected_index)
            c_text_list.insert(selected_index, updated_category)
            top.destroy()
            # category_update_successfull_window()
            logging.info('Category updated')
        else:
            logging.info('Category is already on category list')
            message_window_data_exists()
            top.destroy()
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
    global e_author

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

    new_author = Entry(top, width=50)
    new_author.grid(row=1, column=1, sticky='ew')

    if selected_author:
        selected_index = selected_author[0]
        selected_author_content = a_text_list.get(selected_index)
        old_author.insert(0, selected_author_content)
        a_entry_content = e_author.get()
        new_author.insert(0, a_entry_content)


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
                # author_update_successfull_window()
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
    global e_title

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

    new_title = Entry(top, width=50)
    new_title.grid(row=1, column=1, sticky='ew')

    if selected_title:
        selected_index = selected_title[0]
        selected_title_content = t_text_list.get(selected_index)
        old_title.insert(0, selected_title_content)
        t_entry_content = e_title.get()
        new_title.insert(0, t_entry_content)



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

        titles_list = t_text_list.get(0, END)
        if not updated_title in titles_list:
            add_title(updated_title)
            t_text_list.delete(selected_index)
            t_text_list.insert(selected_index, updated_title)
            top.destroy()
            # title_update_successfull_window()
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
    global e_language

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

    new_language = Entry(top, width=50)
    new_language.grid(row=1, column=1, sticky='ew')

    if selected_language:
        selected_index = selected_language[0]
        selected_language_content = l_text_list.get(selected_index)
        old_language.insert(0, selected_language_content)
        l_entry_content = e_language.get()
        new_language.insert(0,l_entry_content)



    old_language_label = Label(top, text='from')
    old_language_label.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')

    new_language_label = Label(top, text='to')
    new_language_label.grid(row=1, column=0, padx=10, pady=10, sticky='nsew')

    button_update = Button(top, text='Press to update', command=lambda: update_language_to_click(new_language, selected_index))
    button_update.grid(row=2, column=1, padx=10, pady=10)

    button_close = Button(top, text='Close', command=top.destroy)
    button_close.grid(row=2, column=2, padx=10, pady=10)

def update_language_to_click(new_language, selected_index):

    updated_language = new_language.get()
    print('ok')
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
            # language_update_successfull_window()
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
    global e_tag

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

    new_tag = Entry(top, width=50)
    new_tag.grid(row=1, column=1, sticky='ew')

    if selected_tag:
        selected_index = selected_tag[0]
        selected_tag_content = ta_text_list.get(selected_index)
        old_tag.insert(0, selected_tag_content)
        ta_entry_content = e_tag.get()
        new_tag.insert(0, ta_entry_content)


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
            # tag_update_successfull_window()
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

def update_isbn_window():
    global old_isbn_name
    global new_isbn_name
    global selected_isbn
    global selected_index
    global top
    global e_isbn

    top = Toplevel()
    top.grab_set()

    top.columnconfigure(0, weight=1)
    top.columnconfigure(1, weight=1)
    top.columnconfigure(2, weight=1)
    top.columnconfigure(3, weight=1)
    top.rowconfigure(0, weight=1)
    top.rowconfigure(1, weight=1)
    top.rowconfigure(2, weight=1)

    top.title('Update isbn')
    selected_isbn = i_text_list.curselection()


    old_isbn_name = Entry(top, width=50)
    old_isbn_name.grid(row=0, column=1, sticky='ew')

    new_isbn_name = Entry(top, width=50)
    new_isbn_name.grid(row=1, column=1, sticky='ew')

    if selected_isbn:
        selected_index = selected_isbn[0]
        selected_isbn_content = i_text_list.get(selected_index)
        old_isbn_name.insert(0, selected_isbn_content)
        i_entry_content = e_isbn.get()
        new_isbn_name.insert(0, i_entry_content)



    old_isbn_label = Label(top, text='from')
    old_isbn_label.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')

    new_isbn_label = Label(top, text='to')
    new_isbn_label.grid(row=1, column=0, padx=10, pady=10, sticky='nsew')

    button_update = Button(top, text='Press to update', command=lambda: update_isbn_button_to_click(new_isbn_name, selected_index))
    button_update.grid(row=2, column=1, padx=10, pady=10)

    button_close = Button(top, text='Close', command=top.destroy)
    button_close.grid(row=2, column=2, padx=10, pady=10)


def update_isbn_button_to_click(new_isbn, selected_index):
    updated_isbn = new_isbn.get()
    if not updated_isbn:
        logging.info("No isbn indicated for an update")
        return None
    else:
        selected_isbn_text = i_text_list.get(selected_index)
        delete_isbn(selected_isbn_text)

        isbn_list = i_text_list.get(0, END)
        if not updated_isbn in isbn_list:

            add_isbn(updated_isbn)
            i_text_list.delete(selected_index)
            i_text_list.insert(selected_index, updated_isbn)
            top.destroy()
            # isbn_update_successfull_window()
            logging.info('Isbn updated')
        else:
            logging.info('Isbn is already in db')
            message_window_data_exists()
            top.destroy()
            return None


def isbn_update_successfull_window():
    i_u_win_top = Toplevel()
    i_u_win_top.grab_set()
    i_u_win_top.lift()
    i_u_win_top.after(10, lambda: i_u_win_top.attributes('-topmost', False))
    top_label = Label(i_u_win_top, text='Isbn update successfull.')
    top_label.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')

    button_close = Button(i_u_win_top, text='Close', command=i_u_win_top.destroy)
    button_close.grid(row=1, column=0, padx=10, pady=10)


###############********############

def update_cover_page_window():
    global top
    global cp_text_list

    top = Toplevel()
    top.grab_set()

    top.columnconfigure(0, weight=1)
    top.columnconfigure(1, weight=1)
    top.columnconfigure(2, weight=1)
    top.columnconfigure(3, weight=1)
    top.rowconfigure(0, weight=1)

    top.title('Update cover page')
    selected_cover_page = cp_text_list.curselection()

    old_cover_page = Entry(top, width=50)
    old_cover_page.grid(row=0, column=1, sticky='ew')
    if selected_cover_page:
        selected_index = selected_cover_page[0]
        selected_cover_page = cp_text_list.get(selected_index)
        old_cover_page.insert(0, selected_cover_page)

    new_cover_page = Entry(top, width=50)
    new_cover_page.grid(row=1, column=1, sticky='ew')

    old_cover_page = Label(top, text='from')
    old_cover_page.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')

    new_cover_page_label = Label(top, text='to')
    new_cover_page_label.grid(row=1, column=0, padx=10, pady=10, sticky='nsew')

    button_update = Button(top, text='Press to update', command=lambda: update_cover_page(new_cover_page, selected_index))
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
            # cover_page_update_successfull_window()
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

###############*******###############

def update_publisher_window():
    global top
    global e_publisher

    top = Toplevel()
    top.grab_set()

    top.columnconfigure(0, weight=1)
    top.columnconfigure(1, weight=1)
    top.columnconfigure(2, weight=1)
    top.columnconfigure(3, weight=1)
    top.rowconfigure(0, weight=1)

    top.title('Update publisher')
    selected_publisher = p_text_list.curselection()
    selected_index = selected_publisher[0]

    old_publisher = Entry(top, width=50)
    old_publisher.grid(row=0, column=1, sticky='ew')

    new_publisher = Entry(top, width=50)
    new_publisher.grid(row=1, column=1, sticky='ew')

    if selected_publisher:
        selected_index = selected_publisher[0]
        selected_publisher_content = p_text_list.get(selected_index)
        old_publisher.insert(0, selected_publisher_content)
        p_entry_content = e_publisher.get()
        new_publisher.insert(0, p_entry_content)
    if not selected_publisher:
        message_window_empty_data()
        top.destroy()
        return


    old_publisher_label = Label(top, text='from')
    old_publisher_label.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')

    new_publisher_label = Label(top, text='to')
    new_publisher_label.grid(row=1, column=0, padx=10, pady=10, sticky='nsew')

    button_update = Button(top, text='Press to update', command=lambda: update_publisher_button_to_click(new_publisher, selected_index))
    button_update.grid(row=2, column=1, padx=10, pady=10)

    button_close = Button(top, text='Close', command=top.destroy)
    button_close.grid(row=2, column=2, padx=10, pady=10)

def update_publisher_button_to_click(new_publisher, selected_index):
    old_publisher = p_text_list.get(selected_index).strip()
    old_publication_year = None
    old_address_id = None

    if not old_publisher:
        logging.info('No publisher selected for an update')
        return None

    parts = list(filter(None, map(str.strip, old_publisher.split(','))))
    if len(parts) >= 3:
        old_publisher = parts[0]
        old_publication_year = parts[1]
        old_address_id = parts[2]
    else:
        publisher_in_db = session.query(Publisher).filter_by(publisher=old_publisher).first()
        if not publisher_in_db:
            logging.info('Publisher not found in db')
            return None

        old_publication_year = getattr(publisher_in_db, 'publication_year', None)
        old_address_id = getattr(publisher_in_db, 'address_id', None)

    new_publisher_value = new_publisher.get().strip()
    new_publisher_value_split = list(filter(None, map(str.strip, new_publisher_value.split(','))))
    if len(new_publisher_value_split) < 3:
        logging.info('Wrong format for new publisher. Use "name, year, address_id"')
        message_window_empty_data()
        return None

    new_publisher = new_publisher_value_split[0]
    new_publication_year = new_publisher_value_split[1]
    new_address_id = new_publisher_value_split[2]

    if new_publisher in [s.split(',')[0].strip() for s in p_text_list.get(0, END)]:
        logging.info('Publisher is already on the publishers list ')
        message_window_data_exists()
        top.destroy()
        return None

    operation_status, publisher_id = update_publisher(
        old_publisher, new_publisher, old_publication_year, new_publication_year, old_address_id, new_address_id
    )
    if operation_status == OPER_UPDATE_SUCCEEDED:
        p_text_list.delete(selected_index)
        p_text_list.insert(selected_index, f'{new_publisher}, {new_publication_year}, {new_address_id}')
        logging.info(
            f'Publisher: {old_publisher}, publication year: {old_publication_year}, '
            f'publisher address: {old_address_id} was updated to {new_publisher} {new_publication_year}, {new_address_id}'
        )
        top.destroy()
        return None
    else:
        logging.info('Publisher update failed')
        return None

def publisher_update_successfull_window():
    win_top = Toplevel()
    top_label = Label(win_top, text='Publisher update successfull.')
    top_label.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')

    button_close = Button(win_top, text='Close', command=win_top.destroy)
    button_close.grid(row=1, column=0, padx=10, pady=10)

###############*******###############

def select_file_from_disc(event_object):
    filepath = filedialog.askopenfilename(initialdir=".",
                                      title="File with cover",
                                      filetypes=(("PNG files", ".png"),
                                                 ("JPEG files", ".jpeg;.jpg"),
                                                 ("All Files", ".*")))
    if filepath == "":
        event_object.delete(0, END)
    else:
        event_object.delete(0, END)
        event_object.insert(0, str(filepath))

def    add_book_to_db():

    new_book = Book()

    title = author_name = author_surname = language = category = tag = isbn = publisher = shelf_signature = None

    book_list = book_text_list.get(0, END)
    for line in book_text_list.get(0, END):
        # print("line:", line)

        if line.startswith("Category: "):
            category = line.replace("Category: ", "").strip()
            continue

        if line.startswith("Tag: "):
            tag = line.replace("Tag: ", "").strip()
            continue

        if line.startswith("Isbn: "):
            isbn = line.replace("Isbn: ", "").strip()
            continue

        if line.startswith("Title: "):
            title = line.replace("Title: ", "").strip()
            continue
        if line.startswith("Author: "):
            parts = line.replace("Author: ", "").strip().split()
            if len(parts) >= 2:
                author_name = parts[0]
                author_surname = " ".join(parts[1:])
            continue
        if line.startswith("Language: "):
            language = line.replace("Language: ", "").strip()
            continue

        if line.startswith("Publisher: "):
            publisher = line.replace("Publisher: ", "").strip()
            continue

        if line.startswith("Shelf signature: "):
            shelf_signature = line.replace("Shelf signature: ", "").strip()
            continue

    print('tile = ', title )
    print('author_name = ', author_name )
    print('author_surname = ', author_surname )
    print('language = ', language )
    print('category = ', category )
    print('tag = ', tag )
    print('isbn = ', isbn )
    print('publisher = ', publisher)
    print('shef_signature = ', shelf_signature)

    if not all([title, author_name, author_surname, language, category, tag, isbn, publisher, shelf_signature]):
        logging.warning("Some book data are missing")
        message_window_empty_data()
        return None

    title_obj = session.query(Title).filter_by(title=title).first()
    author_obj = session.query(Author).filter_by(author_name=author_name, author_surname=author_surname).first()
    language_obj = session.query(Language).filter_by(language=language).first()
    category_obj = session.query(Category).filter_by(category_name=category).first()
    tag_obj = session.query(Tag).filter_by(tag=tag).first()
    isbn_obj = session.query(Isbn).filter_by(isbn_name=isbn).first()
    publisher_obj = session.query(Publisher).filter_by(publisher=publisher).first()
    shelf_signature_obj = session.query(ShelfSignature).filter_by(shelf_signature=shelf_signature).first()


    existing_book = session.query(Book).filter_by(
        title_id=title_obj.id,
        isbn_id=isbn_obj.id
    ).first()
    if existing_book:
        logging.info("Book with this title, author and isbn exists already in db")
        message_window_data_exists()
        return existing_book.id

    new_book.title_id = title_obj.id
    new_book.language_id = language_obj.id
    new_book.authors.append(author_obj)
    new_book.categories.append(category_obj)
    new_book.tags.append(tag_obj)
    new_book.isbn = isbn_obj
    new_book.publisher = publisher_obj
    if shelf_signature_obj == None:
        shelf_signature_obj = '0001'
    new_book.shelf_signature = shelf_signature_obj


    session.add(new_book)
    session.commit()

    logging.info(f"Book '{title}' was added to db")


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

myButton6 = Button(root, text='Isbns operations', fg='grey', command= isbn_oper_window)
myButton6.grid(row=5, column=0, padx=10, pady=10, sticky='ew')

myButton7 = Button(root, text='Cover pages operations', fg='black', command= cover_page_oper_window)
myButton7.grid(row=6, column=0, padx=10, pady=10, sticky='ew')

myButton8 = Button(root, text='Publishers operations', fg='olive', command= publisher_oper_window)
myButton8.grid(row=7, column=0, padx=10, pady=10, sticky='ew')

myButton9 = Button(root, text='Shelf signature operations', fg='lightsalmon', command= publisher_oper_window)
myButton9.grid(row=8, column=0, padx=10, pady=10, sticky='ew')

myButton10 = Button(root, text='Books operations', fg='black', highlightbackground='orange', command= books_oper_window, width=20, height=3)
myButton10.grid(row=1, column=1, padx=10, pady=10, sticky='ew')

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




def show_cover_image(event):
    global cp_text_list

    selection = cp_text_list.curselection()
    if selection:
        selected_id = cp_text_list.get(selection[0])
        cover_data = session.query(Cover_page).filter(Cover_page.id == selected_id).scalar()
        if cover_data:
            try:
                image = Image.open(io.BytesIO(cover_data))
                image = image.resize((150, 200))
                photo = ImageTk.PhotoImage(image)
                cover_image_label.config(image=photo, text='')
                cover_image_label.image = photo
            except Exception:
                cover_image_label.config(image='', text='Error loading image')
        else:
            cover_image_label.config(image='', text='No cover found')


    cp_text_list.bind("<<ListboxSelect>>", show_cover_image)

root.mainloop()
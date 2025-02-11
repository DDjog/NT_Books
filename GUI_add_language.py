from tkinter import *
from src.operations.language_operations import is_language_in_db, add_language

root = Tk()
root.title('Add language')

root.rowconfigure(0, weight=10)
root.rowconfigure(1, weight=10)
root.rowconfigure(2, weight=10)
root.columnconfigure(0, weight=10)

e = Entry(root, width=25)
e.grid(row=1, column=0, sticky='ew', padx=10, pady=10)

e_label = Label(root, text='Enter language')
e_label.grid(row=0, column=0, sticky='ew', padx=10, pady=10)

def add_to_db():
    new_language = e.get().strip()
    if new_language:
        if is_language_in_db(new_language) == False:
            add_language(new_language)
            e.delete(0, END)


add_button = Button(root, text='Add to the database', command=add_to_db)
add_button.grid(row=2, column=0, sticky='ew', padx=10, pady=10)


root.mainloop()

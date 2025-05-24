from tkinter import *
from tkinter import ttk
import logging
import psycopg2
from sqlalchemy import Table

conn = psycopg2.connect(
    host = 'localhost',
    port = 5432,
    database = 'Books',
    user = 'postgres',
    password = 'secret'
)

cursor = conn.cursor()

cursor.execute('''
SELECT 
    b.id, 
    a.author_name, 
    a.author_surname, 
    t.title, 
    p.publisher,
    i.isbn_name,
    l.language,
    STRING_AGG(tags.tag, ', ') as tags
FROM books b
LEFT JOIN book_m2m_author ba ON b.id=ba.book_id
LEFT JOIN authors a ON ba.author_id = a.id
LEFT JOIN titles t ON b.title_id = t.id
LEFT JOIN publishers p ON b.publisher_id = p.id
LEFT JOIN isbn i ON b.isbn_id = i.id
LEFT JOIN languages l ON b.language_id = l.id
LEFT JOIN book_m2m_tag bt ON b.id = bt.book_id
LEFT JOIN tags ON bt.tag_id = tags.id
GROUP BY 
    b.id,
    a.author_name, 
    a.author_surname, 
    t.title, 
    p.publisher, 
    i.isbn_name, 
    l.language
''')
rows = cursor.fetchall()

root = Tk()
root.title('Books library')
root.geometry('500x250')

main_frame = Frame(root)
main_frame.pack(fill='both', expand=True)

table = ttk.Treeview(main_frame, columns=('id', 'author_name', 'author_surname', 'title', 'publisher'), show='headings')

table.heading('id', text='ID', anchor='center')
table.heading('author_name', text="Author's name", anchor='center')
table.heading('author_surname', text="Author's surname", anchor='center')
table.heading('title', text='Title', anchor='center')
table.heading('publisher', text='Publisher', anchor='center')

table.column('id', width=50, anchor='center')
table.column('author_name', width=80, anchor='center')
table.column('author_surname', width=80, anchor='center')
table.column('title', width=120, anchor='center')
table.column('publisher', width=100, anchor='center')

for row in rows:
    table.insert('', 'end', values=row)

table.pack(side='left', fill='both', expand=True)

details_on_right = Text(main_frame, width=40, wrap="word")
details_on_right.pack(side='right', fill='both', expand=False, padx=10, pady=10)

def clicked_on_row(event):
    selected_item = table.focus()
    if not selected_item:
        return
    selected_values = table.item(selected_item)['values']
    book_id = selected_values[0]

    for row in rows:
        if row[0] == book_id:
            details_text = (
                f"Publisher: {row[4]}\n"
                f"ISBN: {row[5]}\n"
                f"Language: {row[6]}\n"
                f"Tags: {row[7]}\n"
            )
            details_on_right.delete(1.0, END)
            details_on_right.insert(END, details_text)
            break

table.bind('<ButtonRelease-1>', clicked_on_row)

def main():
    None

root.mainloop()
conn.close()

if __name__ == "__main__":
    main()

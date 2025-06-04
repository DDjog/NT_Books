import io
from tkinter import *
from PIL import Image, ImageTk
import psycopg2

conn = psycopg2.connect(
    host='localhost',
    port=5432,
    database='Books',
    user='postgres',
    password='secret'
)

cursor = conn.cursor()

cursor.execute('''
SELECT 
    b.id,
    c.cover_page
FROM books b
LEFT JOIN cover_pages c ON b.id = c.book_id
ORDER BY b.id
''')

rows = cursor.fetchall()

root = Tk()
root.title('Cover pages gallery')
root.geometry('600x400')


main_frame = Frame(root)
main_frame.pack(fill='both', expand=True, padx=10, pady=10)


left_frame = Frame(main_frame)
left_frame.pack(side='left', fill='y')


right_frame = Frame(main_frame)
right_frame.pack(side='left', fill='both', expand=True)

image_label = Label(right_frame)
image_label.pack(padx=10, pady=10)


image_refs = {}

def show_cover(event, image_data):
    if image_data:
            image = Image.open(io.BytesIO(image_data))
            image = image.resize((200, 250))
            photo = ImageTk.PhotoImage(image)
            image_refs['current'] = photo
            image_label.config(image=photo)
    else:
        image_label.config(image='')


for book_id, image_data in rows:
    label = Label(left_frame, text=f'Book ID: {book_id}', anchor='w', width=20)
    label.pack(pady=2, padx=5, anchor='w')
    label.bind("<Enter>", lambda e, data=image_data: show_cover(e, data))

root.mainloop()
conn.close()

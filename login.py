from customtkinter import CTk, CTkLabel, CTkEntry, CTkButton, CTkImage
from PIL import Image
from tkinter import messagebox
import db_manager

def login():
    if usernameEntry.get() == '' or passwordEntry.get() == '':
        messagebox.showerror('Error', 'All fields are required')
    elif usernameEntry.get() == 'admin' and passwordEntry.get() == '@admin123':
        messagebox.showinfo('Success', 'Login is successful')
        root.destroy()
        import main
    else:
        messagebox.showerror('Error', 'Wrong credentials')

# Initialize database connection and create table
db_manager.connect_db()
db_manager.create_table()

root = CTk()
root.geometry('930x478')
root.resizable(0, 0)
root.title('Login Page')

# Load image using Pillow and convert it to CTkImage
try:
    image = CTkImage(Image.open('./images/cover.jpg'), size=(930, 478))
    imageLabel = CTkLabel(root, image=image, text='')
    imageLabel.place(x=0, y=0)
except Exception as e:
    print(f"Error loading image: {e}")

headinglabel = CTkLabel(
    root,
    text='Employee Management System',
    bg_color='#FAFAFA',
    font=('Goudy Old Style', 20, 'bold'),
    text_color='dark blue'
)
headinglabel.place(x=20, y=100)

usernameEntry = CTkEntry(
    root,
    placeholder_text='Enter Your Username',
    width=180
)
usernameEntry.place(x=50, y=150)

passwordEntry = CTkEntry(
    root,
    placeholder_text='Enter Your Password',
    width=180,
    show='*'
)
passwordEntry.place(x=50, y=200)

loginButton = CTkButton(
    root,
    text='Login',
    cursor='hand2',
    command=login
)
loginButton.place(x=70, y=250)

root.mainloop()

db_manager.close_connection()

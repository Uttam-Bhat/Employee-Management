import mysql.connector
from tkinter import messagebox

# Global variables
mycursor = None
conn = None

def connect_db():
    global mycursor, conn
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='employee'
        )
        mycursor = conn.cursor()
    except mysql.connector.Error as err:
        messagebox.showerror('Error', f'Something went wrong: {err}\nPlease ensure MySQL is running and the connection details are correct.')
        exit()

def create_table():
    try:
        mycursor.execute('''
        CREATE TABLE IF NOT EXISTS data (
            Id VARCHAR(20) PRIMARY KEY,
            Name VARCHAR(50),
            Phone VARCHAR(15),
            Role VARCHAR(50),
            Gender VARCHAR(20),
            Salary DECIMAL(10,2)
        )
        ''')
    except mysql.connector.Error as err:
        messagebox.showerror('Error', f'Error creating table: {err}')
        exit()

def insert(id, name, phone, role, gender, salary):
    try:
        mycursor.execute('INSERT INTO data (Id, Name, Phone, Role, Gender, Salary) VALUES (%s, %s, %s, %s, %s, %s)', (id, name, phone, role, gender, salary))
        conn.commit()
    except mysql.connector.Error as err:
        messagebox.showerror('Error', f'Error inserting data: {err}')

def id_exists(id):
    try:
        mycursor.execute('SELECT COUNT(*) FROM data WHERE Id=%s', (id,))
        result = mycursor.fetchone()
        return result[0] > 0
    except mysql.connector.Error as err:
        messagebox.showerror('Error', f'Error checking ID existence: {err}')
        return False

def fetch_employees():
    try:
        mycursor.execute('SELECT * FROM data')
        employees = mycursor.fetchall()
        return employees
    except mysql.connector.Error as err:
        messagebox.showerror('Error', f'Error fetching employees: {err}')
        return []

def update(id, new_name, new_phone, new_role, new_gender, new_salary):
    try:
        mycursor.execute('UPDATE data SET Name=%s, Phone=%s, Role=%s, Gender=%s, Salary=%s WHERE Id=%s', (new_name, new_phone, new_role, new_gender, new_salary, id))
        conn.commit()
    except mysql.connector.Error as err:
        messagebox.showerror('Error', f'Error updating data: {err}')

def delete(id):
    try:
        result = messagebox.askyesno('Confirm', 'Do you really want to delete all the records?')
        if not result:
            return
        mycursor.execute('DELETE FROM data WHERE Id=%s', (id,))
        conn.commit()
    except mysql.connector.Error as err:
        messagebox.showerror('Error', f'Error deleting data: {err}')

def search(option, value):
    try:
        valid_options = ['Id', 'Name', 'Phone', 'Role', 'Gender', 'Salary']
        if option not in valid_options:
            raise ValueError(f'Invalid search option: {option}')
        
        mycursor.execute(f'SELECT * FROM data WHERE {option}=%s', (value,))
        result = mycursor.fetchall()
        return result
    except mysql.connector.Error as err:
        messagebox.showerror('Error', f'Error searching data: {err}')
        return []
    except ValueError as err:
        messagebox.showerror('Error', str(err))
        return []


def close_connection():
    global mycursor, conn
    if mycursor:
        mycursor.close()
    if conn:
        conn.close()

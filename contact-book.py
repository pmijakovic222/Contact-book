import sqlite3

# Connect to database
conn = sqlite3.connect("contact-book.db")
conn2 = sqlite3.connect(":memory:")

# Create a cursor
c = conn.cursor()
c2 = conn2.cursor()

# Create table for memory database
c2.execute("""
    CREATE TABLE book(
        name TEXT,
        surname TEXT,
        phone_number INT
    )""")

# Helping variables

# Functions
    # Adding to tables
def add_to_table(name, surname, phone_number):
    c.execute(f"INSERT INTO book VALUES ('{name}', '{surname}', {phone_number})")

def add_to_table2(name, surname, phone_number):
    c2.execute(f"INSERT INTO book VALUES ('{name}', '{surname}', {phone_number})")
    # Deleting from tables
def delete_by_name(name):
    c.execute(f"DELETE FROM book WHERE name='{name}' ")
def delete_by_surname(surname):
    c.execute(f"DELETE FROM book WHERE surname='{surname}' ")
def delete_by_phone(phone):
    c.execute(f"DELETE FROM book WHERE phone_number='{phone}' ")

# Asking user for input
print("Welcome to a contact book in python!")
while True:
    print("Type 'show' if you want to see who is in your book!")
    print("Type 'show_temp' if you want to see who is in your temp book!")
    print("Type 'add' if you want to add new person to book!")
    print("Type 'delete' if you want to remove person from book!")
    default_input = input("contact book > ")
    change_input = default_input
    if default_input == "add":
        name = input("Enter a name of person you want to add to book: ")
        surname_or_no = input("Do you wanna enter a surname?(y/n) ")
        if surname_or_no == "y":
            surname = input("Enter a surname of person you want to add to book: ")
        phone_number = int(input("Enter phone number: "))
        save_it = input("Do you want to save contact number after program stops?(y/n) ")
        if save_it == "y":
            if surname_or_no == "y":
                add_to_table(name, surname, phone_number)
            else:
                add_to_table(name, "", phone_number)
        else:
            if surname_or_no == "y":
                add_to_table2(name, surname, phone_number)
            else:
                add_to_table2(name, "", phone_number)
        
        conn.commit()
    if default_input == "show":
        c.execute("SELECT * FROM book")
        print("")
        print(c.fetchall())
        conn.commit()
    if default_input == "show_temp":
        c2.execute("SELECT * FROM book")
        print("")
        print(c2.fetchall())
        conn2.commit()
    if "delete" in default_input:
        while True:
            by_what = input("Delete by?(name/surname/phone) ")
            if by_what == "name":
                name_del = input("what name > ")
                print("Deleted every person with name " + name_del + " from your book!")
                delete_by_name(name_del)
                break
            elif by_what == "surname":
                surname_del = input("what surname > ")
                print("Deleted every person with surname " + surname_del + " from your book!")
                delete_by_surname(surname_del)
                break
            elif by_what == "phone":
                phone_del = int(input("what phone number > "))
                print("Deleted every person with phone number " + str(phone_del) + " from your book!")
                delete_by_phone(phone_del)
                break
        conn.commit()
    
    print("")


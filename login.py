import hashlib
import sqlite3

conn = sqlite3.connect('users.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS users
             (username TEXT PRIMARY KEY, password TEXT)''')

def login():
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    hash_pass = hashlib.sha256(password.encode()).hexdigest()
    
    c.execute("SELECT password FROM users WHERE username=?", (username,))
    result = c.fetchone()
    if result and result[0] == hash_pass:
        print("Login successful!")
    else:
        print("Invalid username or password.")
        
def create_account():
    username = input("Enter desired username: ")
    password = input("Enter desired password: ")
    
    hash_pass = hashlib.sha256(password.encode()).hexdigest()
    
    try:
        c.execute("INSERT INTO users VALUES (?, ?)", (username, hash_pass))
        conn.commit()
        print("Account created successfully!")
    except sqlite3.IntegrityError:
        print("Username already exists.")
        
while True:
    choice = input("Enter 'l' to login, 'c' to create an account, or 'q' to quit: ")
    if choice == 'l':
        login()
    elif choice == 'c':
        create_account()
    elif choice == 'q':
        break
    else:
        print("Invalid choice. Try again.")    

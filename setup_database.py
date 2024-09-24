import sqlite3

# Create or connect to the database
conn = sqlite3.connect('sun_lab.db')  # This will create a file called 'sun_lab.db'
cursor = conn.cursor()

# Create the table for swipe data (student ID and timestamp)
cursor.execute('''CREATE TABLE IF NOT EXISTS swipe_data (
                   id INTEGER PRIMARY KEY,
                   student_id TEXT,
                   timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
                )''')

# Create the table for student records (to store active/suspended status)
cursor.execute('''CREATE TABLE IF NOT EXISTS students (
                   student_id TEXT PRIMARY KEY,
                   status TEXT DEFAULT 'active'
                )''')

# Commit the changes and close the connection
conn.commit()
conn.close()

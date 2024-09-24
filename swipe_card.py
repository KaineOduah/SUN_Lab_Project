import sqlite3
from datetime import datetime

def swipe_card(student_id):
    # Connect to the database
    conn = sqlite3.connect('sun_lab.db')
    cursor = conn.cursor()

    # Insert the swipe record
    cursor.execute("INSERT INTO swipe_data (student_id) VALUES (?)", (student_id,))

    # Commit and close
    conn.commit()
    conn.close()

    print(f"Card swiped for student ID: {student_id} at {datetime.now()}")

# Example usage:
swipe_card("123456")  # You can replace "123456" with any student ID


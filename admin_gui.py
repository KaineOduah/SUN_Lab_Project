import tkinter as tk
import sqlite3

# Function to search records in the database
def search_records():
    student_id = student_id_entry.get()
    date_from = date_from_entry.get()
    date_to = date_to_entry.get()

    # Connect to the database
    conn = sqlite3.connect('sun_lab.db')
    cursor = conn.cursor()

    # SQL query to search for records
    query = '''SELECT * FROM swipe_data WHERE student_id LIKE ? 
               AND timestamp BETWEEN ? AND ?'''
    cursor.execute(query, (f'%{student_id}%', date_from, date_to))
    records = cursor.fetchall()

    # Display records
    result_text.delete('1.0', tk.END)  # Clear previous results
    for record in records:
        result_text.insert(tk.END, f"Student ID: {record[1]}, Time: {record[2]}\n")

    conn.close()

# Create the main window
root = tk.Tk()
root.title("SUN Lab Access System")

# Labels and entry fields for search filters
tk.Label(root, text="Student ID").grid(row=0, column=0)
student_id_entry = tk.Entry(root)
student_id_entry.grid(row=0, column=1)

tk.Label(root, text="Date From (YYYY-MM-DD)").grid(row=1, column=0)
date_from_entry = tk.Entry(root)
date_from_entry.grid(row=1, column=1)

tk.Label(root, text="Date To (YYYY-MM-DD)").grid(row=2, column=0)
date_to_entry = tk.Entry(root)
date_to_entry.grid(row=2, column=1)

# Search button
search_button = tk.Button(root, text="Search", command=search_records)
search_button.grid(row=3, column=1)

# Result display area
result_text = tk.Text(root, height=10, width=50)
result_text.grid(row=4, column=0, columnspan=2)

root.mainloop()


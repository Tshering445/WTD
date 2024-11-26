import tkinter as tk
from tkinter import messagebox
import sqlite3

def register():
    # Open connection to the database
    conn = sqlite3.connect('fleet_management.db')
    cur = conn.cursor()

    # Insert driver details
    cur.execute("INSERT INTO drivers (name, license, contact_info) VALUES (?, ?, ?)",
                (entry_name.get(), entry_license.get(), entry_contact.get()))

    conn.commit()
    conn.close()
    
    messagebox.showinfo("Success", "Registration successful!")
    root.destroy()  # Close the window after registration

# Tkinter window setup
root = tk.Tk()
root.title("Fleet Management System - Registration")

tk.Label(root, text="Driver Name").grid(row=0)
tk.Label(root, text="Driver License").grid(row=1)
tk.Label(root, text="Contact Info").grid(row=2)

entry_name = tk.Entry(root)
entry_license = tk.Entry(root)
entry_contact = tk.Entry(root)

entry_name.grid(row=0, column=1)
entry_license.grid(row=1, column=1)
entry_contact.grid(row=2, column=1)

tk.Button(root, text="Register", command=register).grid(row=3, column=1)

root.mainloop()

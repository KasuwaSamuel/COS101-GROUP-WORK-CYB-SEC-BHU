import tkinter as tk
import random
import string

def generate_password():
    password_length = int(length_entry.get())
    password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=password_length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

# Create main window
root = tk.Tk()
root.title("Password Generator n")
root.geometry("300x200")
root.configure(bg="blue")

# Length label and entry
length_label = tk.Label(root, text="Password Length:", bg="blue", fg="white")
length_label.pack()
length_entry = tk.Entry(root)
length_entry.pack()

# Password entry
password_entry = tk.Entry(root)
password_entry.pack()

# Generate button
generate_button = tk.Button(root, text="Generate Password", command=generate_password, bg="green", fg="white")
generate_button.pack()

# Quit button
quit_button = tk.Button(root, text="Quit", command=root.quit, bg="green", fg="white")
quit_button.pack()

root.mainloop()

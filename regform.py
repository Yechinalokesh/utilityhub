import tkinter as tk
from tkinter import messagebox

# Dictionary to store user data (username: [email, password])
user_data = {}

def register_user():
    username = username_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    confirm_password = confirm_password_entry.get()

    # Validate inputs
    if not username or not email or not password:
        messagebox.showwarning("Input Error", "Please fill all fields!")
        return

    if password != confirm_password:
        messagebox.showwarning("Password Error", "Passwords do not match!")
        return

    # Store the user data
    user_data[username] = [email, password]
    messagebox.showinfo("Registration Successful", f"User {username} registered successfully!")
    # Clear the fields after registration
    username_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)
    confirm_password_entry.delete(0, tk.END)

def login_user():
    username = login_username_entry.get()
    password = login_password_entry.get()

    # Validate login
    if username in user_data and user_data[username][1] == password:
        messagebox.showinfo("Login Successful", f"Welcome back {username}!")
    else:
        messagebox.showwarning("Login Failed", "Invalid username or password!")

# Registration Window
def registration_window():
    global username_entry, email_entry, password_entry, confirm_password_entry
    
    reg_window = tk.Tk()
    reg_window.title("Registration Page")
    
    # Username
    tk.Label(reg_window, text="Username:").grid(row=0, column=0, padx=10, pady=5)
    username_entry = tk.Entry(reg_window)
    username_entry.grid(row=0, column=1, padx=10, pady=5)
    
    # Email
    tk.Label(reg_window, text="Email:").grid(row=1, column=0, padx=10, pady=5)
    email_entry = tk.Entry(reg_window)
    email_entry.grid(row=1, column=1, padx=10, pady=5)
    
    # Password
    tk.Label(reg_window, text="Password:").grid(row=2, column=0, padx=10, pady=5)
    password_entry = tk.Entry(reg_window, show="*")
    password_entry.grid(row=2, column=1, padx=10, pady=5)
    
    # Confirm Password
    tk.Label(reg_window, text="Confirm Password:").grid(row=3, column=0, padx=10, pady=5)
    confirm_password_entry = tk.Entry(reg_window, show="*")
    confirm_password_entry.grid(row=3, column=1, padx=10, pady=5)
    
    # Submit Button
    submit_button = tk.Button(reg_window, text="Register", command=register_user)
    submit_button.grid(row=4, columnspan=2, pady=10)
    
    reg_window.mainloop()

# Login Window
def login_window():
    global login_username_entry, login_password_entry
    
    login_win = tk.Tk()
    login_win.title("Login Page")
    
    # Username
    tk.Label(login_win, text="Username:").grid(row=0, column=0, padx=10, pady=5)
    login_username_entry = tk.Entry(login_win)
    login_username_entry.grid(row=0, column=1, padx=10, pady=5)
    
    # Password
    tk.Label(login_win, text="Password:").grid(row=1, column=0, padx=10, pady=5)
    login_password_entry = tk.Entry(login_win, show="*")
    login_password_entry.grid(row=1, column=1, padx=10, pady=5)
    
    # Login Button
    login_button = tk.Button(login_win, text="Login", command=login_user)
    login_button.grid(row=2, columnspan=2, pady=10)
    
    login_win.mainloop()

# Choose between registration and login
def choose_window():
    window = tk.Tk()
    window.title("UtilityHub")

    # Buttons to choose between registration and login
    tk.Button(window, text="Register", command=registration_window, width=20).grid(row=0, pady=20)
    tk.Button(window, text="Login", command=login_window, width=20).grid(row=1, pady=20)

    window.mainloop()

# Run the choose window to start
choose_window()
        <a href="/" class="back-link">Back to Home</a>

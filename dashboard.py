import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

def on_closing():
    root.destroy()

# Create the main window
root = tk.Tk()
root.title("Purse Pal Dashboard")
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
root.attributes('-fullscreen', True)

# Create a frame for the top section (logo and user info)
top_frame = tk.Frame(root, bg='#4b2e2a', height=100)
top_frame.pack(side='top', fill='x')

# Load and display the logo image
logo_image = Image.open("pic.png")
logo_image = logo_image.resize((150, 50), Image.LANCZOS)
logo_photo = ImageTk.PhotoImage(logo_image)

logo_label = tk.Label(top_frame, image=logo_photo, bg='#4b2e2a')
logo_label.image = logo_photo
logo_label.pack(side='left', padx=20, pady=10)

# User information
user_label = tk.Label(top_frame, text="Hello, User", fg='white', bg='#4b2e2a', font=('Helvetica', 16))
user_label.pack(side='right', padx=20)

# Create a frame for the balance and reward points
balance_frame = tk.Frame(root, bg='#4b2e2a', height=80)
balance_frame.pack(side='top', fill='x')

balance_label = tk.Label(balance_frame, text="NPR XXXX.XX\nBalance", fg='white', bg='#4b2e2a', font=('Helvetica', 14))
balance_label.pack(side='left', padx=20)

reward_label = tk.Label(balance_frame, text="XXXX.XX\nReward points", fg='white', bg='#4b2e2a', font=('Helvetica', 14))
reward_label.pack(side='right', padx=20)

# Create a frame for the main buttons
main_frame = tk.Frame(root, bg='#4b2e2a', height=150)
main_frame.pack(side='top', fill='x')

buttons_text = ["Send Money", "Add Money", "Banking Service", "Remittance", "Show QR"]
for text in buttons_text:
    button = tk.Button(main_frame, text=text, font=('Helvetica', 14), width=15, bg='#ebeaea')
    button.pack(side='left', padx=10, pady=10)

# Create a frame for the services
services_frame = tk.Frame(root, bg='#4b2e2a', height=200)
services_frame.pack(side='top', fill='both', expand=True)

services_label = tk.Label(services_frame, text="*Our Services", fg='white', bg='#4b2e2a', font=('Helvetica', 16))
services_label.pack(anchor='nw', padx=20, pady=10)

services = ["Topup & Data", "Water & Electricity", "Internet & TV", "Airlines", "Movies",
            "Bus Ticket", "Hotel Booking", "Education Fee", "Insurance", "Others"]

for service in services:
    service_button = tk.Button(services_frame, text=service, font=('Helvetica', 14), width=15, bg='#ebeaea')
    service_button.pack(side='left', padx=10, pady=10)

# Create a frame for the side options
side_frame = tk.Frame(root, bg='#4b2e2a', width=200)
side_frame.pack(side='right', fill='y')

options = ["View Statement", "Transaction Limit", "My Payments", "Support & Call", "About Us", "Settings"]

for option in options:
    option_label = tk.Label(side_frame, text=option, fg='lightblue', bg='#4b2e2a', font=('Helvetica', 14))
    option_label.pack(anchor='nw', padx=20, pady=5)

# Create an exit button to close the fullscreen window
exit_button = tk.Button(root, text="Exit", font=('Helvetica', 14), bg='#4b2e2a', fg='white', command=on_closing)
exit_button.pack(side='bottom', pady=10)

# Run the application
root.mainloop()

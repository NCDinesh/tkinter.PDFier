import tkinter as tk
from tkinter import messagebox

def option1():
    return

def option2():
    return

def option3():
    return

def center_content(event):
    frame.place(relx=0.5, rely=0.5, anchor="center")
    header_label.place(relx=0.5, rely=0.2, anchor="center")
    footer_label.place(relx=0.5, rely=0.8, anchor="center")

# Create the main window
root = tk.Tk()
root.title("Options GUI")
root.geometry("400x200")

# Set the background color to navy blue
navy_blue = "#001F3F"
root.configure(bg=navy_blue)

# Header Label
header_label = tk.Label(root, text="Select an option", font=("Helvetica", 16), pady=10, bg=navy_blue, fg="white")
header_label.pack()

# Frame to hold the option buttons
frame = tk.Frame(root, bg=navy_blue)
frame.place(relx=0.5, rely=0.5, anchor="center")

# Option Buttons
option_button1 = tk.Button(frame, text="Option 1", width=15, height=2, command=option1, bg="white", fg=navy_blue)
option_button1.grid(row=0, column=0, padx=10)

option_button2 = tk.Button(frame, text="Option 2", width=15, height=2, command=option2, bg="white", fg=navy_blue)
option_button2.grid(row=0, column=1, padx=10)

option_button3 = tk.Button(frame, text="Option 3", width=15, height=2, command=option3, bg="white", fg=navy_blue)
option_button3.grid(row=0, column=2, padx=10)

# Footer Label
footer_label = tk.Label(root, text="© 2023 Your Company", font=("Helvetica", 10), pady=5, fg="white", bg=navy_blue)
footer_label.pack()

# Center the content when the window is resized
root.bind("<Configure>", center_content)

# Run the main loop
root.mainloop()

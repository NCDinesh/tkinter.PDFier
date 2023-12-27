from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from PIL import ImageTk, Image
from tkPDFViewer import tkPDFViewer as pdf
import PyPDF2
import os

root1 = Tk()
root1.title("PDFier")
root1.geometry("600x200")

navy_blue = "#ADD8E6"
root1.configure(bg=navy_blue)


def center_content(event):
    frame.place(relx=0.5, rely=0.5, anchor="center")
    header_label.place(relx=0.5, rely=0.3, anchor="center")
    footer_label.place(relx=0.5, rely=0.7, anchor="center")


# Declare my_img as a global variable
my_img = None


def option2():
    def browseFiles():
        file_path = filedialog.askopenfilename(
            initialdir=os.getcwd(),
            title="Select PDF file",
            filetypes=(("PDF files", "*.pdf"), ("All files", "*.*")),
        )

        if file_path:
            pdf_viewer = pdf.ShowPdf()
            pdf_window = pdf_viewer.pdf_view(
                root3, pdf_location=open(file_path, "r"), width=75, height=100
        )
        pdf_window.pack(pady=(0, 0))

    root3 = Toplevel()
    root3.geometry("600x430+300+100")
    root3.title("PDF Viewer")
    root3.configure(bg="white")

# Adjusted the window size to 800x600 for better viewing
    Button(
        root3,
        text="Open",
        command=browseFiles,
        width=40,
        font="arial 20",
        bd=4,
    ).pack(pady=(20, 20))  # Added some padding for aesthetics

   


def option3():
    return


def option1():
    root = Toplevel()
    root.title("PDF Secure")
    root.geometry("600x430+300+100")
    root.resizable(False, False)

    def browse():
        global filename
        filename = filedialog.askopenfilename(initialdir=os.getcwd(),
                                              title="Select PDF File",
                                              filetypes=(('PDF File', '*.pdf'), ('all files', '*.*')))
        entry1.delete(0, END)  # Clear the entry before inserting the new filename
        entry1.insert(END, filename)

    def protect(entry1, entry2, entry3):
        mainfile = entry1.get()
        protectfile = entry2.get()
        code = entry3.get()

        if mainfile == "" and protectfile == "" and code == "":
            messagebox.showerror("Invalid", "All entries are empty!")
        elif mainfile == "":
            messagebox.showerror("Invalid", "Please select or type the source PDF")
        elif protectfile == "":
            messagebox.showerror("Invalid", "Please Type Target PDF filename")
        elif code == "":
            messagebox.showerror("Invalid", "Please Type the Password")
        else:
            try:
                out = PyPDF2.PdfWriter()
                file = PyPDF2.PdfReader(filename, "rb")
                num = len(file.pages)

                for idx in range(num):
                    page = file.pages[idx]
                    out.add_page(page)

                # password
                out.encrypt(code)

                with open(protectfile, "wb") as f:
                    out.write(f)

                source.set("")
                target.set("")
                password.set("")

                messagebox.showinfo("Info", "Success!")

            except Exception as e:
                messagebox.showerror("Invalid", e)

    global my_img  # Use the global my_img variable
    my_img = ImageTk.PhotoImage(Image.open("D:/GUI(tkinter)/project/images/top image.png"))
    my_label = Label(root, image=my_img)
    my_label.pack()

    global source, target, password, entry1, entry2, entry3
    frame = Frame(root, width=580, height=290, bd=5, relief=GROOVE)
    frame.place(x=10, y=130)

    source = StringVar()
    Label(frame, text="Source PDF file:", font="arial 10 bold", fg="#4c4542").place(x=30, y=50)
    entry1 = Entry(frame, width=30, textvariable=source, font="arial 15", bd=1)
    entry1.place(x=150, y=48)

    Button(frame, text="Browse", bg="#d3cdcd", command=browse).place(x=500, y=45)

    target = StringVar()
    Label(frame, text="Target PDF file:", font="arial 10 bold", fg="#4c4542").place(x=30, y=100)
    entry2 = Entry(frame, width=30, textvariable=target, font="arial 15", bd=1)
    entry2.place(x=150, y=100)

    password = StringVar()
    Label(frame, text="Set User Password:", font="arial 10 bold", fg="#4c4542").place(x=17, y=150)
    entry3 = Entry(frame, width=30, textvariable=password, font="arial 15", bd=1)
    entry3.place(x=150, y=150)

    Button(root, text="Protect PDF file", bg="#bfb9b9", font="arial 14 bold",
           command=lambda: protect(entry1, entry2, entry3)).pack(side=BOTTOM, pady=40)

    root.bind("<Configure>", center_content)  # Bind the centering function to the Configure event


# Header Label
header_label = Label(root1, text="Select an option", font=("Helvetica", 20), pady=10, bg=navy_blue, fg="Black")
header_label.pack()

# Frame to hold the option buttons
frame = Frame(root1, bg=navy_blue)
frame.pack(pady=20)

# Option Buttons
option_button1 = Button(frame, text="Read PDF", width=15, height=2, command=option2, bg="#d3cdcd")
option_button1.grid(row=3, column=0, padx=10)

option_button2 = Button(frame, text="Secure PDF", width=15, height=2, command=option1, bg="#d3cdcd")
option_button2.grid(row=3, column=1, padx=10)

option_button3 = Button(frame, text="Text To Speech", width=15, height=2, command=option3, bg="#d3cdcd")
option_button3.grid(row=3, column=2, padx=10)

# Footer Label
footer_label = Label(root1, text="Minor Project", font=("Helvetica", 10), pady=5, fg="Black", bg=navy_blue)
footer_label.pack()

root1.bind("<Configure>", center_content)  # Bind the centering function to the Configure event

root1.mainloop()

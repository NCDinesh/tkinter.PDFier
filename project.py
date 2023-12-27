from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import PyPDF2
import os

root = Tk()
root.title("PDFier")
root.geometry("600x430+300+100") 
root.resizable(False, False)

def browse():
    global filename
    filename = filedialog.askopenfilename(initialdir=os.getcwd(),
                                          title="Select PDF File",
                                          filetypes=(('PDF File', '*.pdf'), ('all files', '*.*')))
    entry1.delete(0, END)  # Clear the entry before inserting the new filename
    entry1.insert(END, filename)

def protect():
    mainfile = source.get()
    protectfile = target.get()
    code = password.get()

    if mainfile == "" and protectfile == "" and code == "":
        messagebox.showerror("Invalid", "All entries are empty!")

    elif mainfile == "":
        messagebox.showerror("Invalid", "Please select or type the source PDF")

    elif protectfile == "":
        messagebox.showerror("Invalid", "Please Type Target PDF filename")

    elif password.get() == "":
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

        except:
            messagebox.showerror("Invalid","Invalid entry")


# icon
image_icon = PhotoImage(file="images/protect.png")
root.iconphoto(False, image_icon)

# main
Top_image = PhotoImage(file="images/top.png")
Label(root, image=Top_image).pack()

frame = Frame(root, width=580, height=290, bd=5, relief=GROOVE)
frame.place(x=10, y=130)

source = StringVar()
Label(frame, text="Source PDF file:", font="arial 10 bold", fg="#4c4542").place(x=30, y=50)
entry1 = Entry(frame, width=30, textvariable=source, font="arial 15", bd=1)
entry1.place(x=150, y=48)

button_icon = PhotoImage(file="images/folder.png")
Button(frame, image=button_icon, width=35, height=24, bg="#d3cdcd", command=browse).place(x=500, y=45)

target = StringVar()
Label(frame, text="Target PDF file:", font="arial 10 bold", fg="#4c4542").place(x=30, y=100)
entry2 = Entry(frame, width=30, textvariable=target, font="arial 15", bd=1)
entry2.place(x=150, y=100)

password = StringVar()
Label(frame, text="Set User Password:", font="arial 10 bold", fg="#4c4542").place(x=17, y=150)
entry3 = Entry(frame, width=30, textvariable=password, font="arial 15", bd=1)
entry3.place(x=150, y=150)

button_icon1 = PhotoImage(file="")
protect = Button(root, text=" Protect PDF file:", compound=LEFT, image=button_icon1, width=230, height=50, bg="#bfb9b9",
                font="arial 14 bold", command=protect)
protect.pack(side=BOTTOM, pady=40)

root.mainloop()

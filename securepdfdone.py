from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from PIL import ImageTk,Image
import PyPDF2
import os

root1=Tk()
root1.title("PDFier")
root1.geometry("600x430+300+100") 



def option2():
    return

def option3():
    return

def option1():
    root = Tk()
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

    def protect(entry1,entry2,entry3):
       
        # global mainfile,protectfile,code
        # mainfile = source.get()
        # protectfile = target.get()
        # code = password.get()

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
                messagebox.showerror("Invalid",e)


# icon
    # image_icon = PhotoImage(file="images/protect.png")
    # root.iconphoto(False, image_icon)

# main
    # Top_image = PhotoImage(file="images/top.png")
    # Label(root, image=Top_image).pack()
  
    
    global source,target,password,entry1,entry2,entry3
    frame = Frame(root, width=580, height=290, bd=5, relief=GROOVE)
    frame.place(x=10, y=130)

    source = StringVar()
    Label(frame, text="Source PDF file:", font="arial 10 bold", fg="#4c4542").place(x=30, y=50)
    entry1 = Entry(frame, width=30, textvariable=source, font="arial 15", bd=1)
    entry1.place(x=150, y=48)

    # button_icon = PhotoImage(file="images/folder.png")
    Button(frame,text="Browse" ,bg="#d3cdcd", command=browse).place(x=500, y=45)

    target = StringVar()
    Label(frame, text="Target PDF file:", font="arial 10 bold", fg="#4c4542").place(x=30, y=100)
    entry2 = Entry(frame, width=30, textvariable=target, font="arial 15", bd=1)
    entry2.place(x=150, y=100)

    password = StringVar()
    Label(frame, text="Set User Password:", font="arial 10 bold", fg="#4c4542").place(x=17, y=150)
    entry3 = Entry(frame, width=30, textvariable=password, font="arial 15", bd=1)
    entry3.place(x=150, y=150)

    # button_icon1 = PhotoImage(file="")
    Button(root, text="Protect PDF file", bg="#bfb9b9",
           font="arial 14 bold", command=lambda: protect(entry1, entry2, entry3)).pack(side=BOTTOM, pady=40)


# Header Label

header_label = Label(root1, text="Select an option", font=("Helvetica", 16), pady=10)
header_label.pack()

# Frame to hold the option buttons
frame = Frame(root1)
frame.pack(pady=20)

# Option Buttons
option_button1 = Button(frame, text="Read PDF", width=15, height=2,
                              command=option2)
option_button1.grid(row=0, column=0, padx=10)

option_button2 = Button(frame, text="Secure PDF", width=15, height=2,
                              command=option1)
option_button2.grid(row=0, column=1, padx=10)

option_button3 = Button(frame, text="Text To Speech", width=15, height=2,
                              command=option3)
option_button3.grid(row=0, column=2, padx=10)

# Footer Label
footer_label = Label(root1, text="Minor Project", font=("Helvetica", 10), pady=5, fg="gray")
footer_label.pack()



root1.mainloop()

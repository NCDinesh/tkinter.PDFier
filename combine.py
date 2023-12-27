from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from PIL import ImageTk, Image
from tkinter.ttk import Combobox
import pyttsx3
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
Logo = None
imageicon = None
imageicon1 = None
button_icon1 =None
opennow=None


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
    global opennow
    opennow = ImageTk.PhotoImage(Image.open("D:/GUI(tkinter)/project/images/open1.png"))

    read =Button(
        root3,
        text="Open",
        compound=LEFT,
        image=opennow,
        command=browseFiles,
        width=600,
        font="arial 20",
        bd=4,
    )
    read.pack()



   


def option3():
    root5=Toplevel()
    root5.title("PDF Speech")
    root5.geometry("900x450+200+200")
    root5.resizable(False,False)
    root5.configure(bg="#305065")

    engine = pyttsx3.init()

    global imageicon,imageicon1

    def extract_text_from_pdf(pdf_path):
        global text
        with open(pdf_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            text = ""
            for page_number in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_number]
                text += page.extract_text()

        return text
    
    def browse_files():
        global text
        file_path = filedialog.askopenfilename(
            initialdir=os.getcwd(),  # Set the initial directory
            title="Select PDF file",
            filetypes=(("PDF files", "*.pdf"), ("All files", "*.*")),
        )

        if file_path:
            text = extract_text_from_pdf(file_path)

        
            text_area.delete(0, END)  # Clear the entry before inserting the new filename
            text_area.insert(END, text)
            print("Extracted Text:")
            print(text)
            # You can store or display the text as needed


    def speaknow():
        text=text_area.get()
        gender= gender_combobox.get()
        speed = speed_combobox.get()
        voices = engine.getProperty('voices')
    
        def setvoice():
            if(gender =='Male'):
                engine.setProperty('voice',voices[0].id)
                engine.say(text)
                engine.runAndWait()
            else:
                engine.setProperty('voice',voices[1].id)
                engine.say(text)
                engine.runAndWait()
    
        if (text):
            if(speed == 'Fast'):
                engine.setProperty('rate',250)
                setvoice()

            elif(speed == 'Normal'):
                engine.setProperty('rate',150)
                setvoice()

            else:
                setvoice()
                engine.setProperty('rate',60)

        
    def download():
        text=text_area.get()
        gender= gender_combobox.get()
        speed = speed_combobox.get()
        voices = engine.getProperty('voices')
    
        def setvoice():
            if(gender =='Male'):
                engine.setProperty('voice',voices[0].id)
                path=filedialog.askdirectory()
                os.chdir(path)

                engine.save_to_file(text ,"text.mp3")
                engine.runAndWait()
            else:
                engine.setProperty('voice',voices[1].id)
                path=filedialog.askdirectory()
                os.chdir(path)
                engine.save_to_file(text ,"text.mp3")
                engine.runAndWait()
    
        if (text):
            if(speed == 'Fast'):
                engine.setProperty('rate',250)
                setvoice()

            elif(speed == 'Normal'):
                engine.setProperty('rate',150)
                setvoice()

            else:
                setvoice()
                engine.setProperty('rate',60)
        
    #icon
    global Logo,imageicon,imageicon1

    # image_icon = ImageTk.PhotoImage(Image.open("images/speak.png"))
    # root5.iconphoto(False,image_icon)

    #Top Frame
    Top_frame=Frame(root5,bg="white",width=900,height=100)
    Top_frame.place(x=0,y=0)

    Logo = ImageTk.PhotoImage(Image.open("images/speaker logo.png"))
    logo_label=Label(Top_frame,image=Logo)
    logo_label.place(x=10,y=5)

    # Logo = ImageTk.PhotoImage(Image.open("D:/GUI(tkinter)/project/images/top image.png"))
    # Logo_label = Label(root5, image=Logo)
    # Logo_label.pack()

    Label(Top_frame,text="PDF TO SPEECH",font="arial 20 bold",bg="white",fg="black").place(x=110,y=40)

    global text_area
    text_area=Entry(root5,font="Robote 20",bg="white")
    text_area.place(x=10,y=150,width=500,height=250)


    Label(root5,text="VOICE",font="arial 15 bold",bg="#305605",fg="white").place(x=570,y=160)
    Label(root5,text="SPEED",font="arial 15 bold",bg="#305605",fg="white").place(x=760,y=160)

    gender_combobox=Combobox(root5,values=['Male','Female'],font="arial 14",state='r',width=10)
    gender_combobox.place(x=550,y=200)
    gender_combobox.set('Male')

    speed_combobox=Combobox(root5,values=['Fast','Normal','Slow'],font="arial 14",state='r',width=10)
    speed_combobox.place(x=730,y=200)
    speed_combobox.set('Normal')

    imageicon = ImageTk.PhotoImage(Image.open("images/speak.png"))
    btn=Button(root5,text="Speech",compound=LEFT,image=imageicon,width=130,bg="light yellow",font="arial 14 bold",command=speaknow)
    btn.place(x=550,y=270)


    # btn=Button(root5,text="Speech",bg="light yellow",font="arial 14 bold",command=speaknow)
    # btn.place(x=550,y=270)
    
    imageicon1 = ImageTk.PhotoImage(Image.open("D:/GUI(tkinter)/project/images/download.png"))
    save=Button(root5,text="Save",compound=LEFT,image=imageicon1,width=130,bg="light green",font="arial 14 bold",command=download)
    save.place(x=730,y=270)



    btnpdf=Button(root5,text="Upload PDF",font="arial 10 bold",command=browse_files)
    btnpdf.place(x=10,y=410)

    

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

    def Protect(entry1, entry2, entry3):
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

    global my_img,button_icon1  # Use the global my_img variable
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

    
    button_icon1 = ImageTk.PhotoImage(Image.open("D:/GUI(tkinter)/project/images/icon.png"))
    protect = Button(root, text=" Protect PDF file:", compound=LEFT, image=button_icon1, width=300, height=50, bg="#bfb9b9",
                font="arial 14 bold", command=lambda:Protect(entry1,entry2,entry3))
    protect.pack(side=BOTTOM, pady=40)
    
    # Button(root, text="Protect PDF file", bg="#bfb9b9", font="arial 14 bold",
    #        command=lambda: protect(entry1, entry2, entry3)).pack(side=BOTTOM, pady=40)

    root.bind("<Configure>", center_content)  # Bind the centering function to the Configure event


# Header Label
header_label = Label(root1, text="Select an option", font=("Helvetica", 20), pady=20, bg=navy_blue, fg="Black")
header_label.pack()

# Frame to hold the option buttons
frame = Frame(root1, bg=navy_blue)
frame.pack(pady=20)


# Option Buttons
option_button1 = Button(frame, text="Read PDF",font="arial 10 bold" ,width=15, height=2, command=option2, bg="#d3cdcd")
option_button1.grid(row=3, column=0, padx=5)


option_button2 = Button(frame, text="Secure PDF",font="arial 10 bold", width=15, height=2, command=option1, bg="#d3cdcd")
option_button2.grid(row=3, column=1, padx=5)

option_button3 = Button(frame, text="Text To Speech",font="arial 10 bold", width=15, height=2, command=option3, bg="#d3cdcd")
option_button3.grid(row=3, column=2, padx=5)

# Footer Label
footer_label = Label(root1, text="Minor Project", font=("Helvetica", 10), pady=5, fg="Black", bg=navy_blue)
footer_label.pack()

root1.bind("<Configure>", center_content)  # Bind the centering function to the Configure event

root1.mainloop()

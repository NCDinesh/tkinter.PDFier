from tkinter import *

from tkinter import filedialog
from tkinter.ttk import Combobox
import pyttsx3
import os
import PyPDF2

root=Tk()
root.title("PDF Speech")
root.geometry("900x450+200+200")
root.resizable(False,False)
root.configure(bg="#305065")

engine = pyttsx3.init()

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
        initialdir="/",  # Set the initial directory
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
image_icon = PhotoImage(file="images/speak.png")
root.iconphoto(False,image_icon)

#Top Frame
Top_frame=Frame(root,bg="white",width=900,height=100)
Top_frame.place(x=0,y=0)

Logo=PhotoImage(file="images/speaker logo.png")
Label(Top_frame,image=Logo).place(x=10,y=5)

Label(Top_frame,text="PDF TO SPEECH",font="arial 20 bold",bg="white",fg="black").place(x=110,y=40)

global text_area
text_area=Entry(root,font="Robote 20",bg="white")
text_area.place(x=10,y=150,width=500,height=250)


Label(root,text="VOICE",font="arial 15 bold",bg="#305605",fg="white").place(x=570,y=160)
Label(root,text="SPEED",font="arial 15 bold",bg="#305605",fg="white").place(x=760,y=160)

gender_combobox=Combobox(root,values=['Male','Female'],font="arial 14",state='r',width=10)
gender_combobox.place(x=550,y=200)
gender_combobox.set('Male')

speed_combobox=Combobox(root,values=['Fast','Normal','Slow'],font="arial 14",state='r',width=10)
speed_combobox.place(x=730,y=200)
speed_combobox.set('Normal')

imageicon=PhotoImage(file="images/speak.png")
btn=Button(root,text="Speech",compound=LEFT,image=imageicon,width=130,bg="light yellow",font="arial 14 bold",command=speaknow)
btn.place(x=550,y=270)

imageicon1=PhotoImage(file="images/download.png")
save=Button(root,text="Save",compound=LEFT,image=imageicon1,width=130,bg="light green",font="arial 14 bold",command=download)
save.place(x=730,y=270)

btnpdf=Button(root,text="Upload PDF",font="arial 10 bold",command=browse_files)
btnpdf.place(x=10,y=410)



root.mainloop()
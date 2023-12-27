import tkinter as tk
from tkinter import filedialog
import PyPDF2
import pyttsx3

def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        text = ""
        for page_number in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_number]
            text += page.extract_text()

    return text

def convert_text_to_speech(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def browse_files():
    file_path = filedialog.askopenfilename(
        initialdir="/",  # Set the initial directory
        title="Select PDF file",
        filetypes=(("PDF files", "*.pdf"), ("All files", "*.*")),
    )

    if file_path:
        text = extract_text_from_pdf(file_path)
        convert_text_to_speech(text)

# Tkinter setup
root = tk.Tk()
root.geometry("400x200")
root.title("PDF to Speech Converter")

# Button to open file dialog
tk.Button(root, text="Open PDF", command=browse_files).pack(pady=20)

root.mainloop()
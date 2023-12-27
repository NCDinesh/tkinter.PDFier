from tkinter import *
from tkinter import filedialog
from tkPDFViewer import tkPDFViewer as pdf

import os

def browseFiles():
    file_path = filedialog.askopenfilename(
        initialdir=os.getcwd(),
        title="Select PDF file",
        filetypes=(("PDF files", "*.pdf"), ("All files", "*.*")),
    )

    if file_path:
        pdf_viewer = pdf.ShowPdf()
        pdf_window = pdf_viewer.pdf_view(
            root, pdf_location=open(file_path, "r"), width=75, height=100
        )
        pdf_window.pack(pady=(0, 0))

root = Tk()
root.geometry("800x800+300+100")
root.title("PDF Viewer")
root.configure(bg="white")

# Adjusted the window size to 800x600 for better viewing
Button(
    root,
    text="Open",
    command=browseFiles,
    width=40,
    font="arial 20",
    bd=4,
).pack(pady=(20, 20))  # Added some padding for aesthetics

root.mainloop()

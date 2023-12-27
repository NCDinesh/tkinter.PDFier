from tkinter import *
from tkinter import filedialog
import PyPDF2

def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        text = ""
        for page_number in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_number]
            text += page.extract_text()

    return text

def browse_files():
    file_path = filedialog.askopenfilename(
        initialdir="/",  # Set the initial directory
        title="Select PDF file",
        filetypes=(("PDF files", "*.pdf"), ("All files", "*.*")),
    )

    if file_path:
        text = extract_text_from_pdf(file_path)
        print("Extracted Text:")
        print(text)

        
        # You can store or display the text as needed

# Tkinter setup
root = Tk()
root.geometry("400x200")
root.title("PDF Text Extractor")

# Button to open file dialog
Button(root, text="Open PDF", command=browse_files).pack(pady=20)

root.mainloop()
import os
import tkinter as tk

from PIL import Image
from PyPDF2 import PdfMerger, PdfReader, PdfWriter
import fitz  # PyMuPDF

from pathlib import Path
# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Button, PhotoImage, simpledialog
from tkinter import filedialog, messagebox
from tkinter.simpledialog import Dialog

from PyPDF2 import PdfMerger


class CustomIntegerDialog(Dialog):
    def __init__(self, parent, title, prompt):
        self.prompt = prompt
        self.result = None
        super().__init__(parent, title)

    def body(self, master):
        tk.Label(master, text=self.prompt).grid(row=0)
        self.entry = tk.Entry(master)
        self.entry.grid(row=1, column=0)
        self.entry.focus_set()
        return self.entry

    def apply(self):
        try:
            self.result = int(self.entry.get())
        except ValueError:
            self.result = None


def merge_pdfs():
    root = tk.Tk()
    root.withdraw()
    pdf_files = filedialog.askopenfilenames(title="Select PDF Files to Merge", filetypes=[("PDF files", "*.pdf")])
    if not pdf_files:
        messagebox.showerror("No file selected", "Please select at least one PDF file to merge.")
        return

    merger = PdfMerger()
    for pdf in pdf_files:
        merger.append(pdf)

    save_path = filedialog.asksaveasfilename(title="Save Merged PDF", defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
    if not save_path:
        messagebox.showerror("No save location", "Please select a location to save the merged PDF.")
        return

    merger.write(save_path)
    merger.close()
    messagebox.showinfo("Success", f"Merged PDF saved successfully at {save_path}")
def image_to_pdf():
    root = tk.Tk()
    root.withdraw()
    image_files = filedialog.askopenfilenames(title="Select Images to Convert to PDF", filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")])
    if not image_files:
        messagebox.showerror("No file selected", "Please select at least one image file.")
        return

    images = [Image.open(image).convert("RGB") for image in image_files]

    save_path = filedialog.asksaveasfilename(title="Save PDF", defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
    if not save_path:
        messagebox.showerror("No save location", "Please select a location to save the PDF.")
        return

    images[0].save(save_path, save_all=True, append_images=images[1:])
    messagebox.showinfo("Success", f"PDF saved successfully at {save_path}")
def encrypt_pdf():
    root = tk.Tk()
    root.withdraw()
    pdf_file = filedialog.askopenfilename(title="Select a PDF File to Encrypt", filetypes=[("PDF files", "*.pdf")])
    if not pdf_file:
        messagebox.showerror("No file selected", "Please select a PDF file to encrypt.")
        return

    password = simpledialog.askstring("Password", "Enter password for the PDF:")
    if not password:
        messagebox.showerror("No password", "Please enter a password for encryption.")
        return

    reader = PdfReader(pdf_file)
    writer = PdfWriter()

    for page in reader.pages:
        writer.add_page(page)

    writer.encrypt(password)

    save_path = filedialog.asksaveasfilename(title="Save Encrypted PDF", defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
    if not save_path:
        messagebox.showerror("No save location", "Please select a location to save the encrypted PDF.")
        return

    with open(save_path, 'wb') as f:
        writer.write(f)

    messagebox.showinfo("Success", f"Encrypted PDF saved successfully at {save_path}")

def pdf_to_image():
    root = tk.Tk()
    root.withdraw()
    pdf_file = filedialog.askopenfilename(title="Select a PDF File to Convert to Images", filetypes=[("PDF files", "*.pdf")])
    if not pdf_file:
        messagebox.showerror("No file selected", "Please select a PDF file to convert.")
        return

    output_dir = filedialog.askdirectory(title="Select Output Directory")
    if not output_dir:
        messagebox.showerror("No directory selected", "Please select an output directory.")
        return

    try:
        # Create the output directory if it doesn't exist
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        # Convert PDF to images
        pdf_document = fitz.open(pdf_file)

        for page_number in range(pdf_document.page_count):
            page = pdf_document.load_page(page_number)
            image = page.get_pixmap(matrix=fitz.Matrix(2, 2))  # You can adjust the matrix for image size

            image_path = os.path.join(output_dir, f"page_{page_number + 1}.JPG")
            image.save(image_path)

        pdf_document.close()

        messagebox.showinfo("Success", f"PDF pages saved as images in {output_dir}")

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while converting PDF to images: {e}")

def split_pdf():
    root = tk.Tk()
    root.withdraw()
    pdf_file = filedialog.askopenfilename(title="Select a PDF File to Split", filetypes=[("PDF files", "*.pdf")])
    if not pdf_file:
        messagebox.showerror("No file selected", "Please select a PDF file to split.")
        return

    output_dir = filedialog.askdirectory(title="Select Output Directory")
    if not output_dir:
        messagebox.showerror("No directory selected", "Please select an output directory.")
        return

    start_page_dialog = CustomIntegerDialog(root, "Start Page", "Enter the starting page number:")
    start_page = start_page_dialog.result
    if start_page is None:
        messagebox.showerror("No start page", "Please enter the starting page number.")
        return

    end_page_dialog = CustomIntegerDialog(root, "End Page", "Enter the ending page number:")
    end_page = end_page_dialog.result
    if end_page is None:
        messagebox.showerror("No end page", "Please enter the ending page number.")
        return

    output_pdf = filedialog.asksaveasfilename(title="Save Split PDF", defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
    if not output_pdf:
        messagebox.showerror("No save location", "Please select a location to save the split PDF.")
        return

    try:
        # Open the input PDF file
        with open(pdf_file, "rb") as pdf_file:
            pdf_reader = PdfReader(pdf_file)
            pdf_writer = PdfWriter()

            # Perform page splitting and add pages to the new PDF
            for page_num in range(start_page - 1, min(end_page, len(pdf_reader.pages))):
                page = pdf_reader.pages[page_num]
                pdf_writer.add_page(page)

            # Save the new PDF to the output file
            with open(output_pdf, "wb") as output_file:
                pdf_writer.write(output_file)

        messagebox.showinfo("Success", f"PDF pages {start_page} to {end_page} have been split and saved as '{output_pdf}'")

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while splitting the PDF: {e}")

def split_pdf_specific_pages():
    root = tk.Tk()
    root.withdraw()
    pdf_file = filedialog.askopenfilename(title="Select a PDF File to Split Specific Pages", filetypes=[("PDF files", "*.pdf")])
    if not pdf_file:
        messagebox.showerror("No file selected", "Please select a PDF file to split.")
        return

    output_dir = filedialog.askdirectory(title="Select Output Directory")
    if not output_dir:
        messagebox.showerror("No directory selected", "Please select an output directory.")
        return

    pages = simpledialog.askstring("Pages", "Enter the page numbers to split (comma-separated, e.g., 1,2,3):")
    if not pages:
        messagebox.showerror("No pages", "Please enter the page numbers to split.")
        return

    page_numbers = list(map(int, pages.split(',')))

    reader = PdfReader(pdf_file)
    writer = PdfWriter()
    for page_num in page_numbers:
        if 1 <= page_num <= len(reader.pages):
            writer.add_page(reader.pages[page_num - 1])

    save_path = filedialog.asksaveasfilename(title="Save Split PDF", defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
    if not save_path:
        messagebox.showerror("No save location", "Please select a location to save the split PDF.")
        return

    with open(save_path, 'wb') as f:
        writer.write(f)

    messagebox.showinfo("Success", f"Split PDF saved successfully at {save_path}")


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"D:\Tkinter-Designer\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("676x433")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 433,
    width = 676,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    338.0,
    244.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    321.00000274181366,
    295.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    363.0,
    212.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    347.00002722773945,
    214.99998534722909,
    image=image_image_4
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    321.00001960992813,
    386.00000232458115,
    image=image_image_5
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: encrypt_pdf(),
    relief="flat"
)
button_1.place(
    x=468.0,
    y=166.0,
    width=168.0,
    height=68.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: image_to_pdf(),
    relief="flat"
)
button_2.place(
    x=79.0,
    y=173.0,
    width=168.0,
    height=68.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: merge_pdfs(),
    relief="flat"
)
button_3.place(
    x=79.0,
    y=49.0,
    width=168.0,
    height=68.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: pdf_to_image(),
    relief="flat"
)
button_4.place(
    x=468.0,
    y=44.0,
    width=168.0,
    height=68.0
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: split_pdf(),
    relief="flat"
)
button_5.place(
    x=79.0,
    y=307.0,
    width=168.0,
    height=68.0
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: split_pdf_specific_pages(),
    relief="flat"
)
button_6.place(
    x=468.0,
    y=300.0,
    width=168.0,
    height=68.0
)
window.resizable(False, False)
window.mainloop()

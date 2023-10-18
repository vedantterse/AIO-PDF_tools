# AIO-PDF_tools
PDF Tools
Overview
PDF Tools is a command-line utility that provides a set of tools for working with PDF files. The tools included in this utility allow users to perform various actions such as merging PDFs, converting images to PDF, encrypting PDFs, converting PDFs to images, splitting PDFs, and extracting specific pages from a PDF.

Features
PDF Merger: Merge multiple PDF files into a single PDF.
Image to PDF Converter: Convert a collection of images to a PDF document.
PDF Encryption: Encrypt PDF files with a password for added security.
PDF to Image Converter: Convert PDF pages to image files.
PDF Splitter: Split a PDF into multiple parts.
Custom Page Extraction: Extract specific pages from a PDF document.
How to Use
Directory Setup:

Place your PDF files in the designated input directories as mentioned below:
PDF_Merger: For PDF merger tool.
input_img2pdf: For image to PDF converter.
PDF_ENCRYPT: For PDF encryption tool.
input_pdf_to_img: For PDF to image converter.
input_split: For PDF splitter tool.
input_custom_pages: For custom page extraction tool.
Run the Script:

Execute the script and follow the on-screen instructions.
Choose the desired action by entering the corresponding number.
Check Outputs:

The results of the operations will be available in the respective output directories.
Example Usage
Merging PDFs:
bash
Copy code
python pdf_tools.py
# Choose option 1 for PDF Merger
# Place PDF files in 'PDF_Merger' directory
# Check merged PDF in 'Merged_pdf' directory
Image to PDF Conversion:
bash
Copy code
python pdf_tools.py
# Choose option 2 for Image to PDF Converter
# Place images in 'input_img2pdf' directory
# Check converted PDF in 'img2pdf_output' directory
PDF Encryption:
bash
Copy code
python pdf_tools.py
# Choose option 3 for PDF Encryption
# Place PDF file in 'PDF_ENCRYPT' directory
# Enter password when prompted
# Check encrypted PDF in 'ENCRYPTED_PDF' directory
PDF to Image Conversion:
bash
Copy code
python pdf_tools.py
# Choose option 4 for PDF to Image Converter
# Place PDF files in 'input_pdf_to_img' directory
# Check converted images in 'output_pdf_to_img' directory
PDF Splitting:
bash
Copy code
python pdf_tools.py
# Choose option 5 for PDF Splitter
# Place PDF file in 'input_split' directory
# Enter start and end page numbers
# Check split PDF in 'output_split' directory
Custom Page Extraction:
bash
Copy code
python pdf_tools.py
# Choose option 6 for Custom Page Extraction
# Place PDF file in 'input_custom_pages' directory
# Enter page numbers to extract (e.g., 1 3 5)
# Check extracted PDF in 'output_custom_pages' directory
Notes
Ensure that the required input directories are created before running the script.
Follow on-screen instructions for each tool to complete the desired action.
Contact the project owner for any issues or additional information.
Feel free to customize the above README to include more details or specific instructions based on your project's needs.

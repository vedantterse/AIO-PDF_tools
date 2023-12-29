# AIO-PDF_tools
# PDF Tools
Overview
PDF Tools is a command-line utility that provides a set of tools for working with PDF files. The tools included in this utility allow users to perform various actions such as merging PDFs, converting images to PDF, encrypting PDFs, converting PDFs to images, splitting PDFs, and extracting specific pages from a PDF.

# Features
**PDF Merger: Merge multiple PDF files into a single PDF.**

**Image to PDF Converter: Convert a collection of images to a PDF document.**

**PDF Encryption: Encrypt PDF files with a password for added security.**

**PDF to Image Converter: Convert PDF pages to image files.**

**PDF Splitter: Split a PDF into multiple parts.**

**Custom Page Extraction: Extract specific pages from a PDF document.**


## How to Use
 
**Getting Started**

To set up the project locally, follow these steps:

1. **Clone the Repository:**
    
   ```
   git clone https://github.com/your-username/PDF_Tools.git
   ```
   
   ```
   cd PDF_Tools
   ```
------refer to 'Instructions:' down below and then exceute this commands of setup script if that dosent work-------
   
Run the Setup Script:
```
bash setup.sh
```

If you encounter permission issues, you might need to make the script executable:

```
chmod +x setup.sh
```

The setup script will create the necessary directories for each tool:


Additionally, it will install any dependencies required for the tools.

Run the PDF Tools:

python pdf_tools.py
Follow the on-screen instructions to use the tools.

![image](https://github.com/vedantterse/AIO-PDF_tools/assets/69134828/86bc9c07-9f9f-47f1-a830-0a4171e036b7)






### 
Instructions:-
Make sure Python is installed on your computer.
Open the terminal in the directory where you've cloned the repository.
Execute the following commands one by one in the terminal:
 
 ```
python -m pip install PyPDF2
 ```

 ```
 python -m pip install PyMuPDF
```
 
 ```
python -m pip install img2pdf
```
 
Feel free to explore and contribute to the project. If you encounter any issues, please report them in the Issues section.
 


**Directory Setup:**
Place your PDF files in the designated input directories as mentioned below:
_PDF_Merger: For PDF merger tool._

input_img2pdf: For image to PDF converter.

PDF_ENCRYPT: For PDF encryption tool.

input_pdf_to_img: For PDF to image converter.

input_split: For PDF splitter tool.

input_custom_pages: For custom page extraction tool.

Run the Script:

Execute the script and follow the on-screen instructions.
Choose the desired action by entering the corresponding number.
Check the Output.!

  
Notes
Ensure that the required input directories are created before running the script.
Follow on-screen instructions for each tool to complete the desired action.
Contact the project owner for any issues or additional information.
 

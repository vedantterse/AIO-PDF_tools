@echo off
echo Setting up PDF Tools...

:: Function to create directories
:CREATE_DIRECTORIES
for %%i in (
    "PDF_Merger"
    "Merged_pdf"
    "input_img2pdf"
    "img2pdf_output"
    "PDF_ENCRYPT"
    "ENCRYPTED_PDF"
    "input_pdf_to_img"
    "output_pdf_to_img"
    "input_split"
    "output_split"
    "input_custom_pages"
    "output_custom_pages"
) do (
    if not exist "%%~i" (
        mkdir "%%~i"
        echo Created directory: %%~i
    )
)

:: Function to install dependencies
:INSTALL_DEPENDENCIES
echo Installing dependencies...
pip install PyPDF2
pip install fitz
pip install img2pdf
echo Dependencies installed.

echo Setup complete.
pause

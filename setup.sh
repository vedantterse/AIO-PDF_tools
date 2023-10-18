#!/bin/bash

# This is a setup script for PDF Tools project

# Function to create directories
create_directories() {
    directories=(
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
    )

    for dir in "${directories[@]}"; do
        if [ ! -d "$dir" ]; then
            mkdir "$dir"
            echo "Created directory: $dir"
        fi
    done
}

# Function to install dependencies
install_dependencies() {
    echo "Installing dependencies..."

    pip install PyPDF2
    pip install fitz

    pip install img2pdf

    echo "Dependencies installed."
}

# Main setup routine
echo "Setting up PDF Tools..."

# Create directories
create_directories

# Install dependencies
install_dependencies

echo "Setup complete."

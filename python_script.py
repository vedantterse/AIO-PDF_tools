import os

print('\033[32mENTER the number according to the options!!\033[0m')
print('\033[33mthe INPUT directory of the tools is mentioned  place your files accordingly\033[0m ')
print('''\033[34mENTER:\033[0m

        \033[36m 1 for pdf merger\033[0m \033[33m[PDF_merger]\033[0m
         \033[36m2 for image to PDF\033[0m \033[33m[input_img2pdf]\033[0m
        \033[36m 3 for pdf encryption\033[0m \033[33m[PDF_ENCRYPT]\033[0m
         \033[36m4 for pdf to image\033[0m \033[33m[input_pdf_to_img]\033[0m
        \033[36m 5 for pdf splitter\033[0m \033[33m[input_split]\033[0m
        \033[36m 6 for pdf splitter(specific pages)\033[0m \033[33m[input_custom_pages]\033[0m''')
print('''when trying for the first time you may notice error.
first add the files according to the directories and then perform the actions''')


def create_directories():
    required_directories = ['PDF_Merger', 'Merged_pdf', 'input_img2pdf', 'img2pdf_output', 'PDF_ENCRYPT',
                            'ENCRYPTED_PDF', 'input_pdf_to_img', 'output_pdf_to_img', 'input_split',
                            'output_split', 'input_custom_pages', 'output_custom_pages']
    for directory in required_directories:
        if not os.path.exists(directory):
            os.makedirs(directory)


create_directories()
while True:
    exit_p = False  # Variable to check if "exit" is entered
    while True:
        w = input(
            '\033[36mEnter the value for the corresponding action (press \033[91m exit\033[0m \033[36mfor ending the '
            'program):\033[0m ')
        if w.lower() == 'exit':
            exit_p = True
            break
        if w in ['1', '2', '3', '4', '5', '6']:
            break
        else:
            print('Enter a valid value')

    if exit_p:  # Check if "exit" was entered
        break  # Break out of the outer while loop to end the program
    if w == "1":
        print("Place the pdf file(s) in the 'PDF_merger' directory and check out the output at 'merger_pdf' directory")


        def merge_pdfs(input_directory, output_directory, output_filename):
            try:
                # Create the input directory if it doesn't exist
                if not os.path.exists(input_directory):
                    os.makedirs(input_directory)

                # Create the output directory if it doesn't exist
                if not os.path.exists(output_directory):
                    os.makedirs(output_directory)

                # Get a list of all PDF files in the input directory
                input_pdf_files = [os.path.join(input_directory, file) for file in os.listdir(input_directory) if
                                   file.lower().endswith(".pdf")]

                if not input_pdf_files:
                    print("\033[31mNo PDF files found in the 'PDF_merger' directory.\033[0m")
                    return

                # Merge the PDFs
                pdf_merger = PyPDF2.PdfMerger()
                for pdf_file in input_pdf_files:
                    with open(pdf_file, "rb") as file:
                        pdf_merger.append(file)

                # Save the merged PDF to the output directory
                output_pdf_file = os.path.join(output_directory, output_filename)
                with open(output_pdf_file, "wb") as output_file:
                    pdf_merger.write(output_file)

                print(
                    f"{len(input_pdf_files)} PDF files have been merged and saved as '{output_filename}' in the 'merger_pdf' directory.")
                print("\033[42m Task Completed: PDF MERGED \033[0m")


            except Exception as e:
                print(f"\033[91mAn error occurred: {e}\033[0m")


        create_directories()

        if __name__ == "__main__":
            input_directory = "PDF_Merger"  # Input directory path
            output_directory = "Merged_pdf"  # Output directory path
            output_filename = "merged.pdf"  # Output merged PDF filename

            merge_pdfs(input_directory, output_directory, output_filename)

    elif w == '2':
        print("place the images in 'clutterpng directory and check the output at the 'img2pdf_output'")
        import img2pdf


        def images_to_pdf(input_images, output_pdf):
            try:
                with open(output_pdf, "wb") as pdf_file:
                    pdf_file.write(img2pdf.convert(input_images))

                print(f"{len(input_images)} images have been converted to PDF: '{output_pdf}'")
                print("\033[42m Task Completed: IMG TO PDF \033[0m")


            except Exception as e:
                print(f"\033[91mAn error occurred: {e}\033[0m")


        if __name__ == "__main__":
            input_directory = "input_img2pdf"  # Compulsory input directory path (Change if necessary)
            output_directory = "img2pdf_output"  # Output directory for the PDF (Change if necessary)
            output_pdf_file = os.path.join(output_directory, "img2pdf.pdf")

            # create the input directory if it doesn't exist
            if not os.path.exists(input_directory):
                os.makedirs(input_directory)
            # Create the output directory if it doesn't exist
            if not os.path.exists(output_directory):
                os.makedirs(output_directory)

            # Get a list of all image files in the input folder
            input_image_files = [os.path.join(input_directory, img) for img in os.listdir(input_directory) if
                                 img.lower().endswith((".jpg", ".jpeg", ".png", ".gif"))]

            if not input_image_files:
                print("\033[31mNo image files found in the 'Clutterpng' folder.\033[0m")
            else:
                images_to_pdf(input_image_files, output_pdf_file)

        create_directories()

    elif w == '3':
        print("Place the file in the 'PDF_ENCRYPT' directory and check the output in the 'ENCRYPTED_PDF' directory.")

        import os
        import PyPDF2


        # Code for encrypting the PDF file
        def encrypt_pdf(input_pdf, output_pdf, password):
            try:
                with open(input_pdf, "rb") as pdf_file:
                    pdf_reader = PyPDF2.PdfReader(pdf_file)
                    pdf_writer = PyPDF2.PdfWriter()

                    for page_number in range(len(pdf_reader.pages)):
                        page = pdf_reader.pages[page_number]
                        pdf_writer.add_page(page)

                    pdf_writer.encrypt(password)

                    with open(output_pdf, "wb") as output_file:
                        pdf_writer.write(output_file)

                print(f"PDF file '{input_pdf}' has been encrypted with a password and saved as '{output_pdf}'")
                print("\033[42m Task Completed: PDF Encryption \033[0m")


            except Exception as e:
                print(f"\033[91mAn error occurred: {e}\033[0m")


        create_directories()

        if __name__ == "__main__":
            while True:
                input_directory = "PDF_ENCRYPT"
                output_directory = "ENCRYPTED_PDF"
                password = input('\033[94mEnter the password you want to give to the file:\033[0m ')
                if password.lower() == "exit":
                    break

                input_pdf_file = input('Enter the name of the file you want to encrypt (or type "exit" for MainMenu): ')
                if input_pdf_file.lower() == "exit":
                    break

                if input_pdf_file.lower() == "exit":
                    break
                if not input_pdf_file.endswith(".pdf"):
                    input_pdf_file += ".pdf"
                input_pdf_path = os.path.join(input_directory, input_pdf_file)
                output_pdf_file = os.path.join(output_directory, f"{input_pdf_file}")
                # calling the function
                encrypt_pdf(input_pdf_path, output_pdf_file, password)


    elif w == '4':
        print("place the files at 'input_pdf_to_img' and check the output at 'output_pdf_to_img' ")
        import fitz


        def pdf_to_image(input_pdf, output_directory):
            try:
                # Create the output directory if it doesn't exist
                if not os.path.exists(output_directory):
                    os.makedirs(output_directory)

                # Convert PDF to images
                pdf_document = fitz.open(input_pdf)

                for page_number in range(pdf_document.page_count):
                    page = pdf_document.load_page(page_number)
                    image = page.get_pixmap(matrix=fitz.Matrix(2, 2))  # You can adjust the matrix for image size

                    image_path = f"{output_directory}/page_{page_number + 1}.JPG"
                    image.save(image_path)

                    print(
                        f"Page {page_number + 1} of {os.path.basename(input_pdf)} saved as {os.path.basename(image_path)}")

                pdf_document.close()



            except Exception as e:
                print(f"\033[91mAn error occurred: {e}\033[0m")


        if __name__ == "__main__":
            input_directory = "input_pdf_to_img"  # Input directory path
            output_directory = "output_pdf_to_img"  # Output directory path

            # Create the input directory if it doesn't exist
            if not os.path.exists(input_directory):
                os.makedirs(input_directory)

            # Create the output directory if it doesn't exist
            if not os.path.exists(output_directory):
                os.makedirs(output_directory)

            pdf_files = [file for file in os.listdir(input_directory) if file.lower().endswith(".pdf")]

            for input_pdf_file in pdf_files:
                pdf_to_image(os.path.join(input_directory, input_pdf_file), output_directory)

        create_directories()
    elif w == '5':
        print("place the pdf at 'input_split' and check the output at 'output_split'")

        ##pdf splitter###

        import os
        import PyPDF2


        def split_pdf(input_directory, input_pdf, output_directory, output_pdf, start_page, end_page):
            try:
                # Create the output directory if it doesn't exist
                if not os.path.exists(output_directory):
                    os.makedirs(output_directory)

                # Get the full paths of the input and output PDF files
                input_pdf_path = os.path.join(input_directory, input_pdf)
                output_pdf_path = os.path.join(output_directory, output_pdf)

                # Open the input PDF file
                with open(input_pdf_path, "rb") as pdf_file:
                    pdf_reader = PyPDF2.PdfReader(pdf_file)
                    pdf_writer = PyPDF2.PdfWriter()

                    # Perform page splitting and add pages to the new PDF
                    for page_num in range(start_page - 1, min(end_page, len(pdf_reader.pages))):
                        page = pdf_reader.pages[page_num]
                        pdf_writer.add_page(page)

                    # Save the new PDF to the output file
                    with open(output_pdf_path, "wb") as output_file:
                        pdf_writer.write(output_file)

                print(
                    f"PDF pages {start_page} to {end_page} from '{input_pdf}' have been split and saved as '{output_pdf}'.")
                print("\033[42m Task Completed: PDF SPLIT \033[0m")


            except Exception as e:
                print(f"\033[91mAn error occurred: {e}\033[0m")


        if __name__ == "__main__":
            while True:
                input_directory = "input_split"
                output_directory = "output_split"
                try:
                    input_pdf = input("Enter the name of the input PDF file : ")
                    if input_pdf.lower() == "exit":
                        break
                    output_pdf = input("Enter the desired name for the output PDF file: ")
                    if output_pdf.lower() == "exit":
                        break
                    start_page = int(input("Enter the starting page number: "))
                    if start_page == "exit":
                        break
                    end_page = int(input("Enter the ending page number: "))
                    if end_page == "exit":
                        break

                    if not input_pdf.endswith(".pdf"):
                        input_pdf += ".pdf"
                    if not output_pdf.endswith(".pdf"):
                        output_pdf += ".pdf"
                    split_pdf(input_directory, input_pdf, output_directory, output_pdf, start_page, end_page)
                except Exception as e:
                    print(f"\033[91mAn error occurred: {e}\033[0m")


    elif w == '6':
        print("Place the PDF in 'input_custom_pages' and check the output at 'output_custom_pages'")
        print("\033[34m(Use this to get the specific pages of pdf  )\033[0m ")

        import os
        import PyPDF2


        def split_pdf(input_directory, input_pdf, output_directory, output_pdf, pages_to_split):
            try:
                # Create the output directory if it doesn't exist
                if not os.path.exists(output_directory):
                    os.makedirs(output_directory)
                if not os.path.exists(input_directory):
                    os.makedirs(input_directory)

                # Get the full paths of the input and output PDF files
                input_pdf_path = os.path.join(input_directory, input_pdf)
                output_pdf_path = os.path.join(output_directory, output_pdf)

                # Convert the list of pages to split into integers
                pages_to_split = [int(page) for page in pages_to_split.split()]

                # Open the input PDF file
                with open(input_pdf_path, "rb") as pdf_file:
                    pdf_reader = PyPDF2.PdfReader(pdf_file)
                    pdf_writer = PyPDF2.PdfWriter()

                    # Perform page splitting and add specified pages to the new PDF
                    for page_num in pages_to_split:
                        if 1 <= page_num <= len(pdf_reader.pages):
                            page = pdf_reader.pages[page_num - 1]  # Adjust for 0-based index
                            pdf_writer.add_page(page)

                    # Save the new PDF to the output file
                    with open(output_pdf_path, "wb") as output_file:
                        pdf_writer.write(output_file)

                print(
                    f"PDF pages {', '.join(map(str, pages_to_split))} from '{input_pdf}' have been split and saved as '{output_pdf}'.")
                print("\033[42m Task Completed: PDF SPLIT \033[0m")

            except Exception as e:
                print(f"\033[91mAn error occurred: {e}\033[0m")


        if __name__ == "__main__":
            while True:
                input_directory = "input_custom_pages"
                output_directory = "output_custom_pages"
                try:
                    input_pdf = input("Enter the name of the input PDF file (or type 'exit' to quit): ")
                    if input_pdf.lower() == "exit":
                        break

                    output_pdf = input("Enter the desired name for the output PDF file: ")
                    if output_pdf.lower() == "exit":
                        break
                    pages_to_split = input("Enter the page numbers to split (e.g.:- 1 9 10 11): ")
                    if pages_to_split.lower() == "exit":
                        break

                    if not input_pdf.endswith(".pdf"):
                        input_pdf += ".pdf"
                    if not output_pdf.endswith(".pdf"):
                        output_pdf += ".pdf"
                    split_pdf(input_directory, input_pdf, output_directory, output_pdf, pages_to_split)
                except Exception as e:
                    print(f"\033[91mAn error occurred: {e}\033[0m")

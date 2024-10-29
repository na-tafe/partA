# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 20:25:18 2024

@author: nadifa aziza
student ID: 20027521


"""
"""

design, code, and test a program that uses  Python to manage PDF files. 
1.	Write a Python program that provides the ability to: 
1.1.	Merge at least two PDF files into one. Use list data structure with at least two PDF files. As an optional bonus you can create an empty list and ask for user input to populate empty list with user defined PDF files.
1.2.	Rotate a page in PDF file.
1.3.	Encrypt PDF file.
1.4.	Decrypt PDF file.
2.	Debug and test your program. You must write unit tests to test the functionality specified above. Screenshot your test results. 
3.	Comment your programs and upload your evidence in compressed format into the Blackboard assessment area.

note: pip install PyPDF2 and pip install reportlab

"""

import PyPDF2  # Import the PyPDF2 library for handling PDF files
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
"""
def create_sample_pdf(file_name, text):
    #Create a PDF file with specified text.
    c = canvas.Canvas(file_name, pagesize=letter)
    c.drawString(100, 750, text)
    c.save()

# List to store names of created PDFs
listofpdf = []

# Number of PDFs to create
num_pdfs = 2  # Change this to the desired number

for i in range(num_pdfs):
    file_name = f'sample{i+1}.pdf'  # Naming the PDFs
    text = f'This is sample PDF number {i+1}.'
    create_sample_pdf(file_name, text)
    listofpdf.append(file_name)  # Add the file name to the list

# Output the list of created PDF names
print(listofpdf)

"""

def merge_pdfs(pdf_list, output_file):
    #Merge multiple PDF files into a single PDF.
    pdf_writer = PyPDF2.PdfWriter()  # Create a PdfWriter object for output

    for pdf in pdf_list:
        with open(pdf, 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)  # Create a PdfReader object for the new merged file
            
            for page in range(len(pdf_reader.pages)):
                pdf_writer.add_page(pdf_reader.pages[page])  # Add each page to the writer

    with open(output_file, 'wb') as output_pdf:
        pdf_writer.write(output_pdf)  # Save the merged PDF

def rotate_page(pdf_file, page_number):
    #Rotate a specific page in a PDF file.
    with open(pdf_file, 'rb') as rotate_file:
        pdf_reader = PyPDF2.PdfReader(rotate_file)  # Read the PDF file directly
        pdf_writer = PyPDF2.PdfWriter()  # Create a PdfWriter object
        
        # Check if the specified page number is valid (1-indexed)
        if page_number < 1 or page_number > len(pdf_reader.pages):
            raise ValueError("Invalid page number.")

        # Access the specified page (convert 1-indexed to 0-indexed)
        page = pdf_reader.pages[page_number - 1]  # Access the specified page
        page.rotate(180)  # Rotate the page by 180 degrees

        # Add the rotated page to the writer
        pdf_writer.add_page(page)

        # Write output to a new file
        with open('NewRotate.pdf', 'wb') as result_pdf_file:
            pdf_writer.write(result_pdf_file)  # Save the rotated PDF

def encrypt_pdf(pdf_file, password):
    #Encrypt a PDF file with a password.
    
    #pdf_file (str): The path of the PDF file to encrypt.
    #password (str): The password to use for encryption.

    pdf_reader = PyPDF2.PdfReader(open(pdf_file, 'rb'))  # Read the PDF file using PdfReader from PyPDF2
    pdf_writer = PyPDF2.PdfWriter()  # Create a PdfWriter object

    for i in range(len(pdf_reader.pages)):
        pdf_writer.add_page(pdf_reader.pages[i])  # Add each page to the writer

    pdf_writer.encrypt(password)  # Encrypt the PDF with the provided password

    with open('encrypted_output.pdf', 'wb') as output_pdf:
        pdf_writer.write(output_pdf)  # Save the encrypted PDF

def decrypt_pdf(encrypted_pdf_file, password):
    #Decrypt an encrypted PDF file with the provided password.
    
    #Parameters:
    #    encrypted_pdf_file (str): The path of the encrypted PDF file.
    #    password (str): The password to decrypt the PDF.
    
    pdf_reader = PyPDF2.PdfReader(open(encrypted_pdf_file, 'rb'))  # Read the encrypted PDF file
    
    if pdf_reader.is_encrypted:
        pdf_reader.decrypt(password)  # Attempt to decrypt the PDF

    pdf_writer = PyPDF2.PdfWriter()  # Create a PdfWriter object

    for i in range(len(pdf_reader.pages)):
        pdf_writer.add_page(pdf_reader.pages[i])  # Add each page to the writer

    with open('decrypted_output.pdf', 'wb') as output_pdf:
        pdf_writer.write(output_pdf)  # Save the decrypted PDF




#Run the program

def main():
#asking to user for instruction
    while True:
        instruction=input("Enter funtion to run: 'M' to merge PDF, 'R' to rotate, 'E' to Encrypt, 'D' to decrypt, or 'X' to exit program: ")
        
        if instruction == 'X':
            print("You are exiting this program...")
            break
            
        if instruction == 'M':
            pdf_list = [] #put the file in the list
            
            while True:
                
                pdf_file = input("Enter the path of a PDF file to merge (type 'done' after inputting minimum of 2 pdf): ")
                if pdf_file.lower() == 'done':
                    if len(pdf_list) < 2: #if input is less than 2, error message will be prompted
                        raise ValueError("Please provide at least two PDF files to merge.")
                        continue #ask for more input, as it needs atleast 2
                    break
        
                pdf_list.append(pdf_file) #merge file in the list
            
            output_file = 'merged_output.pdf' #name the newly created merged file
            merge_pdfs(pdf_list, output_file)
            print(f"Merged {len(pdf_list)} PDF files into '{output_file}'.")
        
        elif instruction == 'R':
            # Rotate a page in a specific PDF
            rotate_file = input("Enter the PDF file path to rotate a page: ")
            page_number = int(input("Enter the page number to rotate: "))
            rotate_page(rotate_file, page_number)
            print(f"Rotated page {page_number} in '{rotate_file}' by 180 degrees.")
            
        elif instruction == 'E':
            # Encrypt a PDF file
            encrypt_file = input("Enter the PDF file path to encrypt: ")
            password = input("Enter a password to encrypt the PDF: ")
            encrypt_pdf(encrypt_file, password)
            print(f"Encrypted '{encrypt_file}' and saved as 'encrypted_output.pdf'.")
            
        elif instruction == 'D':
            # Decrypt a PDF file
            encrypted_pdf_file = input("Enter the encrypted PDF file path to decrypt: ")
            decrypt_password = input("Enter the password to decrypt the PDF: ")
            decrypt_pdf(encrypted_pdf_file, decrypt_password)
            print(f"Decrypted '{encrypted_pdf_file}' and saved as 'decrypted_output.pdf'.")
            
        else:
            print("invalid input")
            continue





if __name__ == '__main__':
    main()

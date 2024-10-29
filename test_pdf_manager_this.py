# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 21:54:32 2024

@author: 61420
"""
import unittest  # For creating tests
import PyPDF2  # For PDF handling
import os  # For file system operations
from reportlab.lib.pagesizes import letter  # For letter size from reportlab
from reportlab.pdfgen import canvas  # For creating PDFs
from pdf_manager import merge_pdfs, rotate_page, encrypt_pdf, decrypt_pdf  # Import functions from the main program


class TestPdfManager(unittest.TestCase):
    def setUp(self):
        """Set up test resources for each test."""
        # Setup file names
        self.pdf_file1 = 'test1.pdf'
        self.pdf_file2 = 'test2.pdf'
        self.merged_pdf_file = 'merged_output.pdf'
        self.rotate_pdf_file = 'NewRotate.pdf'
        self.encrypted_pdf_file = 'encrypted_output.pdf'
        self.decrypted_pdf_file = 'decrypted_output.pdf'
    
        # Create simple test PDFs with text
        sample_text = 'This is sample text for create sample pdf'
        self.create_sample_pdf(self.pdf_file1, sample_text)
        self.create_sample_pdf(self.pdf_file2, sample_text)

    def tearDown(self):
        """Remove files created during tests."""
        for file in [
            self.pdf_file1, self.pdf_file2, self.merged_pdf_file,
            self.rotate_pdf_file, self.encrypted_pdf_file, self.decrypted_pdf_file
        ]:
            try:
                if os.path.exists(file):  # If file exists, remove it
                    os.remove(file)
            except PermissionError as e:  # Handle file removal errors
                print(f"Error removing file {file}: {e}")

    def create_sample_pdf(self, file_name, text):
        #Create a simple PDF file with text.
        c = canvas.Canvas(file_name, pagesize=letter)  # Create a PDF canvas
        c.drawString(100, 750, text)  # Add text to the PDF
        c.save()  # Save the PDF file
        
        
    def test_merge_pdfs(self):
        """Test merging multiple PDFs."""
        merge_pdfs([self.pdf_file1, self.pdf_file2], self.merged_pdf_file)  # Merge two PDFs
        self.assertTrue(os.path.exists(self.merged_pdf_file))  # Assert merged file exists

        with open(self.merged_pdf_file, 'rb') as merged_file:  # Open the merged file
            merged_reader = PyPDF2.PdfReader(merged_file)
            self.assertEqual(len(merged_reader.pages), 2)  # Expecting 2 pages from each sample file

    def test_rotate_page(self):
        """Test rotating a page in a PDF."""
        rotate_page(self.pdf_file1, 1)  # Rotate the first page
        self.assertTrue(os.path.exists(self.rotate_pdf_file))  # Check if the rotated file exists

    def test_encrypt_pdf(self):
        """Test encrypting a PDF."""
        encrypt_pdf(self.pdf_file1, 'password')  # Encrypt the file with a password
        self.assertTrue(os.path.exists(self.encrypted_pdf_file))  # Assert encrypted file exists

    def test_decrypt_pdf(self):
        """Test decrypting an encrypted PDF."""
        encrypt_pdf(self.pdf_file1, 'password')  # File needs to be encrypted first
        decrypt_pdf(self.encrypted_pdf_file, 'password')  # Decrypting the file using the password
        self.assertTrue(os.path.exists(self.decrypted_pdf_file))  # Assert decrypted file exists

if __name__ == '__main__':
    unittest.main()  # Run the unit tests




"""
# update 1
#import necessay modules used in the program testing
import unittest #for creating tests
import PyPDF2 # for pdf handling
import os #for file system operation
from reportlab.lib.pagesizes import letter # for letter size from report lab. pip install reportlab
from reportlab.pdfgen import canvas #import canvas fro creating pdf
from pdf_manager import merge_pdfs, rotate_page, encrypt_pdf, decrypt_pdf #import functions from main program


class TestPdfManager(unittest.TestCase):
    def setUp(self):
        #Set up test resources for each test.
        # Setup file names
        self.pdf_file1 = 'test1.pdf'
        self.pdf_file2 = 'test2.pdf'
        self.merged_pdf_file = 'merged_output.pdf'
        self.rotate_pdf_file = 'NewRotate.pdf'
        self.encrypted_pdf_file = 'encrypted_output.pdf'
        self.decrypted_pdf_file = 'decrypted_output.pdf'
    
        # Create simple test PDFs with text
        self.create_sample_pdf(self.pdf_file1, 'Sample PDF 1')
        self.create_sample_pdf(self.pdf_file2, 'Sample PDF 2')

    def tearDown(self):
        #Remove files created during tests.
        for file in [
            self.pdf_file1, self.pdf_file2, self.merged_pdf_file,
            self.rotate_pdf_file, self.encrypted_pdf_file, self.decrypted_pdf_file
        ]:
            try:
                if os.path.exists(file):  # If file exists, remove it
                    os.remove(file)
            except PermissionError as e:  # Handle file removal errors
                print(f"Error removing file {file}: {e}")

    def create_sample_pdf(self, file_name, text):
        #Create a simple PDF file with text.
        c = canvas.Canvas(file_name, pagesize=letter)  # Create a PDF canvas
        c.drawString(100, 750, text)  # Add text to the PDF
        c.save()  # Save the PDF file

    def test_merge_pdfs(self):
        #Test merging multiple PDFs.
        merge_pdfs([self.pdf_file1, self.pdf_file2], self.merged_pdf_file)  # Merge two PDFs
        self.assertTrue(os.path.exists(self.merged_pdf_file))  # Assert merged file exists

        with open(self.merged_pdf_file, 'rb') as merged_file:  # Open the merged file
            merged_reader = PyPDF2.PdfReader(merged_file)
            self.assertEqual(len(merged_reader.pages), 2)  # Expecting 2 pages from each sample file

    def test_rotate_page(self):
        #Test rotating a page in a PDF.
        rotate_page(self.pdf_file1, 1)  # Rotate the first page
        self.assertTrue(os.path.exists(self.rotate_pdf_file))  # Check if the rotated file exists

    def test_encrypt_pdf(self):
        #Test encrypting a PDF.
        encrypt_pdf(self.pdf_file1, 'password')  # Encrypt the file with a password
        self.assertTrue(os.path.exists(self.encrypted_pdf_file))  # Assert encrypted file exists

    def test_decrypt_pdf(self):
        #Test decrypting an encrypted PDF.
        encrypt_pdf(self.pdf_file1, 'password')  # File needs to be encrypted first
        decrypt_pdf(self.encrypted_pdf_file, 'password')  # Decrypting the file using the password
        self.assertTrue(os.path.exists(self.decrypted_pdf_file))  # Assert decrypted file exists

if __name__ == '__main__':
    unittest.main()  # Run the unit tests



"""


"""
#import necessay modules used in the program testing
import unittest #for creating tests
import PyPDF2 # for pdf handling
import os #for file system operation
from reportlab.lib.pagesizes import letter # for letter size from report lab. pip install reportlab
from reportlab.pdfgen import canvas #import canvas fro creating pdf
from pdf_manager import merge_pdfs, rotate_page, encrypt_pdf, decrypt_pdf #import functions from main program



class TestPdfManager(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        #setup test resources for the test
        cls.pdf_file1 = 'test1.pdf' 
        cls.pdf_file2 = 'test2.pdf'
        cls.merged_pdf_file = 'merged_output.pdf'
        cls.rotate_pdf_file = 'NewRotate.pdf'
        cls.encrypted_pdf_file = 'encrypted_output.pdf'
        cls.decrypted_pdf_file = 'decrypted_output.pdf'
    
        # Create simple test PDFs with text
        cls.create_sample_pdf(cls.pdf_file1, 'Sample PDF 1')
        cls.create_sample_pdf(cls.pdf_file2, 'Sample PDF 2')

    @classmethod
    def tearDownClass(cls):
        # Remove files created during tests
        for file in [
            cls.pdf_file1, cls.pdf_file2, cls.merged_pdf_file,
            cls.rotate_pdf_file, cls.encrypted_pdf_file, cls.decrypted_pdf_file
        ]:
            try:
                if os.path.exists(file): #if file exist, the it will be removed
                    os.remove(file)
            except PermissionError as e: #if file does nit exist, error
                print(f"Error removing file {file}: {e}")

    @staticmethod
    def create_sample_pdf(file_name, text):
        #Create a simple PDF file with text.#
        c = canvas.Canvas(file_name, pagesize=letter)
        c.drawString(100, 750, text)
        c.save()

    def test_merge_pdfs(self):
        merge_pdfs([self.pdf_file1, self.pdf_file2], self.merged_pdf_file) #merge two pdfs
        self.assertTrue(os.path.exists(self.merged_pdf_file)) #assert merged file exist

        with open(self.merged_pdf_file, 'rb') as merged_file: # to open merged file
            merged_reader = PyPDF2.PdfReader(merged_file)
            self.assertEqual(len(merged_reader.pages), 2)  # Expecting 2 pages from each sample file in the merged pdf

    def test_rotate_page(self):
        #Test rotating a page in a PDF.
        rotate_page(self.pdf_file1, 1) # test rotate first page
        self.assertTrue(os.path.exists(self.rotate_pdf_file)) #check if the rotated file exist

    def test_encrypt_pdf(self):
        #Test encrypting a PDF.
        encrypt_pdf(self.pdf_file1, 'password') # encrypting the file with password
        self.assertTrue(os.path.exists(self.encrypted_pdf_file)) #encrypted file exist

    def test_decrypt_pdf(self):
        #Test decrypting an encrypted PDF.
        encrypt_pdf(self.pdf_file1, 'password') #file needs to be encrypted first
        decrypt_pdf(self.encrypted_pdf_file, 'password') # decrypting file using the password
        self.assertTrue(os.path.exists(self.decrypted_pdf_file)) #asser decrypted file exist

if __name__ == '__main__':
    unittest.main()
    """

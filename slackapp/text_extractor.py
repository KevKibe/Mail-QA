import os
import PyPDF2
from PyPDF2 import PdfReader
import docx
from dotenv import load_dotenv


load_dotenv()

class TextExtractor:
    """A class to extract text from files of different formats."""

    def __init__(self, file_path):
        self.file_path = file_path
        self.file_extension = os.path.splitext(file_path)[1]
        self.text = None

    def check_format(self):
        """Checks the format of the file.

        Returns:
          True if the file is of a supported format, False otherwise.
        """

        supported_formats = [".pdf", ".txt", ".docx"]
        if self.file_extension not in supported_formats:
            return False
        else:
            return True

    def extract_text(self):
        """Extracts the text from the file.

        Returns:
          A string containing the text from the file, or None if the file is not of a supported format.
        """

        if not self.check_format():
            return None

        if self.file_extension == ".pdf":
            self.text = self.extract_text_from_pdf()
        elif self.file_extension == ".txt":
            self.text = self.extract_text_from_txt()
        elif self.file_extension == ".docx":
            self.text = self.extract_text_from_docx()

        return self.text

    def extract_text_from_pdf(self):
        """Extracts text from a PDF file.

        Returns:
          A string containing the text from the PDF file.
        """

        pdf_file = PdfReader(self.file_path)
        text = ""
        for page in pdf_file.pages:
            text += page.extract_text()
        return text

    def extract_text_from_txt(self):
        """Extracts text from a TXT file.

        Returns:
          A string containing the text from the TXT file.
        """

        with open(self.file_path, "r") as f:
            text = f.read()
        return text

    def extract_text_from_docx(self):
        """Extracts text from a DOCX file.

        Returns:
          A string containing the text from the DOCX file.
        """

        doc = docx.Document(self.file_path)
        text = ""
        for paragraph in doc.paragraphs:
            text += paragraph.text
        return text
    
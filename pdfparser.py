from base import BaseClass
import PyPDF2

class Parser(BaseClass):

    def __init__(self, file):
        
        super().__init__(file)
    
    def parser(self):
        combined_text = ""

        pdf_reader = PyPDF2.PdfReader(self.file)
        num_pages = len(pdf_reader.pages)

        for page_num in range(num_pages):
            page = pdf_reader.pages[page_num]
            text = page.extract_text()
        
            if text:
                combined_text += text + "\n"
        
        self.text = combined_text

        return
    
# pdf_path = 'cv.pdf'
# pdf_parser = Parser(pdf_path)
# pdf_parser.parser()
# print(pdf_parser.text)
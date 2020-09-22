import itertools

import PyPDF2


class PdfExtractor:
    def __init__(self, input_file, output_file):
        self._input_file = input_file
        self._output_file = output_file
        self._pdf_reader = PyPDF2.PdfFileReader(input_file)
        self._pdf_writer = PyPDF2.PdfFileWriter()
        self._pages = []

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._input_file.close()
        self._output_file.close()

    def collect_pages(*pages, ranges=None):
        if pages is None:

        if ranges is None:
            ranges = []
        pages_numbers = set(itertools.chain(pages, *ranges))
        
        if not pages_numbers:
            raise ValueError

        self._pages = [self._pdf_reader.getPage(page) for page in pages_numbers]

    def create_document(output_file):
        for page in self._pages:
            self._pdf_writer.addPage(page)
        self._pdf_writer.write(self._output_file)


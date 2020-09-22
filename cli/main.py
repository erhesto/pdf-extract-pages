import argparse
from ..pdfextractor import PdfExtractor


def text_range(value):
    MAX_RANGE = 10000
    start, end = value.split('-')

    if start.isnumeric():
        start = int(start)
    if end.isnumeric():
        end = int(end) + 1
    else:
        end = self.MAX_RANGE
    
    return range(start, end)


def main():
    parser = argparse.ArgumentParser(description="Get files from PDF")
    parser.add_argument("input", type=argparse.FileType('rb'))
    parser.add_argument("output", type=argparse.FileType('wb'))
    parser.add_argument("--pages", type=int, nargs='+', default=[], help="Numbers of pages")
    parser.add_argument("--ranges", default=[], nargs="+", type=text_range, required=False)

    args = parser.parse_args()
    with PdfExtractor(args.input, args.output) as pdf_extractor:
        number_of_pages = pdf_extractor.collect_pages(*args.pages, ranges=args.ranges)
        pdf_extractor.create_document()



if __name__ == "__main__":
    main()

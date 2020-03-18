import PyPDF2
import argparse
import itertools


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


def get_pages(pdf_reader, *pages_numbers):
    return [pdf_reader.getPage(page) for page in pages_numbers]


def create_document(pdf_writer, output_file, pages):
    for page in pages:
        pdf_writer.addPage(page)
    pdf_writer.write(output_file)


def main():
    parser = argparse.ArgumentParser(description="Get files from PDF")
    parser.add_argument("input", type=argparse.FileType('rb'))
    parser.add_argument("output", type=argparse.FileType('wb'))
    parser.add_argument("--pages", type=int, nargs='+', default=[], help="Numbers of pages")
    parser.add_argument("--ranges", default=[], nargs="+", type=text_range, required=False)

    args = parser.parse_args()
    pages_numbers = set(itertools.chain(args.pages, *args.ranges))
    
    pdf_reader = PyPDF2.PdfFileReader(args.input)
    pdf_writer = PyPDF2.PdfFileWriter()
    
    pages = get_pages(pdf_reader, *pages_numbers)
    
    if not pages:
        raise ValueError("There are not pages to extract!")

    create_document(pdf_writer, args.output, pages)
    print(f"Done, wrote {len(pages)} pages to {args.output.name}")
    args.output.close()
    args.input.close()


if __name__ == "__main__":
    main()

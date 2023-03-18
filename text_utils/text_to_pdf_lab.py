import io
import sys

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

def text_to_pdf_lab(filename:str):
    # Open the text file for reading
    with open(filename, 'r') as file:
        text = file.read()

    # Split the text into lines
    lines = text.splitlines()

    # Create a buffer for the PDF
    pdf_buffer = io.BytesIO()

    # Create a canvas object to write the PDF to
    pdf_canvas = canvas.Canvas(pdf_buffer, pagesize=letter)

    # Set the position of the first line
    x, y = 100, 700

    # Write each line to the canvas
    for line in lines:
        pdf_canvas.drawString(x, y, line)
        y -= 20

    # Save the PDF to a file
    pdf_canvas.save()

    # save the pdf with name .pdf
    dot_pos = filename.rfind('.')
    fname = filename if (dot_pos < 0) else filename[:dot_pos]

    fname += '_2.pdf'
    with open(fname, 'wb') as file:
        file.write(pdf_buffer.getvalue())

    return fname


def main():
    """
    Converts a text file to a PDF file.

    Usage:
    - python text_to_pdf.py <file.txt>
    """
    argcount = len(sys.argv)
    if argcount == 2:
        filename = sys.argv[1]
        pdf_name = text_to_pdf_lab(filename)
        print(f'Text file "{filename}" converted to PDF: "{pdf_name}"')
    else:
        print("\nUsage: python text_to_pdf_lab.py <file.txt>")
        
if __name__ == '__main__':
    main()
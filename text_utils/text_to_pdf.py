""" 
    Utility app to convert txt file to PDF using fpdf library
    Author  : Orhan Çavuş
    Twitter : @orhanrcavus
    Date    : 13.11.2021
    usage   : python text_to_pdf.py file.txt
"""
import sys
import platform
from fpdf import FPDF

def text_as_list(text:str, chars_per_line:int=70) -> list:
    """
    Splits a given string into a list of strings, with each string having at most 
    the given number of characters.

    Args:
    - text (str): The input text to split into lines.
    - chars_per_line (int): The maximum number of characters per line. Default is 70.

    Returns:
    - A list of strings where each string has at most `chars_per_line` characters.
    """    
    text_len = len(text)
    result = []    
    
    # Used early return to reduce nested indentation levels.
    if text_len <= chars_per_line:
        result.append(text)
        return result	
    
    lines = text_len // chars_per_line

    for i in range(lines):
        from_index = i * chars_per_line
        to_index = (i+1) * chars_per_line
        result.append(text[from_index:to_index])

    last_pos = (text_len - lines * chars_per_line)
    if last_pos > 0: 
        result.append(text[to_index:])

    return result


def text_file_to_pdf(filename):
    """Reads 'filename' and writes to PDF with 'CourierNewBold TTF' font  """
    # save FPDF() class into
    # a variable pdf
    pdf = FPDF()

    # Add a page
    pdf.add_page()

    system_name = platform.system()
    if system_name == "Darwin":
        # macos true type font directory, for other OS sould be changed
        courier_ttf=r"/Library/Fonts/Courier New Bold.ttf"
    elif system_name == "Windows":
        # windows true type fonts dir
        courier_ttf=r"C:\Windows\Fonts\Courbd.ttf"
    else:
        raise Exception("Linux version not implemented ..")

    # set style and size of font
    pdf.add_font('CourierNewBold', '', courier_ttf, uni = True)
    pdf.set_font("CourierNewBold", size = 12)

    with open(filename, 'r', encoding="utf-8") as f:
        for x in f:
            # remove carriage return from the end of the line 
            # text_line = x.rstrip()
            text_line_list = text_as_list(x.rstrip())
            for text_line in text_line_list:
                pdf.cell(200, 5, txt = text_line, ln = 1, align = 'L')		

    # save the pdf with name .pdf
    dot_pos = filename.rfind('.')
    fname = filename if (dot_pos < 0) else filename[:dot_pos]

    fname += '.pdf'
    pdf.output(fname)

    # return pdf file name
    return fname

if __name__ == '__main__':
    """Text file to .pdf  """
    argcount = len(sys.argv)
    if argcount > 1:
        filename = sys.argv[1]
        fname = text_file_to_pdf(filename)
        print(f'Text file to pdf conversion : {fname}')		
    elif argcount == 1:
        print("\nusage: python text_to_pdf.py file.txt")
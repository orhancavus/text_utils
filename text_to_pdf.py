""" 
	Utility app to convert txt file to PDF using fpdf library
	Author  : Orhan Çavuş
	Twitter : @orhanrcavus
	Date    : 13.11.2021
"""
import sys
from fpdf import FPDF

def text_file_to_pdf(filename):
	"""Reads a text filename and writes to PDF with CourierNewBold TTF font  """
	# save FPDF() class into
	# a variable pdf
	pdf = FPDF()

	# Add a page
	pdf.add_page()

	# set style and size of font
	# macos true type font directory
	pdf.add_font('CourierNewBold', '', r"/Library/Fonts/Courier New Bold.ttf", uni=True)
	pdf.set_font("CourierNewBold", size = 12)

	with open(filename, 'r') as f:
		for x in f:
			# remove carriage return right
			text_line = x.rstrip()
			# TODO if line length greater than XX wrap string ..
			pdf.cell(200, 10, txt = text_line, ln = 1, align = 'L')		

	# save the pdf with name .pdf
	dot_pos = filename.rfind('.')
	if dot_pos > 1:
		fname = filename[:dot_pos] 
	else:
		fname = filename

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
		print("usage: text_to_pdf file.txt")
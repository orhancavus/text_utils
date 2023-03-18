import pytest
from text_to_pdf import text_file_to_pdf

def test_text_to_pdf():
    assert text_file_to_pdf("README.txt") == "README.pdf"

@pytest.mark.parametrize("filename,output_filename",[("README.txt","README.pdf")])
def test_with_params_text_pdf(filename, output_filename ):
    assert text_file_to_pdf(filename) == output_filename
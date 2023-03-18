import pytest
import platform

from text_utils.text_to_pdf import text_file_to_pdf

sample_file_name="Sample_file.txt"
sample_outpout_file_name="Sample_file.pdf"

def test_text_to_pdf():
    assert text_file_to_pdf(sample_file_name) == sample_outpout_file_name

@pytest.mark.parametrize("filename,output_filename",[(sample_file_name, sample_outpout_file_name)])
def test_with_params_text_pdf(filename, output_filename ):
    assert text_file_to_pdf(filename) == output_filename

def test_linux_error_is_raised():
    system_name=platform.system()
    if system_name == "Linux":
        with pytest.raises(Exception):
            text_file_to_pdf(sample_file_name)  

# Python basic pdf utility applications that converts text file to pdf

    Author  : Orhan Çavuş
    Twitter : @orhanrcavus
    Date    : 13.11.2021
    Modified: 18.03.2023
    usage   : python text_to_pdf.py file.txt

## text_to_pdf.py - Utility app to convert text file to PDF using fpdf library

    requires : pip install -r requirements.txt 
    link     : https://pypi.org/project/fpdf/ 

### Macos true type font directory, for other OSes sould be changed

    courier_ttf=r"/Library/Fonts/Courier New Bold.ttf" 

    notes    :  
    - Font size      : 12  
    - Font Name      : CourierNewBold    
    - Macos font dir : /Library/Fonts/Courier New Bold.ttf  

### Windows true type font directory

    courier_ttf=r"C:\Windows\Fonts\Courbd.ttf"
    https://learn.microsoft.com/en-us/typography/fonts/windows_11_font_list

### Test

[Calmcode.io - pytest](https://calmcode.io/pytest/introduction.html)

    ```bash
    pytest test_text_to_pdf.py
    pytest --verbose
    pytest --verbose .\test_text_to_pdf.py::test_text_to_pdf
    pytest -vv tests/test_text_to_pdf.py::test_text_to_list

    python setup.py develop

    pytest
    ```

### Package test

    ```bash
    ❯ python
    Python 3.10.4 | packaged by conda-forge | (main, Mar 30 2022, 08:38:02) [MSC v.1916 64 bit (AMD64)] on win32
    Type "help", "copyright", "credits" or "license" for more information.
    >>> from text_utils.text_to_pdf import text_file_to_pdf
    >>> text_file_to_pdf("README.md")
    'README.pdf'
    >>>

    >>> help(text_file_to_pdf)
    Help on function text_file_to_pdf in module text_utils.text_to_pdf:

    text_file_to_pdf(filename)
        Reads 'filename' and writes to PDF with 'CourierNewBold TTF' font

    >>>
    ```

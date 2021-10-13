import re
import fitz  # pip install PyMuPDF
# a regular expression of URLs
url_regex = r"([-a-zA-Z0-9])"
# extract raw text from pdf
file = "CauseListFile.pdf"
# file = "1810.04805.pdf"
# open the PDF file
with fitz.open(file) as pdf:
    text = ""
    for page in pdf:
        # extract text of each PDF page
        text += page.getText()
        urls = []
        # extract all urls using the regular expression

        for match in re.finditer(url_regex, text):
            url = match.group()
            print("[+] URL Found:", text)
            urls.append(url)
        print("[*] Total URLs extracted:", len(urls))

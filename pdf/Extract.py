from os import name
import requests
from bs4 import BeautifulSoup
from urllib.request import unquote

# target URL
url = 'https://delhihighcourt.nic.in/causelist_NIC_PDF.asp'

# make HTTP GET request to the target URL

response = requests.get(url)

# parse content
content = BeautifulSoup(response.text, 'lxml')


all_urls = content.find_all('a')
name = "3LZM6YNU0EL"
# loop over all URLs
for url in all_urls:
 
    try:
    

        if '.PDF' and name  in url['href']:
         
            pdf_url = ''

            # append base URL if no 'https' available in URL
            if 'https' not in url['href']:
                pdf_url = 'https://delhihighcourt.nic.in/' + url['href']

            # otherwise use bare URL
            else:
                pdf_url = url['href']

           
            
            pdf_response = requests.get(pdf_url)
            print(pdf_response.url)

           
            
            # extract  PDF file name
            filename = unquote(pdf_response.url).split(
                '/')[-1]
            
            # write PDF to local file
            with open(filename, 'wb') as f:
               
                f.write(pdf_response.content)

  
    except:
        pass

import requests
from bs4 import BeautifulSoup

import csv
# target URL
url = 'https://coreyms.com'

# make HTTP GET request to the target URL

response = requests.get(url).content

soup = BeautifulSoup(response, 'lxml')
# print(soup.prettify)
# exit()

csv_file=open('scraped.csv','w')
csv_write=csv.writer(csv_file)

csv_write.writerow(['headline','summary','youtube'])

for article in soup.find_all('article'):
        
    #print(article.prettify)

    headline= article.a.text
    print(headline)

    summary = article.find('div', class_='entry-content').p.text
    print(summary)

    try:

        video=article.find('iframe',class_='youtube-player')['src']
        print(video)
        video_id=video.split('/')[4].split('?')[0]
        #print(video_id)

        yt_link=f'https://youtube.com/watch?v={video_id}'
        print(yt_link)
    except:
        yt_link=None
    print(yt_link)

    print()
    csv_write.writerow([headline,summary,yt_link])

csv_file.close()

#----------------------------------basic methods --------------------------------------------
# # parse content
# Html_content = response.content

# #print(Html_content)

# soup=BeautifulSoup(Html_content,'html.parser')

# #print(soup.prettify)

# title =soup.title
# #print(title)

# paras=soup.find_all('p')

# #print(paras)

# anchor = soup.find_all('a')

# #print(anchor)
# #to get all url link of website

# all_links=set()

# for link in anchor:
#     if(link.get('href')!='#'):
#         linktext = "https://coreyms.com" +link.get('href')
#         all_links.add(linktext)
# #print(all_links)

# text=soup.get_text()
# #print(text)




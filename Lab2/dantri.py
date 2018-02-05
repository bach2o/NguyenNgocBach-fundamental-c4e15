from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel

url = "http://dantri.com.vn"
output_file_name = "new.xlsx"
# 1. Download website
# 1.1 Open a connection
conn = urlopen(url)
# 1.2 Read
data = conn.read() # dạng bytes

# 1.3 Decode
html_content = data.decode("utf8") # hoặc chơi hẳn 3 bước trong 1: html_content = urlopen(url).read.decode("utf-8")
html_file = open("dantri.html", "wb") # write
html_file.write(data)
html_file.close()
# print(html_content)

# 2. Extract Region of interest (ROI)

# 3. Extract News

# 4. Cteate a soup
soup = BeautifulSoup(html_content, 'html.parser') # Dạng khác xml
# print(soup.prettify)
ul = soup.find('ul', "ul1 ulnew") # class id
# print(ul.prettify)
li_list = ul.find_all('li') # Nó sẽ tìm ra một list
# for li in li_list:
#     li = li.prettify()
#     print(li)
#     print("*****")
news_list = []
for lis in li_list:
    h4 = lis.h4
    a = h4.a
    href = url + a['href']
    title = a.string
    news = {
        'Title': title,
        'Link': href
    }
    news_list.append(news)
    # print(href)
    # print(title)

    # print('*')
print(news_list, end=' ')

pyexcel.save_as(records = news_list, dest_file_name = 'Dantri.xlsx')

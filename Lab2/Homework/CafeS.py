
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
output_file_name = "cafe.xlsx"

url = "http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2017/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn"  # change to whatever your url is
conn = urlopen(url)
data = conn.read()

html_content = data.decode("utf8") # hoặc chơi hẳn 3 bước trong 1: html_content = urlopen(url).read.decode("utf-8")
html_file = open("cafe.html", "wb") # write
html_file.write(data)
html_file.close()

# Tìm ROI
soup = BeautifulSoup(html_content, 'html.parser') # Dạng khác xml
table1 = soup.find('table', id = 'tblGridData')
table2 = soup.find('table',id = 'tableContent')
td_list = table1.find_all('td')
# column_heads = [i.text.encode('utf-8') for i in rows[0].findAll('th')[1:]]
data_list = []
for td in td_list:
    td = td_list.string
    data_list.append(td)
print(data_list)
# for index, value  in enumerate(td_list):
#     number = value.string
#     data= {
#             'Field': number
#     }
#     if number is not None:
#         data_list.append(data)

# #3. Extract news
#install pyexcel
import pyexcel

pyexcel.save_as(records= nicedatalist, dest_file_name= output_file_name)

from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
from collections import OrderedDict

output_file_name = "cafe.xlsx"
url = "http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2017/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn"  # change to whatever your url is
html_content = urlopen(url).read().decode("utf8") # chơi hẳn 3 bước trong 1: html_content = urlopen(url).read.decode("utf-8")

# Tìm ROI
soup = BeautifulSoup(html_content,'html.parser')

div0 = soup.find('div', style = 'background-color:#e1e1e1;overflow:hidden', id = 'divTableHeader')
table0 = div0.find('table', id = 'tblGridData')
tr_list_0 = table0.find('tr')
td_list_0 = tr_list_0.find_all('td')
x1 = td_list_0[1].string # td_list_0[0] không có string, đòi hỏi vào sâu hơn nữa
x2 = td_list_0[2].string
x3 = td_list_0[3].string
x4 = td_list_0[4].string

div = soup.find('div', style = 'overflow:hidden;width:100%;border-bottom:solid 1px #cecece;')
table = div.find('table', id = 'tableContent')
tr_list = table.find_all('tr', class_= ['r_item', 'r_item_a'])

data_list = []
for tr in tr_list:
    td_list = tr.find_all('td')
    cac_khoan_thu = td_list[0].string
    quy4_16 = td_list[1].string
    quy1_17 = td_list[2].string
    quy2_17 = td_list[3].string
    quy3_17 = td_list[4].string
    data = {
        ' ': cac_khoan_thu,
        x1: quy4_16,
        x2: quy1_17,
        x3: quy2_17,
        x4: quy3_17
    }
    rearange_data = OrderedDict(data.items())
    data_list.append(rearange_data)

pyexcel.save_as(records = data_list, dest_file_name = output_file_name)

from urllib.request import urlopen
from bs4 import BeautifulSoup
from youtube_dl import YoutubeDL
import pyexcel

url = "https://www.apple.com/itunes/charts/songs/"
output_file_name = "TopSongs.xlsx"
conn = urlopen(url)
data = conn.read()

html_content = data.decode("utf8") # hoặc chơi hẳn 3 bước trong 1: html_content = urlopen(url).read.decode("utf-8")
html_file = open("iTunes_top_songs.html", "wb") # write
html_file.write(data)
html_file.close()

# Tìm ROI
soup = BeautifulSoup(html_content, 'html.parser') # Dạng khác xml
section = soup.find('section', class_='section chart-grid')
div = section.find('div', class_="section-content") # class id
ul = div.find('ul')
li_list = ul.find_all('li') # Nó sẽ tìm ra một list

# Tạo danh sách bài hát - ca sĩ và lưu vào file excel
Song_list = []
for lis in li_list:
    names = lis.h3.string
    artists = lis.h4.string
    Names_Artists = {
        'Names': names,
        'Artists': artists
    }
    Song_list.append(Names_Artists)
pyexcel.save_as(records = Song_list, dest_file_name = output_file_name)

# Setup cho youtubedl
dl = YoutubeDL()
options = {
    'default_search': 'ytsearch',
    'max_downloads': 1,
    'format': 'bestaudio/audio'
}

# Vòng lặp tải nhạc
for song in Song_list:
    dl = YoutubeDL(options)
    search = song['Names'] + ' ' + song['Artists']
    dl.download([search])

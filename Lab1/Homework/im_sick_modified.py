from gmail import GMail, Message
from random import choice

import datetime
now = datetime.datetime.now()
current_time = datetime.time(now.hour, now.minute)

import winsound
duration = 1000  # millisecond
freq = 440  # Hz

# Creating the message
html_template = '''
<h1 style="text-align: center;"><span style="background-color: #ff6600;"><strong>Th&ocirc;ng b&aacute;o</strong></span></h1>
<p><strong>V&agrave;o ng&agrave;y 30 th&aacute;ng 1 năm 2018, <span style="color: #ff00ff;">kebopdaithanthanh</span> đ&atilde; gặp một tai nạn bất ngờ tr&ecirc;n đường đi về nh&agrave;.</strong></p>
<p><strong>Hiện giờ <span style="color: #ff00ff;">kebopdaithanthanh</span> đ&atilde; bị {{sickness}} n&ecirc;n kh&ocirc;ng thể c&oacute; mặt đ&uacute;ng giờ. Xin ch&acirc;n th&agrave;nh xin lỗi!</strong></p></p>
'''
sickness_list = ['kiết lị', 'tiêu chảy', 'sỏi thận', 'thoái hóa đốt sống cổ', 'trĩ', 'sốt virus', 'gãy chân', 'gãy tay', 'đau đầu', 'liệt nửa người', 'liệt toàn thân', 'bại não', 'hôi nách']
sickness = choice(sickness_list)
html_content = html_template.replace('{{sickness}}',sickness)
gmail = GMail('kebopdaithanthanh@gmail.com','bach2o123')
msg = Message('Như bạn có thể thấy, đây là một cái email khác. ',to='kebopdaithanthanh@gmail.com',html = html_content)

loop1 = True
loop2 = True

while loop1: # Vòng lặp nhập đúng thời gian
    try:
        time_entry = input('Enter a time in Hour-Minute format. Note that the Hour is in 24-hours format: ')
        hour, minute = map(int, time_entry.split('-')) # Định dạng thời gian
        time1 = datetime.time(hour, minute)
        while loop2: # Vòng lặp ngồi đọc giờ và so sánh giờ
            if current_time == time1:
                try:
                    gmail.send(msg)
                    winsound.Beep(freq, duration)
                    print('Your message has been sent!')
                    loop1 = False
                except: # Nếu không gửi được email
                    print('Something went wrong! Please check the computer time format and the internet connection.')
                    loop2 = False
                    loop1 = False
            else:
                now = datetime.datetime.now()
                current_time = datetime.time(now.hour, now.minute)
                continue
    except ValueError:
        print('Please enter the appropriate time! ')

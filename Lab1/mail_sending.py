from gmail import GMail, Message
from random import choice

html_template = '''
<h1 style="text-align: center;"><span style="background-color: #ff6600;"><strong>Th&ocirc;ng b&aacute;o</strong></span></h1>
<p><strong>V&agrave;o ng&agrave;y 30 th&aacute;ng 1 năm 2018, <span style="color: #ff00ff;">kebopdaithanthanh</span> đ&atilde; gặp một tai nạn bất ngờ tr&ecirc;n đường đi về nh&agrave;.</strong></p>
<p><strong>Hiện giờ <span style="color: #ff00ff;">kebopdaithanthanh</span> đ&atilde; bị {{sickness}} n&ecirc;n kh&ocirc;ng thể c&oacute; mặt đ&uacute;ng giờ. Xin ch&acirc;n th&agrave;nh xin lỗi!</strong></p></p>
'''
sickness_list = ['kiết lị', 'tiêu chảy', 'sỏi thận', 'thoái hóa đốt sống cổ', 'trĩ', 'sốt virus', 'gãy chân', 'gãy tay', 'đau đầu', 'liệt nửa người', 'liệt toàn thân', 'bại não', 'hôi nách']
sickness = choice(sickness_list)
html_content = html_template.replace('{{sickness}}',sickness)
gmail = GMail('kebopdaithanthanh@gmail.com','bach2o123')
# msg = Message('This is a trash message!',to="c4e.201708@gmail.com",text='''
# ░▄▀▄▀▀▀▀▄▀▄░░░░░░░░░
# ░█░░░░░░░░▀▄░░░░░░▄░
# █░░▀░░▀░░░░░▀▄▄░░█░█
# █░▄░█▀░▄░░░░░░░▀▀░░█
# █░░▀▀▀▀░░░░░░░░░░░░█
# █░░░░░░░░░░░░░░░░░░█
# █░░░░░░░░░░░░░░░░░░█
# ░█░░▄▄░░▄▄▄▄░░▄▄░░█░
# ░█░▄▀█░▄▀░░█░▄▀█░▄▀░
# ░░▀░░░▀░░░░░▀░░░▀░░░''')
msg = Message('Như bạn có thể thấy, đây là một cái email khác. ',to='kebopdaithanthanh@gmail.com',html = html_content)
gmail.send(msg)

from pymongo import MongoClient
mongo_uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"
# server:@ds021182.mlab.com
# port:21182

# 1. Mở một kết nối đến mlab
client = MongoClient(mongo_uri)

# 2. Lấy database
db = client.get_default_database()

# 3. Lấy collection
customer = db['customers']
post = db['posts']

my_post = '''
Xung quanh ta có rất nhiều đồng đội.
Đồng đội trong lớp học,
đồng đội trên chiến trường,
đồng đội ở đất nước,
đồng đội tựa bờ vai.













Nhưng ai cũng biết, bóp dái đồng đội mới là thú vui bậc nhất.
                    ~kebopdaithanthanh~
'''
new_post = {
    "title": "Đồng đội",
    "author": "Nguyễn Ngọc Bách",
    "content": my_post
}
try:
    post.insert_one(new_post)
except:
    print('Something went wrong! Please check the computer time format and the internet connection.')

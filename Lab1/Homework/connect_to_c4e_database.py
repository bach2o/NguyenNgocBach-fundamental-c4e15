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

from pymongo import MongoClient
mongo_uri = "mongodb://admin:admin@ds119078.mlab.com:19078/kebopdaithanthanh"
# server:@ds119078.mlab.com
# port:19078
# 1. Mở một kết nối đến mlab
client = MongoClient(mongo_uri)

# 2. Lấy database
db = client.get_default_database()

# 3. Lấy collection
games = db['games'] # retrieve collection
game_list = games.find()

for game in game_list:
    print(game['title'])
# blog = db['blog']

# 4. Tạo document mới
# create a new document
#
# new_game = {
#     'title': 'Grand Theft Auto 5',
#     'description': 'Dangerous Game'
# }
#
# new_blog = {
#     'title': 'Intel scammed users?',
#     'description': 'Multiple products from Intel have been diagnosed with the Meltdown and Spectre...'
# }
# # 5. Put the created document into collection
# games.insert_one(new_game)
# blog.insert_one(new_blog)

from pymongo import MongoClient
mongo_uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"
# server:@ds021182.mlab.com
# port:21182

# 1. Mở một kết nối đến mlab
client = MongoClient(mongo_uri)

# 2. Lấy database
db = client.get_default_database()

# 3. Lấy collection
customers = db['customers']

customer_list = customers.find()

# 4. Thiết lập các biến trong ref
events = 0
advertisements = 0
word_of_mouth = 0
others = 0


# 5. Đếm.
try:
    for customers in customer_list:
        if customers['ref'] == 'events':
            events += 1
        elif customers['ref'] == 'ads':
            advertisements += 1
        elif customers['ref'] == 'wom':
            word_of_mouth += 1
        else:
            others += 1

    print(events, "events")
    print(advertisements, 'ads')
    print(word_of_mouth, 'wom')
    print(others, 'others')


    # 6. Vẽ
    import matplotlib
    matplotlib.use('TkAgg')

    from matplotlib import pyplot

    labels = ['Events', 'Word of mouth', 'Advertisements', 'Others']
    values = [events, word_of_mouth, advertisements, others]
    colors = ['red', 'green', 'blue', 'gray']

    pyplot.pie(values, labels = labels, colors = colors)
    pyplot.axis('equal')

    pyplot.show()
except:
    print('Something went wrong! Please check the internet connection or the database server.')

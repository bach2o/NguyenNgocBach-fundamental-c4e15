from matplotlib import pyplot

# 1. Prepare database
texts = ['Android', 'iOS', 'Web']
values = [30, 40, 30]
colors = ['red', 'green', 'gold']
explode = [0.2, 0.1, 0.1]
# 2. pyplot
pyplot.bar(values, labels=texts, colors=colors, explode = explode )


# 3. Show
pyplot.show()

favs = ['vãi', 'cả', '**']
print(*favs, sep=", ")

#for fav in favs:
#    print(fav, end=", ")
#print()

print("*" * 10)

#pos = 1
#for fav in favs:
#    print("{0}. {1}".format(pos, fav))
#    pos += 1
print(*enumerate(favs))
for index, fav in enumerate(favs):
    s = "{0}. {1}".format(index + 1, fav)
    print(s)

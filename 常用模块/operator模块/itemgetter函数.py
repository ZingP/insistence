from operator import itemgetter

l1 = [1,2,3]
l2 = (3,4,5)
l3 = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

getter = itemgetter(1)

for i in [l1, l2, l3]:
    print(getter(i))
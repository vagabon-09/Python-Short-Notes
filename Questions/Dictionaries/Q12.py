def margeCommon(d1, d2):

    for i, j in d1.items():
        if i in d2.keys():
            d1[i] = d1[i]+d2[i]

    for j in d2:
        if j not in d1.keys():
            d1[j] = d2[j]


d2 = {'a': 100, 'b': 200, 'c': 300, 'e': 500}
d1 = {'a': 300, 'b': 200, 'd': 400}


if len(d1) < len(d2):
    margeCommon(d2, d1)
else:
    margeCommon(d1, d2)


print(d1)

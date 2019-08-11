l1 = ['b','c','d','c','a','a']
l2 = []

for ls in l1:
    if ls not in l2:
        l2.append(ls)

print(l2)



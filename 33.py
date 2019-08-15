list_data = [1,2,5,8,10,3,18,6,20]
a = [x for x in list_data[::2] if x%2==0]
b = [x for x in list_data[::4] if x%2==0]
c = [x for x in list_data[::6] if x%2==0]
print(a)
print(b)
print(c)


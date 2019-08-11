d = {'a':24,'k':33,'g':52,'i':12}


print(type(d))
print(d)

new_list = sorted(d.items(),key=lambda x:x[0])
new_dict = dict(new_list)


print(type(new_dict))
print(new_dict)

new_list1 = sorted(d.items(),key=lambda x:x[1])
print(type(new_list1))
new_dict1 = dict(new_list1)


print(type(new_dict1))
print(new_dict1)








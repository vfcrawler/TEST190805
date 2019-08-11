dict1 = {"name": "zhangsan", "age": 18}

print(dict1)

print(dict1.items())

print(type(dict1.items()))

dict2 = {value: key for key, value in dict1.items()}


print(dict2)


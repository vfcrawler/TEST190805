str1 = "k:1|k1:2|k2:3|k3:4"

dict1 = { k:v for t in str1.split('|') for k,v in (t.split(":"), )}

print(dict1)






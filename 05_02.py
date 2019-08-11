d = {'a':24,'k':33,'g':52,'i':12}
print(d)

d1 = { key : value for key,value in d.items()}
print(d1)

d2 = { value : key for key,value in d.items()}
print(d2)

d4 = sorted(d.items(),key=lambda x : x[0])
print(dict(d4))

d5 = sorted(d.items(),key=lambda x : x[1])
print(dict(d5))

for l in d.items():
    print(eval(str(l)))


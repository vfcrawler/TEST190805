
d1 = {"a":1,"b":2}
d2 = {"c":3,"d":4}
d3 = {"a":3,"c":4}

ret = {}

ret = dict(d1.items()+d2.items())

print(ret)



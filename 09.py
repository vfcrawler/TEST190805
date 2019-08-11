alist = [{'name':'a','age':20},{'name':'b','age':30},{'name':'c','age':25}]

# 升序
new_alist_asc = sorted(alist,key=lambda x:x['age'])

# 降序
new_alist_desc = sorted(alist,key=lambda x:x['age'],reverse=True)

print(new_alist_asc)
print(new_alist_desc)





alist=[{"name":"a","age":20},{"name":"b","age":30},{"name":"c","age":25}]
alist_new=sorted(alist,key=lambda x:x['age'],reverse=False)

print(alist_new)


# 执行顺序
# for x in range(1,5)
#     if x > 2
#         for y in range(1,4)
#             if y < 3
#                 x*y

a = [x*y for x in range(1,5) if x > 2 for y in range(1,4) if y < 3]
print(a)





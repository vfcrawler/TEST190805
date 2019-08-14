
def num_list(num):
    return [x for x in num if x%2==0 and num.index(x)%2==0]

if __name__ == '__main__':
    num=[x for x in range(100)]
    result = num_list(num)
    print(result)


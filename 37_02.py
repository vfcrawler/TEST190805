
def str2IntSorted(str_input):
    return ''.join(sorted(str_input,
                          key=lambda x:int(x)%2==0 and 30-int(x) or int(x)))

if __name__ == '__main__':
    print(str2IntSorted('1982376455'))




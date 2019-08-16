
def str2IntSorted(str_input):

    if isinstance(str_input,str):

        ls = [int(x) for x in str_input]
        ls.sort(reverse=True)

        for i in range(len(ls)):
            if ls[i]%2==1:
                ls.insert(0,ls.pop(i))

        return ''.join(str(x) for x in ls)

if __name__ == '__main__':
    print(str2IntSorted('1982376455'))



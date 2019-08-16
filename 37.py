
def str2IntSorted(str_input):

    if isinstance(str_input,str):

        ls = [int(x) for x in str_input]

        ls_l = [x for x in ls if x%2==1]
        ls_r = [x for x in ls if x%2==0]

        ls_l.sort(reverse=False)
        ls_r.sort(reverse=True)

        ls_l.extend(ls_r)

        return ''.join(str(x) for x in ls_l)

if __name__ == '__main__':
    print(str2IntSorted('1982376455'))


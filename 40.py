

def strCount(str_input):

    dis_count={}

    if isinstance(str_input,str):
        for c in str_input:
            dis_count[c] =  dis_count.get(c,0)+1

    return ','.join(map(lambda x:x[0]+'-'+str(x[1]),
                        dis_count.items()))


if __name__ == '__main__':
    print(strCount('DDJDHGHASGDSA'))


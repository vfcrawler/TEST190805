from functools import reduce

def find_second_large_num(num_list):
    '''
    :param num_list:
    :return (第1大的数,第2大的数)[1]:
    '''
    ret = reduce(lambda ot,x: x>ot[0] and (x,ot[0])
                  or x>ot[1] and (ot[0],x)
                  or ot,num_list,(0,0))

    return ret[1]

if __name__ == '__main__':
    num_list = [1, 2, 3, 5, 6, 67, 8, 8, 34, 34, 34]
    print(find_second_large_num(num_list))


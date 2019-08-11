import random

def shuffle_list(li):
    random.shuffle(li)


if __name__ == '__main__':
    alist = [1,2,3,4,5,6,7,8,9,10,11,12]
    shuffle_list(alist)
    print(alist)
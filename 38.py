
def find_second_large_num(num_list):
    return sorted(num_list)[-2]


if __name__ == '__main__':
    num_list = [1,2,3,5,6,67,8,8,34,34,34]
    print(find_second_large_num(num_list))


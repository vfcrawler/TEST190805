
def find_second_large_num(num_list):

        one = num_list[0]
        two = num_list[0]

        if len(num_list)>0:
            for i in range(1,len(num_list)):
                if num_list[i]>one:
                    two = one
                    one = num_list[i]
                elif num_list[i]>two:
                    two = num_list[i]

        return two

if __name__ == '__main__':
    num_list = [1, 2, 3, 5, 6, 67, 8, 8, 34, 34, 34]
    print(find_second_large_num(num_list))



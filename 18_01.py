class Solution(object):
    def reserve(self,x):
        str_x = str(x)
        if x<0:
            str_x = '-'+str_x[1:][::-1]
        else:
            str_x = str_x[::-1]
        x = int(str_x)

        return x if -2147483648 < x < 2147483647 else 0

if __name__ == '__main__':
    s = Solution()
    reverse_int = s.reserve(0)
    print(reverse_int)

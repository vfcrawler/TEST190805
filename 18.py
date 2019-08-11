class Solution(object):
    def reserve(self,x):
        if -10<x<10:
            return x
        str_x = str(x)
        if str_x[0]!='-':
            str_x = str_x[::-1]
            x = int(str_x)
        else:
            str_x = str_x[1:][::-1]
            x = int(str_x)
            x = -x

        return x if -2147483648<x<2147483647 else 0

if __name__ == '__main__':
    s = Solution()
    reverse_int = s.reserve(123456)
    print(reverse_int)






import string
def get_missing_letter(str_input):
    #方法2 使用string.ascii_lowercase生成a-z字符串
    s1 = set(string.ascii_lowercase)
    s2 = set(str_input.lower())

    # 排序字符串
    ret = ''.join(sorted(s1-s2))
    return ret

if __name__ == '__main__':
    print(get_missing_letter('python'))













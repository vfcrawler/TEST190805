def get_missing_letter(str_input):
    #方法1 手输a-z字符串
    s1 = set('abcdefghijklmnopqrstuvwxyz')
    s2 = set(str_input.lower())

    # 排序字符串
    ret = ''.join(sorted(s1-s2))
    return ret

if __name__ == '__main__':
    print(get_missing_letter("python"))






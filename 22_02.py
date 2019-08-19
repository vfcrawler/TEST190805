def get_missing_letter(str_input):
    #方法三 使用map(chr,range(ord('a'),ord('z')+1))生成a-z字符串
    s1 = set(''.join(map(chr,range(ord('a'),ord('z')+1))))
    s2 = set(str_input.lower())

    # 排序字符串
    ret = ''.join(sorted(s1-s2))
    return ret

if __name__ == '__main__':
    print(get_missing_letter('Python'))


from collections import Counter

def strCount(str_input):
    return ','.join(map(lambda x:x[0]+'-'+str(x[1]),
                       Counter(str_input).most_common()))

if __name__ == '__main__':

    print(strCount('ABCDFGRSFDCXVS'))
    

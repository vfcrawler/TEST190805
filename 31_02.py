import re
from collections import Counter

def countwords(filepath):
    with open(filepath,'r+') as f:
        return list(map(
                        lambda x:x[0],
                        Counter(re.sub('\W+',' ',f.read()).split()).most_common(10)
                    ))

if __name__ == '__main__':
    print(countwords('31_01.txt'))


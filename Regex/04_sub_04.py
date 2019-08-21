import re

html = '''<li data-view="4" class="active"><a href="/3.mp3" 
singer="齐秦">往事随风</a></li>
<li data-view="6"><a href="/4.mp3" 
singer="beyond">光辉岁月
</a></li>'''

# 修饰符参数放在第4个位置
ret1 = re.sub('<a.*?>(.*?)</a>','',html,re.S)

# 修饰符指定参数名
ret2 = re.sub('<a.*?>(.*?)</a>','',html,flags=re.S)

print('\n修饰符参数放在第4个位置返回结果:\n')
print(ret1)
print('\n修饰符指定参数名返回结果:\n')
print(ret2)

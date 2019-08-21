# 先利用sub方法将<a></a>标签去掉(替换成空串),
# 再使用findall()方法取出所有的歌名
import re

html='''<div id="songs-list">
<h2 class="title">经典老歌</h2>
<p class="introduction">
经典老歌列表
</p>
<ul id="list" class="list-group">
<li data-view="2">一路上有你</li>
<li data-view="7">
<a href="/2.mp3" singer="任贤齐">沧海一声笑</a>
</li>
<li data-view="4" class="active"><a href="/3.mp3" 
singer="齐秦">往事随风</a></li>
<li data-view="6"><a href="/4.mp3" 
singer="beyond">光辉岁月
</a></li>
<li data-view="5">
<a href="/5.mp3" singer="陈慧琳">记事本</a>
</li>
<li data-view="5">
<a href="/6.mp3" singer="邓丽君">但愿人长久</a>
</li>
</ul>
</div>'''

# 先将HTML文本中的<a...></a>标签替换成空串
tmp = re.sub('<a.*?>|</a>','',html,flags=re.S)

# 再使用findall()方法提取<li></li>标签中的文本
ret = re.findall('<li.*?>(.*?)</li>',tmp,flags=re.S)

for e in ret:
    # 将换行符替换成
    print(re.sub('\n','',e,flags=re.S))




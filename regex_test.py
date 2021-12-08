# import re

# content = '''Hello 1234567 World_This
# is a Regex Demo
# '''
# # .*是贪婪模式，.*？为非贪婪模式
# # re.S标记匹配包括换行符在内的所有字符
# result = re.match('He.*?(\d+).*?Demo$', content, re.S)
# print(result.group())


# import re

# content = 'Extra strings Hello 1234567 World_This is a Regex Demo Extra Strings'
# # result = re.match('Hello.*?(\d+).*?Demo', content)
# result = re.search('Hello.*?(\d+).*?Demo', content)
# print(result)


import re

html = '''<div id="songs-list">
<h2 class="title">经典老歌</h2>
<p class="introduction">
经典老歌列表
</p>
<ul id="list' class="list-group">
<li data-view="2">一路有你</li>
<li data-view=7">
<a href="/2.mp3" singer="任贤齐">沧海一声笑</a>
</li>
<li data-view="4" class="active">
<a href="/3.mp3" singer="齐秦">往事随风</a>
</li>
<li data-view="6"><a href="/4.mp3" singer="beyond">光辉岁月</a></li>
<li data-view="5"><a href="/5.mp3" singer="陈慧琳">记事本</a></li>
<li data-view="5">
<a href="/6.mp3" singer="邓丽君">但愿人长久</a>
</li>
</ul>
</dev>
'''
# result = re.search('<li.*?active.*?singer="(.*?)">(.*?)</a>', html, re.S)
# if result:
#     print(result.group(1), result.group(2))

# results = re.findall('<li.*?href="(.*?)".*?singer="(.*?)">(.*?)</a>', html, re.S)
# print(results)
# print(type(results))
# for result in results:
#     print(result)
#     print(result[0], result[1], result[2])


# html = re.sub('<a.*?>|</a>', '', html)
# print(html)
# results = re.findall('<li.*?>(.*?)</li>', html, re.S)
# for result in results:
#     print(result.strip())
#     # print(result[0])

# import re

# content = '54akfkdf3kk32323kfk'
# content = re.sub('\d+', '', content)
# print(content)


import re

content1 = '2021-12-08 10:00'
content2 = '2021-12-08 12:00'
content3 = '2021-12-08 22:00'
pattern = re.compile('.{1}\d{2}:\d{2}')
result1 = re.sub(pattern, '', content1)
result2 = re.sub(pattern, '', content2)
result3 = re.sub(pattern, '', content3)
print(result1, result2, result3, sep=' ')

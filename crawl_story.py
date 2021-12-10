import array
import re
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
from cn2an import cn2an
import time
import numpy as np

def get_content(url):
    r = requests.get(url = url)
    html = r.text
    bs = BeautifulSoup(html, 'lxml')
    texts = bs.find('div', id = 'content')
    content = texts.text.strip().split('\xa0'*4)
    return content

if __name__ == '__main__':
    book_name = '诡秘之主.txt'
    host = 'https://www.xinbiquge.org'
    url = host + '/xiaoshuo/1bm.html'
    r = requests.get(url = url)
    html = r.text
    bs = BeautifulSoup(html, 'lxml')
    listmain = bs.find('div', class_ = 'listmain')
    chapters = listmain.find_all('a')
    chapterList = []
    multi = {}
    for chapter in chapters:
        url = host + chapter.get('href')
        if chapter.string:
            result = re.match('(\d+)(.*)', chapter.string)
            chapter_id = 1
            if result == None:
                result = re.match('第(.*?)章(.*)', chapter.string)
                chapter_id = cn2an(result.group(1))
                chapter_id = str(chapter_id)
            else:
                chapter_id = result.group(1)
            if not chapter_id in multi:
                chapter_name = result.group(2)
                multi[chapter_id] = True
                chapterList.append([chapter_id, chapter_name, url])

    chapterList.sort(key=lambda chapter: int(chapter[0]))
    for chapter in tqdm(chapterList):
        content = get_content(chapter[2])
        with open(book_name, 'a', encoding='utf-8') as f:
            f.write(chapter[1])
            f.write('\n'.join(content))
            
        time.sleep(10)

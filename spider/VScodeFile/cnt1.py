import json
from multiprocessing import Pool
import requests
import re
headers={
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0; HTC; Titan)",
}

def getOnePage(url):
    try:
        response=requests.get(url,headers=headers)
        if response.status_code==200:
            return response.text
        else:
            return None
    except:
        return None

def dealOnePage(html):
    #onePart=re.search('<dd>.*?board-index board-index-1">(\d+).*?title="(\S+)".*?<img.*alt=.*?src="(\S+).*</a>.*?<* class="star">(\S+).*?</p>.*?class="releasetime">(\S+)</p>.*?class="integer">(\S+)</i>./class="fraction">(\S+)</i>.*</dd>')
    # cntNew='<dd>.*?board-index.*?>(\d+)</i>.*?title="(.*?)".*?board-img.*?src="(\a).*</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>.*?integer">(.*?)</i>.*fraction">(.*?)</i>*?</dd>'
    # cntNew=re.compile(cntNew)
    pattern=re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name"><a.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>',re.S)
    #pattern=re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?title="(.*?)".*?>.*?class="board-img".*?src="(.*?)">.*?star">(.*?)</p>*?releasetime">(.*?)</p>.*?interger">(.*?)</i>.*?fraction">(\d+)</i>.*?</dd>',re.S)
    items=re.findall(pattern,html)
    for item in items:
        item=yield {
            'index':item[0],
            'img':item[1],
            'title':item[2],
            'stars':item[3].strip()[3:],
            'time':item[4].strip()[5:],
            'score':item[5]+item[6]
        }
    # print(html)
    # for item in items:
    #     print(item)
    #     print(item[0]+" "+item[1]+" "+item[2]+" "+item[3]+" "+item[1]+" "+(item[5]+item[6]))
def write_to_file(content):
    with open('result.txt','a',encoding='utf-8') as f:
        f.write(json.dumps(content,ensure_ascii=False)+'\n')
        f.close()
def main(pageNums):
    baseUrl="https://maoyan.com/board/4?offset="+str(pageNums)
    text=getOnePage(baseUrl)
    print(text)
    for item in dealOnePage(text):
        print(item)
        write_to_file(item)


if __name__ == '__main__':
    for i in range(10):
        main(i*10)
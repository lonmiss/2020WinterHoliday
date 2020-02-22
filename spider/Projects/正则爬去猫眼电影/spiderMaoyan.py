import requests
import re
headers={
    'User-Agent':"Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1"
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
    pattern=re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name"><a.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>.*?integer">(.*?)<*i>.*?fraction">(.*?)</i>.*?</dd>',re.S)
    items=re.findall(pattern,html)
    print(items)

def main(pageNums):
    baseUrl="https://maoyan.com/board/4?offset="+str(pageNums)
    text=getOnePage(baseUrl)
    dealOnePage(text)

if __name__ == '__main__':
    main(0)
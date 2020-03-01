import requests
import re
headers={
    'User-Agent':"Mozilla/5.0 (Windows NT 6.1; rv:2.0.0) Gecko/20100101 Firefox/4.0.1"
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
    pattern = re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name"><a.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>',re.S)
    items=re.findall(pattern,html)
    for item in items:
        print(item[0]+" "+item[1]+" "+item[2]+" "+item[3]+" "+item[1]+" "+(item[5]+item[6]))

def main(pageNums):
    baseUrl="https://maoyan.com/board/4?offset="+str(pageNums)
    text=getOnePage(baseUrl)
    print(text)
    dealOnePage(text)


if __name__ == '__main__':
    main(0)
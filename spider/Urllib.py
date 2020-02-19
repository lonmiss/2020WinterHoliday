import urllib.response
# response=urllib.request.urlopen("http://www.baidu.com")
response=urllib.request("http://www.baidu.com")
print(response.read().decode('utf-8'))


# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import re


def getHttpUrl(graburl):
    r = requests.get(graburl)
    soup = BeautifulSoup(r.content, "html5lib")


    a = soup.find_all('a')
    urlList = []
    for i in a:
        # Æ¥Åä×Ö·û´®
        try:
            url = i.get('href')
            pattern = re.compile(r'http')
            match = pattern.search(url)


            if match:
                urlList.append(url)
        except:
            print('error')




    return urlList


####
####
# http://news.baidu.com
urlList = getHttpUrl('https://www.douban.com/')
fil = open(r'C:\Users\Administrator\Desktop\321.txt','w')
for i in urlList:
    print(i)
    newList = getHttpUrl(i)    
    for j in newList:
        print(j,file = fil)

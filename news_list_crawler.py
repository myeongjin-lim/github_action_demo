import requests as req
import os
from os.path import abspath
from bs4 import BeautifulSoup as bs

BASE_DIR = os.path.dirname(os.path.abspath("__file__"))
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'}

category = ['0401','0402','0403','0404','0405','0408','0409']
news_href_list = []

for cate in category:
    
    for pageNo in range(1,11):
        url = 'https://www.hankyung.com/economy/{}?page={}'.format(cate, pageNo)
        
        res = req.get(url, headers = headers)
        html = bs(res.content, 'lxml')

        tit_tags = html.select('h3.tit > a')

        for tit in tit_tags:
            news_href_list.append(tit.get('href'))  

file = open(os.path.join(BASE_DIR, 'news_list.txt'), 'w', encoding='utf-8')
file.write(str(news_href_list)
file.close()

print('수집완료>>',os.path.join(BASE_DIR, 'news_list.txt'))

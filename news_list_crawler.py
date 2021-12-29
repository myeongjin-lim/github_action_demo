import requests as req
import os
from bs4 import BeautifulSoup as bs

def crawling_hankyung_news_link(news_url, pageNum):
    news_href_list = []
    
    for pageNo in range(1,pageNum+1):
        url = '{}{}'.format(news_url, pageNo)
        headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'}

        res = req.get(url, headers = headers)
        html = bs(res.content, 'lxml')

        tit_tags = html.select('h3.tit > a')

        for tit in tit_tags:
            news_href_list.append(tit.get('href'))  
            
    return news_href_list

def save_file(data):
    file = open(os.path.join(BASE_DIR, 'news_list.txt'), 'w', encoding='utf-8')
    file.write(data)
    file.close()
    print('저장완료')

category = ['0401','0402','0403','0404','0405','0408','0409']
news_href_list = []

for cate in category:
    url = 'https://www.hankyung.com/economy/{}?page='.format(cate)
    news_href_list.append(crawling_hankyung_news_link(url, 10))
    
save_file(str(news_href_list))

import requests as req
from bs4 import BeautifulSoup as bs
import json
import os
import sys
from inspect import getsourcefile
from os.path import abspath
import cx_Oracle

oracle_url = 'project-db-stu.ddns.net'
oracle_user = 'cgi_7_2_1216'
oracle_password = 'smhrd2'
oracle_port = '1524'
oracle_dbName = 'xe'

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'}

category = ['0401','0402','0403','0404','0405','0408','0409']
news_href_list = []

#카테고리별 뉴스링크 수집
for cate in category:
    
    for pageNo in range(1,11):
        url = 'https://www.hankyung.com/economy/{}?page={}'.format(cate, pageNo)
        
        res = req.get(url, headers = headers)
        html = bs(res.content, 'lxml')

        tit_tags = html.select('h3.tit > a')

        for tit in tit_tags:
            news_href_list.append([int(cate),tit.get('href')]) 
            

# 데이터베이스 연결
conn = cx_Oracle.connect(oracle_user,oracle_password, '{}:{}/{}'.format(oracle_url,oracle_port, oracle_dbName))

# 커서생성
cursor = conn.cursor()

sql = 'insert into news_link values(:1,:2, )'

for href in news_href_list:
    cursor.execute(sql,href)
# cursor.execute(sql, news_href_list[0])
    
print('저장된 링크수>>',cursor.rowcount)

# SQL실행 후 반영 및 커서, 데이터베이스객체 연결종료
cursor.close()
conn.commit()
conn.close()

# import requests as req
# import os
# from os.path import abspath
# from bs4 import BeautifulSoup as bs

# BASE_DIR = os.path.dirname(os.path.abspath("__file__"))
# headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'}

# category = ['0401','0402','0403','0404','0405','0408','0409']
# news_href_list = []

# for cate in category:
    
#     for pageNo in range(1,11):
#         url = 'https://www.hankyung.com/economy/{}?page={}'.format(cate, pageNo)
        
#         res = req.get(url, headers = headers)
#         html = bs(res.content, 'lxml')

#         tit_tags = html.select('h3.tit > a')

#         for tit in tit_tags:
#             news_href_list.append(tit.get('href'))  

# with open(os.path.join(BASE_DIR, 'news_list.txt'), 'w+', encoding='utf-8') as text_file:
#     text_file.write(str(news_href_list))
    
# print('수집완료>> ',os.path.join(BASE_DIR, 'news_list.txt'))

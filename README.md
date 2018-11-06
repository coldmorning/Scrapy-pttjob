# scrapy-pttjob:
## Document:
crawl web:  https://www.ptt.cc/bbs/Soft_Job/index.html

## Json format
{'article_id': 'M.15xxxxxxA.7A0',<br />
 'author': 'yugggg ',<br />
 'content': '\n\nBlog 好讀版：\n',<br />
 'date': 'Mon Nov  5 14:01:04 2018',<br />
 'ip': '180.1xx.2xx.4x',<br />
 'tag': 'Soft_Job',<br />
 'title': '[心得] 如何在xxxxxxxx'}<br />

## Environment:
Python 3.6 <br />
Scrapy 1.5.1 <br />
## Run:
scrapy crawl pttjob -o log.json <br />

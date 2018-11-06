# scrapy-pttjob:
## Document:
crawl web:  https://www.ptt.cc/bbs/Soft_Job/index.html

## Json format
{'article_id': 'M.15xxxxxxA.7A0',
 'author': 'yugggg ',
 'content': '\n\nBlog 好讀版：\n',
 'date': 'Mon Nov  5 14:01:04 2018',
 'ip': '180.1xx.2xx.4x',
 'tag': 'Soft_Job',
 'title': '[心得] 如何在xxxxxxxx'}

## Environment:
Python 3.6 <br />
Scrapy 1.5.1 <br />
## Run:
scrapy crawl pttjob -o log.json <br />

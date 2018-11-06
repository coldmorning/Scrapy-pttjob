import scrapy
import re
from pttjob.items import PttjobItem


class Spider_PttJob(scrapy.Spider):
    
    name = 'pttjob'
    start_urls = ['https://www.ptt.cc/bbs/Soft_Job/index.html']
    allowed_domains = ['ptt.cc']
    MAX_page=1
    def parse(self, response):
        if self.MAX_page:
            domain = 'https://www.ptt.cc/'
            for href in response.xpath('//div[@class="title"]/a'):
                title = href.xpath('text()')[0].extract()
                url = domain+href.xpath('@href')[0].extract()
                yield scrapy.Request(url, callback=self.parse_article)
            self.MAX_page-=1;
            next_page = domain+response.xpath('//a[contains(text(), "上頁")]/@href')[0].extract()
            yield scrapy.Request(next_page, callback=self.parse)
    def parse_article(self,response):
        item = PttjobItem()
       
#       print(response.xpath('//span[text()="標題"]/following-sibling::span/text()')[0].extract())
#       iten['board']

        item['title']  = response.xpath('//span[text()="標題"]/following-sibling::span/text()')[0].extract()
        item['author'] = response.xpath('//span[text()="作者"]/following-sibling::span/text()')[0].extract()
        item['date']   = response.xpath('//span[text()="時間"]/following-sibling::span/text()')[0].extract()
        item['tag']    = response.xpath('//span[text()="看板"]/following-sibling::span/text()')[0].extract()
        item['content']= response.xpath('//div[@id="main-content"]/text()')[0].extract()

        # find article id: https://www.ptt.cc/bbs/Soft_Job/(articel id).html
        url = response.xpath('//link[@rel="canonical"]/@href')[0].extract()
        article_id = url.split('/')[-1].strip('.html')
        item['article_id'] = article_id
        
        # find article ip address 
        StrAndIp = response.xpath('//span[contains(text(),"發信站: ")]')[0].extract()
        ip = re.search(r'[0-9]*\.[0-9]*\.[0-9]*\.[0-9]*',StrAndIp)
        try:       
            item['ip'] = ip.group(0)          

        except:
            item['ip'] = "None"

        #item['message']
        yield item

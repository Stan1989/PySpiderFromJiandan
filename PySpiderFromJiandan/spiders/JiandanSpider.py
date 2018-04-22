#coding:utf-8

import scrapy
from PySpiderFromJiandan.items import PyspiderfromjiandanItem

class JiandanSpider(scrapy.Spider):
    name = 'PySpiderFromJiandan'
    allowed_domains = []
    start_urls = ["http://jandan.net/ooxx"]
    def parse(self, response):
        print('JiandanSpider::parse')
        for idx in range(1,2):
            surl = "http://jiandan.net/ooxx/page-" + str(idx)
            request = scrapy.Request(url=surl, callback=self.parse_post, dont_filter=True)
            request.meta['PhantomJS'] = True
            yield request



    def parse_post(self,response):
        imgUrls = response.xpath('//a[@class="view_img_link"]/@href').extract()
        for imgUrl in imgUrls:
            imgUrl = 'http:' + imgUrl
            print('debug : JiandanSpider::parse_post,' + imgUrl)
            item = PyspiderfromjiandanItem()
            item['image_urls'] = [imgUrl]
            yield item


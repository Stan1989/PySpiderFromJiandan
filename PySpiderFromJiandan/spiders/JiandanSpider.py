# coding:utf-8
# We can use this spider to crawl the images of pretty girls.
# Cause the images are loaded dynamically. So we need to use PhantomJS to get the page which is loaded .
# Then we use the normal ways to get image-urls.


import scrapy
from PySpiderFromJiandan.items import PyspiderfromjiandanItem


class JiandanSpider(scrapy.Spider):
    name = 'PySpiderFromJiandan'
    allowed_domains = []
    start_urls = ["http://jandan.net/ooxx"]

    def parse(self, response):
        print('JiandanSpider::parse')
        # define the range of pages.
        for idx in range(1, 2):
            surl = "http://jiandan.net/ooxx/page-" + str(idx)
            request = scrapy.Request(url=surl, callback=self.parse_post, dont_filter=True)
            request.meta['PhantomJS'] = True
            yield request

    # define the call-back function .
    #  to parse the page.
    def parse_post(self, response):
        imgUrls = response.xpath('//a[@class="view_img_link"]/@href').extract()
        for imgUrl in imgUrls:
            imgUrl = 'http:' + imgUrl
            print('debug : JiandanSpider::parse_post,' + imgUrl)
            item = PyspiderfromjiandanItem()
            item['image_urls'] = [imgUrl]
            yield item

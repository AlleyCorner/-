#! usr/bin/env python3

import scrapy

class ShiyanlouGitHubSpider(scrapy.Spider):
    name = 'shiyanlou'

    def start_requests(self):
        url_tmp1 = 'https://github.com/shiyanlou?page={}&tab=repositories'

        urls = (url_tmp1.format(i) for i in range(1,4))
        for url in urls:
            yield scrapy.Request(url=url,callback=self.parse)

    def parse(self,response):
        i=0
        while i<30:
            i += 1
            path = ('//*[@id="user-repositories-list"]/ul/li[{}]').format(i)
            for item in response.xpath(path):
                yield{
                    'name':("".join(item.xpath(path+'/div[1]/h3/a/text()').re('(.+)'))).strip(),
                    'update_time':"".join(item.xpath(path+'/div[3]/relative-time').re('datetime="(.+)"'))}

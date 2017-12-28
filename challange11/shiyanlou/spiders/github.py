'''
#!usr/bin/env python3
# -*- coding: utf-8 -*-
import scrapy


class GithubSpider(scrapy.Spider):
    name = 'github'

    @property
    def start_urls(self):
        url_tmp1 = "https://github.com/shiyanlou?page={}&tab=repositories"
        return (url_tmp1.format(i) for i in range(1,4))
        for url in urls:
            yield scrapy.Request(url = url,callback = self.parse)
    def parse(self, response):
        i = 0
        while i < 30:
            i += 1
            path = ('//*[@id="user-repositories-list"]/ul/li[{}]').format(i)
            for text in response.xpath(path):
#                item = ShiyanlouItem({
                yield{
                    'name':("".join(item.xpath(path+'/div[1]/h3/a/text()').re('(.+)'))).strip(),
                    'update_time':("".join(item.xpath(path+'/div[3]/relative-time').re('datetime="(.+)"')))}
#                yield item
                    
'''

#! usr/bin/env python3

from shiyanlou.items import ShiyanlouItem
import scrapy

class GithubSpider(scrapy.Spider):
    name = 'github'
    @property
    def start_urls(self):
        url_tmp1 = 'https://github.com/shiyanlou?page={}&tab=repositories'
        
        return (url_tmp1.format(i) for i in range(1,4))

    def parse(self,response):
        i=0
        while i<30:
            i += 1
            path = ('//*[@id="user-repositories-list"]/ul/li[{}]').format(i)
            for text in response.xpath(path):
                item = ShiyanlouItem({
                    'name':("".join(text.xpath(path+'/div[1]/h3/a/text()').re('(.+)'))).strip(),
                    'update_time':"".join(text.xpath(path+'/div[3]/relative-time').re('datetime="(.+)"'))})
                yield item

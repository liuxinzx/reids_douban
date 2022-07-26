import scrapy

import  re

from scrapy.http import HtmlResponse

from doubantop250.items import Doubantop250Item



class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['douban.com']
    start_urls = ['https://movie.douban.com/top250']

    def parse(self, response):

        # pass
        movie_list = response.xpath('//*[@id="content"]/div/div[1]/ol/li/div')
        for movie in movie_list:
            item = Doubantop250Item()
            item['link'] = movie.xpath('./div[2]/div[1]/a/@href').extract_first()
            item['img_src'] = movie.xpath('./div[1]/a/img/@src').extract_first()
            item['chinese_name'] = movie.xpath('./div[2]/div[1]/a/span[1]/text()').extract_first()
            foreign_name = movie.xpath('./div[2]/div[1]/a/span[2]/text()').extract_first().replace('\xa0' , '')
            item['foreign_name'] = foreign_name.replace('/' , '')
            item['score'] = movie.xpath('./div[2]/div[2]/div/span[2]/text()').extract_first()
            ratings = movie.xpath('./div[2]/div[2]/div/span[4]/text()').extract_first()
            item['number_ratings'] =  re.findall(r"\d+\.?\d*", ratings)[0]
            item['overview'] = movie.xpath('./div[2]/div[2]/p[2]/span/text()').extract_first()
            item['details'] = movie.xpath('./div[2]/div[2]/p[1]/text()').extract_first().strip().replace('\xa0' , '')

            yield  item





        #模拟翻页
        part_url = response.xpath('//*[@id="content"]/div/div[1]/div[2]/span[3]/a/@href').extract_first()



        next_url = response.urljoin(part_url)
        yield scrapy.Request(
            url=next_url,
            callback=self.parse
        )

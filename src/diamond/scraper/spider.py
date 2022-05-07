import scrapy
from scrapy.crawler import CrawlerProcess


class DiamondSpider(scrapy.Spider):
    name = "diamond_spider"

    def start_requests(self):
        urls = ['https://www.datacamp.com/courses/all']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # simple example: write out the html
        html_file = 'DC_course.html'
        with open(html_file, 'wb') as fout:
            fout.write( response.body )
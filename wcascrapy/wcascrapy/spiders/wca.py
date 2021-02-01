import scrapy


class WcaSpider(scrapy.Spider):
    name = 'wca'
    allowed_domains = ['worldcubeassociation.org']
    start_urls = ['http://worldcubeassociation.org/']

    def parse(self, response):
        pass

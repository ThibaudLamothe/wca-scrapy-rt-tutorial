# Scraping imports
import scrapy

class spiderWCA(scrapy.Spider):
    name = "spiderWCA"
    start_urls=['https://www.worldcubeassociation.org/persons/2012LAMO01']

    def parse(self, response):

        # name = response.css('div#person h2 ::text').extract_first().strip()
        rows = response.css('div.results-by-event table tbody.event-333 tr.result')
        for row in rows:
            competition=row.css('td.competition a::text').extract()
            competition = None if len(competition)==0 else competition[0]
            yield {
                'single' :row.css('td.single::text').extract_first().strip(),
                'avg'    :row.css('td.average::text').extract_first().strip(),
                'round': row.css('td.round ::text').extract_first(),
                'competition': competition,
                # 'name':name,
                # 'profile':response.url
                }

        # Generic information
        # yield {
        #     'name' : response.css('div#person h2 ::text').extract_first().strip(),
        #     'profile' : response.url
        # }
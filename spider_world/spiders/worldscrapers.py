import scrapy


class WorldscrapersSpider(scrapy.Spider):
    name = "worldscrapers"
    start_urls = ['https://www.worldometers.info/world-population/population-by-country/']
    
        
    def parse(self, response):
        rows = response.css('tbody')
        trs = rows.css('tr')
        
        for tr in trs:
            
            population = tr.css('td:nth-child(3)::text').get().strip()
            country = tr.css('td:nth-child(2) a::text').get().strip()
            yield {
                'population': population,
                'country': country,
            }
        
        
        
            
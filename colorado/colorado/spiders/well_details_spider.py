import scrapy
import pandas as pd

class WellDetailsSpider(scrapy.Spider):
    name = "well_details"

    wells = pd.read_csv('./Wells.csv')

    def start_requests(self):
        urls = ['http://cogcc.state.co.us/cogis/FacilityDetail.asp?facid=' + str(i) + '&type=WELL' for i in wells['API']]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)
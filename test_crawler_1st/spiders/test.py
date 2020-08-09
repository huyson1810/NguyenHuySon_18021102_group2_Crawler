import scrapy
import json


class CellphonesSpider(scrapy.Spider):
    name = 'sena'
    start_urls = ['https://www.thegioididong.com/']
    CRAWLED_COUNT = 0

    def parse(self, response):
        if response.status == 200 and response.css('section::attr(class)').get() == 'type0':
            f = open('./output/TGDD.txt','a',encoding="utf-8")
            data = {
                'link': response.url,
                'name': response.css('div.rowtop h1::text').get(),
                'img_src': response.css('div#normalproduct aside.picture div.icon-position img::attr(src)').get(),
                'short_desc':response.css('meta[name="description"]::attr(content)').get(),
                'specification': ','.join([
                    ''.join(c.css('*::text').getall())
                    for c in response.css('ul.parameter span,ul.parameter div')]),
                'rate': response.css('div.toprt div.crt b::text').get(),
                'price':response.css('div.area_price strong::text').get()
            }
            f.write(json.dumps(data, ensure_ascii=False))
            f.write('\n')
        yield from response.follow_all(css='a[href^="https://www.thegioididong.com/"]::attr(href), a[href^="/"]::attr(href)', callback=self.parse)

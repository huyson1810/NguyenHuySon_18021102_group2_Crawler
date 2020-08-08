import scrapy
import json
import re
from datetime import datetime

OUTPUT_FILENAME = 'output/e-commerce/tgdd_{}.txt'.format(datetime.now().strftime('%Y%m%d_%H%M%S'))


class TgddSpider(scrapy.Spider):
    name = 'tgdd'
    allowed_domains = ['thegioididong.com']
    start_urls = ['http://thegioididong.com/']
    CRAWLED_COUNT = 0

    def parse(self, response):
        if response.status == 200 and response.css('body::attr("id")').get() == 'product-detail':
            print('Crawling from:', response.url)
            data = {
                'link': response.url,
                'category': response.css('div.breadcrumb-wrapper > ul > li > a > span::text').getall(),
                'name': response.css('div.product-info-container > a > h1::text').get(),
                'img_url': response.css('div.product-slide-container > div.big-image > img::attr("data-src")').get(),
                'brand': response.css('div.product-info-container > div.brand > a::text').get(),
                'short_desc': '\n'.join(response.css('div.product-info-container > div.product-short-desc p::text').getall()),

                'priority_price': response.css('div.product-info-container > div.priority-store span.store-price.product-price::text').get(),
                'priority_store': response.css('div.product-info-container > div.priority-store img::attr("title")').get(),
            }



            with open(OUTPUT_FILENAME, 'a', encoding='utf8') as f:
                f.write(json.dumps(data, ensure_ascii=False))
                f.write('\n')
                self.CRAWLED_COUNT += 1
                self.crawler.stats.set_value('CRAWLED_COUNT', self.CRAWLED_COUNT)
                print('SUCCESS:', response.url)

    #    yield from response.follow_all(css=a[href^="/"]::attr(href)', callback=self.parse)

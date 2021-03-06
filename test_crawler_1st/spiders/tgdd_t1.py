import scrapy
import json
import re
from datetime import datetime

OUTPUT_FILENAME = 'output/e-commerce/tgdd_t1_{}.txt'.format(datetime.now().strftime('%Y%m%d_%H%M%S'))


class TgddSpider(scrapy.Spider):
    name = 'tgdd_t1'
    allowed_domains = ['thegioididong.com']
    start_urls = ['https://www.thegioididong.com/loa-laptop/loa-bluetooth-icutes-mb-m818-cun']
    CRAWLED_COUNT = 0

    def parse(self, response):
        # if response.status == 200 and response.css('body::attr("id")').get() == 'product-detail':
        print('Crawling from:', response.url)
        data = {
            'link': response.url,

            'name': response.css('div.rowtop h1::text').get(),
            'rate': str(response.css('div.toprt div.crt b::text').get()),
            'category': '/ '.join([
                ''.join(c.css('*::text').getall()) for c in response.css('ul.breadcrumb > li > a span')
            ]),

            'price': response.css('div.area_price > strong::text').get(),
            #            'sale_price': response.css('div.box-online > div > strong:text').get(),
            #            'end_date_sale': response.css('div.box-online > div > div::attr(data-time)').get(),

            'promotion_infor': '\n'.join([
                ''.join(c.css('*::text').getall())
                for c in response.css('div.infopr span')
            ]),

            'img_src': response.css('meta[itemprop="image"]::attr(content)').get(),
            'introduction': response.css('meta[name="description"]::attr(content)').get(),
            'short_description': ' '.join([
                ', '.join(c.css('*::text').getall())
                for c in response.css('ul.parameter span,ul.parameter div')
            ]),

            # 'specification': response.css('article.area_article p::text').getall()

            'specification':
                ''.join([
                    ''.join(c.css('*::text').getall())
                    for c in response.css('article.area_article p')
                ]),

        }

        data['category'] = data['category'].replace('Trang chủ', '')

        with open(OUTPUT_FILENAME, 'a', encoding='utf8') as f:
            f.write(json.dumps(data, ensure_ascii=False))
            f.write('\n')
            self.CRAWLED_COUNT += 1
            self.crawler.stats.set_value('CRAWLED_COUNT', self.CRAWLED_COUNT)
            print('SUCCESS:', response.url)

    # yield from response.follow_all(css='a[href^="https://www.thegioididong.com"]::attr(href), a[href^="/"]::attr(href)', callback=self.parse)

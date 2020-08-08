import scrapy
import json
from datetime import datetime

OUTPUT_FILENAME = 'output/news/kenh14_{}.txt'.format(datetime.now().strftime('%Y%m%d_%H%M%S'))


class Kenh14TestSpider(scrapy.Spider):
    name = 'kenh14_test'
    allowed_domains = ['kenh14.vn']
    start_urls = ['https://kenh14.vn']
    CRAWLED_COUNT = 0

    def parse(self, response):
        if response.status == 200 and response.css('meta[property="og:type"]::attr("content")').get() == 'article':
            print('Crawling from: ' + response.url)
            data = {
                'link': response.url,
                'title': response.css('h1.kbwc-title::text').get(),
                'author': response.css('span.kbwcm-author::text').get(),
                'source': response.css('span.kbwcm-source a::text').get(),
                'description': response.css('h2.knc-sapo::text').get(),
                # 'image': response.css('div.VCSortableInPreviewMode active a::attr(href)').get(),

                'tags': response.css('ul.knt-list > li.kli > a::text').getall(),

                # 'date': response.css('span.kbwcm-time::text').get(),
                'pub_date': response.css('meta[property="article:published_time"]::attr("content")').get(),

                # 'content': '\n'.join(response.css('div.knc-content p::text').getall())
                'content': '\n'.join([
                    ''.join(c.css('*::text').getall())
                    for c in response.css('div.knc-content p')
                ]),

            }

            with open(OUTPUT_FILENAME, 'a', encoding='utf8') as f:
                f.write(json.dumps(data, ensure_ascii=False))
                f.write('\n')
                self.CRAWLED_COUNT += 1
                self.crawler.stats.set_value('CRAWLED_COUNT', self.CRAWLED_COUNT)
                print('SUCCESS:', response.url)

        yield from response.follow_all(css='a[href^="/"]::attr(href)', callback=self.parse)

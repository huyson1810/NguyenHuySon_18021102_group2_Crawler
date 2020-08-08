import scrapy
import json
from datetime import datetime

OUTPUT_FILENAME = 'output/news/kenh14t1_{}.txt'.format(datetime.now().strftime('%Y%m%d_%H%M%S'))


class Kenh14TestSpider(scrapy.Spider):
    name = 'kenh14_t1'
    allowed_domains = ['kenh14.vn']
    start_urls = [
        'https://kenh14.vn/giang-ho-mang-huan-hoa-hong-ngang-nhien-lam-mv-quang-cao-game-danh-bac-co-the-bi-xu-ly-hinh-su-20200613094353799.chn']
    CRAWLED_COUNT = 0

    def parse(self, response):
        print('Crawling from: ' + response.url)
        data = {
            'link': response.url,
            'title': response.css('h1.kbwc-title::text').get(),
            'author': response.css('span.kbwcm-author::text').get().split(','),
            'source': response.css('span.kbwcm-source a::text').get().split(','),
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

        with open(OUTPUT_FILENAME, 'w', encoding='utf8') as f:
            f.write(json.dumps(data, ensure_ascii=False))
            f.write('\n')
            print('SUCCESS:', response.url)

       # yield from response.follow_all(css='a[href^="/"]::attr(href)', callback=self.parse)

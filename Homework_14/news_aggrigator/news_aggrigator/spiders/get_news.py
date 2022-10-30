from datetime import datetime

import scrapy


class GetNewsSpider(scrapy.Spider):
    name = 'get_news'
    allowed_domains = ['forklog.com']
    start_urls = ['https://forklog.com/news']

    def parse(self, response, **kwargs):
        posts = response.xpath('//div[@class="post_item"]')
        result = {}
        for post in posts:
            image = post.xpath('.//img/@src').extract()
            if len(image) > 0:
                result['image'] = image[1]
            else:
                result['image'] = None
            result['title'] = post.xpath('.//div[@class="text_blk"]//p/text()').get()
            result['content'] = post.xpath('.//span[@class="post_excerpt"]/text()').get()
            result['author'] = post.xpath('.//a[@class="author_lnk"]/text()').get()
            date = post.xpath('.//span[@class="post_date"]/text()').get()
            try:
                result['date'] = datetime.strptime(date, '%d.%m.%Y').isoformat()
            except ValueError:
                print(f'Error! {date} format is not correct!')
                continue
            print('POST', post)
            yield result

            next_url = 'https://forklog.com/wp-content/themes/forklogv2/ajax/getPosts.php'
            load_more_btn = response.xpath('//div[@class="load_more_btn"]')
            if load_more_btn:
                yield scrapy.FormRequest(url=next_url, callback=self.parse, formdata={'offset': '101', 'category': '1'})

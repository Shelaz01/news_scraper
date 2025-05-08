import scrapy


class CnnSpider(scrapy.Spider):
    name = "cnn"
    allowed_domains = ["edition.cnn.com"]
    start_urls = [
        'https://edition.cnn.com/business',
        'https://edition.cnn.com/politics',
        'https://edition.cnn.com/entertainment',
        'https://edition.cnn.com/sport'
    ]

    def parse(self, response):
        category = response.url.split('/')[-1]

        for article in response.css('h3.cd__headline a'):
            headline = article.css('::text').get()
            url = response.urljoin(article.attrib['href'])

            if headline and url:
                yield {
                    'headline': headline.strip(),
                    'url': url,
                    'category': category
                }

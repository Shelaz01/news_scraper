import scrapy

class CBCSpider(scrapy.Spider):
    name = 'cbc'
    allowed_domains = ['cbc.ca']
    start_urls = [
        "https://www.cbc.ca/news/politics",
        "https://www.cbc.ca/news/business",
        "https://www.cbc.ca/news/entertainment",
        "https://www.cbc.ca/news/sports"
    ]

    def parse(self, response):
        # Select article blocks
        articles = response.css('a.card')
        for article in articles:
            link = article.css('::attr(href)').get()
            if link and link.startswith("/"):
                link = response.urljoin(link)
                yield scrapy.Request(link, callback=self.parse_article)

    def parse_article(self, response):
        yield {
            'title': response.css('h1::text').get(default='').strip(),
            'url': response.url,
            'category': response.url.split('/')[4],  # 'politics', 'business', etc.
            'content': ' '.join(response.css('div.text-content p::text').getall()).strip()
        }

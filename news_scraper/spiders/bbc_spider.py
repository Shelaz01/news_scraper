import scrapy
from news_scraper.items import NewsArticleItem

class BBCSpider(scrapy.Spider):
    name = 'bbc'
    allowed_domains = ['bbc.com']
    start_urls = [
        'https://www.bbc.com/news/business',
        'https://www.bbc.com/news/politics',
        'https://www.bbc.com/culture/entertainment-news',
        'https://www.bbc.com/sport'
    ]

    def parse(self, response):
        category = response.url.split("/")[-1]

        # --- Case 1: Standard <h2> headlines (e.g., Politics, Business, etc.)
        for headline in response.css('h2[data-testid="card-headline"]'):
            title = headline.css('::text').get()
            parent = headline.xpath('./ancestor::a[1]/@href').get()
            if title and parent:
                yield {
                    'headline': title.strip(),
                    'url': response.urljoin(parent),
                    'category': category
                }

        # --- Case 2: Sports headlines (with <a> > <span> > <p>)
        for link in response.css('a.ssrcss-1oo1bfh-PromoLink'):
            title = link.css('p::text').get()
            if not title:
                title = link.css('span::text').get()
            href = link.css('::attr(href)').get()
            if title and href:
                yield {
                    'headline': title.strip(),
                    'url': response.urljoin(href),
                    'category': category
                }

    def get_category_from_url(self, url):
        if 'business' in url:
            return 'Business'
        elif 'politics' in url:
            return 'Politics'
        elif 'culture' in url or 'entertainment' in url:
            return 'Arts/Culture'
        elif 'sport' in url:
            return 'Sports'
        return 'Unknown'

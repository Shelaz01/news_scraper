import scrapy

class AlJazeeraSpider(scrapy.Spider):
    name = 'aljazeera'
    allowed_domains = ['aljazeera.com']
    
    start_urls = [
        'https://www.aljazeera.com/news',        # Politics / General News
        'https://www.aljazeera.com/business',    # Business
        'https://www.aljazeera.com/sports',      # Sports
        'https://www.aljazeera.com/entertainment-culture',  # Arts / Culture
    ]

    def parse(self, response):
        if 'news' in response.url:
            category = 'Politics'
        elif 'business' in response.url:
            category = 'Business'
        elif 'sports' in response.url:
            category = 'Sports'
        elif 'entertainment-culture' in response.url:
            category = 'Arts/Culture'
        else:
            category = 'General'

        for article in response.css('a.u-clickable-card__link'):
            headline = article.css('span::text').get()
            url = response.urljoin(article.attrib['href'])

            if headline and url:
                yield {
                    'headline': headline.strip(),
                    'url': url,
                    'category': category
                }

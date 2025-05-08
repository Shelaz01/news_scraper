import scrapy

class GuardianSpider(scrapy.Spider):
    name = 'guardian'
    allowed_domains = ['theguardian.com']
    start_urls = [
        'https://www.theguardian.com/world',
        'https://www.theguardian.com/uk/business',
        'https://www.theguardian.com/uk/sport',
        'https://www.theguardian.com/uk/culture',
    ]

    def parse(self, response):
        category = response.url.split("/")[-1]

        # Select <a> tags with headline in aria-label
        for article in response.css('a[aria-label]'):
            headline = article.attrib.get('aria-label')
            url = response.urljoin(article.attrib['href'])
            if headline and url:
                yield {
                    'headline': headline.strip(),
                    'url': url.strip(),
                    'category': category
                }

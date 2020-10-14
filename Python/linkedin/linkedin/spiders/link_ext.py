import scrapy


class QuotesSpider(scrapy.Spider):
    name = "links"

    def start_requests(self):
        urls = [
            "https://www.linkedin.com/mynetwork/invite-connect/connections/"
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-1]
        filename = 'links-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)
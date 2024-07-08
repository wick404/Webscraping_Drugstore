from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor



class RossmannSpider(CrawlSpider):
    name = "rosscrawler"
    allowed_domains = ["www.rossmann.pl"]
    start_urls = ["https://www.rossmann.pl/"]

    rules = (
        Rule(LinkExtractor(allow="kategoria/([^,]+,\d+)"), callback='parse_category'),
    )

    def parse_category(self, response):
        yield {'url': response.url}

#Run from terminal with: scrapy runspider rosscrawler -o output.csv -t csv
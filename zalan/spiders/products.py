import scrapy


class ProductsSpider(scrapy.Spider):
    name = "products"
    allowed_domains = ["zalando.co.uk"]

    def start_requests(self):
        start_urls = []
        for p in range(1, 429):
            start_urls.append(f"https://www.zalando.co.uk/men/?p={p}")
        
        for url in start_urls:
            yield scrapy.Request(url=url, callback=self.parse_search_page)

    def parse_search_page(self, response):
        pass

    def parse(self, response):
        pass

import scrapy.spiders
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule
import subprocess


class CrawlWebSpider(scrapy.spiders.CrawlSpider):
    name = "hiCrawlSpider"
    start_urls = None
    allowed_domains = None
    rules = (Rule(LinkExtractor(), callback="parse_items", follow=True),)

    def __init__(self, *args, **kwargs):
        super(CrawlWebSpider, self).__init__(*args, **kwargs)
        self.start_urls = kwargs.get("start_urls").strip().split()
        self.allowed_domains = kwargs.get("allowed_domain").strip().split()

    def parse_items(self, response):
        yield {"url": response.url, 'title': response.xpath('//title/text()').extract()[0], 'text': response.text}


if __name__ == '__main__':
    urls = "https://saurabhy27.github.io"
    domain = "saurabhy27.github.io"
    subprocess.run(["scrapy", "crawl", "hiCrawlSpider", "-O", "saurabhy27_github_io.csv", "-a", "start_urls={}".format(urls), "-a",
                    "allowed_domain={}".format(domain)])

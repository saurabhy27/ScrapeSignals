import scrapy
import subprocess


class SitemapWebSpider(scrapy.spiders.SitemapSpider):
    name = "hiSitemapSpider"
    sitemap_urls = None
    allowed_domain = None
    sitemap_rules = [("", "parse_items")]
    def __init__(self, *args, **kwargs):
        super(SitemapWebSpider, self).__init__(*args, **kwargs)
        print("Hi there")
        self.sitemap_urls = kwargs.get("sitemap_urls").strip().split()
        self.allowed_domain = kwargs.get("allowed_domain").strip()

    def parse_items(self, response):
        yield {"url": response.url, 'title': response.xpath('//title/text()').extract()[0], 'text': response.text}


if __name__ == '__main__':
    url = "https://salesken.ai/sitemap.xml"
    allowed_doamin = "salesken.ai"
    subprocess.run(
        ["scrapy", "crawl", "hiSitemapSpider", "-O", 'sitemapData.csv', "-a", "sitemap_urls={}".format(url), '-a',
         'allowed_domain={}'.format(allowed_doamin)])

import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
import subprocess


class SimpleWebSpider(scrapy.Spider):
    name = "hiSimpleSpider"
    start_urls = None

    def __init__(self, *args, **kwargs):
        super(SimpleWebSpider, self).__init__(*args, **kwargs)
        self.start_urls = kwargs.get("start_urls").strip().split(",")

    def start_requests(self):
        for start_url in self.start_urls:
            yield scrapy.Request(start_url, callback=self.parse)

    def parse(self, response, **kwargs):
        yield {'url': response.url, 'title': response.xpath('//title/text()').extract()[0],
               'body': response.text}
        url = response.xpath("//*[@id='NavbarCollapseId']/ul/li[2]/a").css("a::attr(href)").get()
        url = response.urljoin(url)
        yield scrapy.Request(url, callback=self.parse)


if __name__ == "__main__":
    # settings = get_project_settings()
    # settings["LOG_FILE"] = "log.log"
    # process = CrawlerProcess(settings)
    # process.crawl("simpleSpider")
    # process.start()
    urls = "https://saurabhy27.github.io,https://saurabhy27.github.io/resume.html"
    subprocess.run(["scrapy", "crawl", "hiSimpleSpider", '-O', 'simpleData.csv', '-a', 'start_urls={}'.format(urls)])

import nltk
from src.services import clean_data, rake, yake
import subprocess
from urllib.parse import urlparse
import os
from threading import Thread
nltk.download('stopwords')
nltk.download('punkt')


def fetch_keywords(file_name):
    rake_keywords = []
    yake_keywords = []
    for gen in clean_data.clean_data(file_name):
        rake_keywords.extend(rake.extaract_rake_keywords(gen))
        # yake_keywords.append(yake.extaractKeywords(gen))
    return rake_keywords


def extract_keywords_from_website(website):
    crawler_name = "hiCrawlSpider"
    domain_name = urlparse(website).netloc
    file_name = domain_name.replace(".", "_")
    file_path = os.path.join(os.getcwd(), "{}.csv".format(file_name))
    if os.path.isfile(file_path):
        os.remove(file_path)
    subprocess.run(["scrapy", "crawl", "{}".format(crawler_name), "-O", "{}.csv".format(file_name), "-a",
                    "start_urls={}".format(website), "-a", "allowed_domain={}".format(domain_name)])
    keywords = fetch_keywords(file_path)
    os.remove(file_path)
    return keywords

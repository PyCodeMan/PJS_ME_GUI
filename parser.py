from html.parser import HTMLParser
import urllib.request as ureq
from urllib.parse import urljoin
from texts_templates import *


class HTMLScraper(HTMLParser):

    def __init__(self, tag, class_name, base_url):
        super().__init__()
        self.tag = tag
        self.class_name = class_name
        self.base_url = base_url
        self.target_data = ''
        self.target_link = []
        self.found_tag = False
        self.target_index = 0

    def found_must_tag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == self.tag and 'class' in attrs and attrs['class'] == self.class_name and self.target_index < 6:
            self.target_index += 1

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == self.tag and 'class' in attrs and attrs['class'] == self.class_name and self.target_index != 6:
            self.found_tag = True
            href = attrs.get('href')
            self.target_index += 1
            if href:
                self.target_link.append(urljoin(self.base_url, href))
        else:
            self.found_tag = False
    
    def handle_data(self, data):
        if self.found_tag and self.target_index == 6:
            self.target_data += data
    
    def get_target_data(self):
        if self.target_index == 6:
            data = self.target_data
            link = self.target_link.pop()
            self.target_data = ''
            self.target_link = []
            return data, link


def scrape(url, tag, class_name, base_url):

    with ureq.urlopen(url) as response:
        scraper = HTMLScraper(tag, class_name, base_url)
        scraper.feed(response.read().decode('utf-8'))

    data, link = scraper.get_target_data()
    return data.replace("  ", ""), link


if __name__ == '__main__':
    print(scrape(url, tag, class_name, base_url))

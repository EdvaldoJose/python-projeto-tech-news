# Requisito 1
from parsel import Selector
import requests
import time


def fetch(url):
    try:
        time.sleep(1)
        response = requests.get(
            url, headers={"user-agent": "Fake user-agent"}, timeout=3
        )
        if response.status_code != 200:
            return None
        return response.text
    except requests.ReadTimeout:
        return None
    raise NotImplementedError


# Requisito 2
def scrape_updates(html_content):
    selector = Selector(text=html_content)
    urls = selector.css(".entry-preview .entry-title a::attr(href)").getall()
    return urls
    raise NotImplementedError


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    next_page_link = selector.css(".nav-links .next::attr(href)").get()
    return next_page_link
    raise NotImplementedError


# Requisito 4
def scrape_news(html_content):
    news_dictionary = {}
    selector = Selector(text=html_content)
    news_dictionary["url"] = selector.css(
        "head link[rel=canonical]::attr(href)").get()

    news_dictionary["title"] = selector.css(
        ".entry-title::text").get().strip(" \xa0")

    news_dictionary["timestamp"] = selector.css(
        ".meta-date::text").get()

    news_dictionary["writer"] = selector.css(".author a::text").get()

    news_dictionary["reading_time"] = int(selector.css(
        ".meta-reading-time::text").re_first(r"\d+"))

    first_paragraph_news = selector.xpath("(//p)[1]//text()").getall()

    news_dictionary["summary"] = "".join(first_paragraph_news).strip(" \xa0")

    news_dictionary["category"] = selector.css(
        ".meta-category .label::text").get()
    return news_dictionary
    raise NotImplementedError


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
    raise NotImplementedError

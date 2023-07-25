from tech_news.database import db
from datetime import datetime


# Requisito 7
def search_by_title(title):
    title_news = db.news.find(
        {"title": {"$regex": title, "$options": "i"}},
        {"title": True, "url": True},
    )

    return_news = []
    for news in title_news:
        return_news.append((news["title"], news["url"]))
    return return_news
    raise NotImplementedError


# Requisito 8
def search_by_date(date):
    try:
        date_format = datetime.strptime(date, "%Y-%m-%d")

        date_news = db.news.find(
            {"timestamp": datetime.strftime(date_format, "%d/%m/%Y")},
            {"title": True, "url": True},
        )

        return_news = []
        for dat in date_news:
            return_news.append((dat["title"], dat["url"]))

        return return_news

    except ValueError:
        raise ValueError("Data inválida")
    raise NotImplementedError


# Requisito 9
def search_by_category(category):
    news_by_category = db.news.find(
        {"category": {"$regex": category, "$options": "i"}},
        {"title": True, "url": True},
    )

    return_news = []
    for cat in news_by_category:
        return_news.append((cat["title"], cat["url"]))

    return return_news
    raise NotImplementedError

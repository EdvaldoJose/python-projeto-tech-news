from tech_news.database import db


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
    """Seu código deve vir aqui"""
    raise NotImplementedError


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
    raise NotImplementedError

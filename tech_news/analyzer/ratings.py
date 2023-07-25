from tech_news.database import db


# Requisito 10
def top_5_categories():
    categories_counter = {}

    for cat_news in db.news.find():
        category = cat_news.get("category")
        if category:
            categories_counter[category] = categories_counter.get(
                category, 0) + 1

    top_categories = sorted(
        categories_counter.items(), key=lambda item: (-item[1], item[0])
    )

    return [category for category, _cat_news in top_categories[:5]]
    raise NotImplementedError

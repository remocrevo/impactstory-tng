from models.badge import Badge

def badge_configs_without_functions():
    resp = []
    for badge_def in all_badge_defs:
        badge_def.pop("function", None)
        resp.append(badge_def)
    return resp

all_badge_defs = [
    {
        "name": "big_in_japan",
        "display_name": "Big in Japan",
        "level": "gold",
        "is_for_products": True,
        "group": "geo_japan",
        "description": "You have 42 products which have more than 3 tweets in Japan",
        "extra_description": None,
        "function": (lambda person: None)
    },
    {
        "name": "twitter_famous",
        "display_name": "Twitter famous",
        "level": "silver",
        "is_for_products": False,
        "group": "twitter_impressions",
        "description": "You have made more than 42000 Twitter impressions",
        "extra_description": None,
        "function": (lambda person: Badge(name="twitter_famous"))
    },
    {
        "name": "sleeping_beauty",
        "display_name": "Sleeping beauty",
        "level": "bronze",
        "is_for_products": True,
        "group": "time_sleeping_beauty",
        "description": "You have a product that got popular after a long sleep",
        "extra_description": None,
        "function": (lambda person: Badge(name="sleeping_beauty", products=dict([(p.doi, True) for p in person.products])))
    },
]
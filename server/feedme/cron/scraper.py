from newsplease import NewsPlease
from django.utils.dateparse import parse_date
from newspaper import Source
from ..models import Feed
def scrape_news():
    the_star = Source("https://thestar.com")
    cbc = Source("https://cbc.ca")
    the_globe = Source("https://theglobeandmail.com")
    global_news = Source("https://globalnews.ca")
    
    # articles are cached, not sure about across cron jobs so duplicate articles aren't returned
    # cache can be cleared using .clean_memo_cache()
    the_star.clean_memo_cache()
    the_star.build()
    cbc.build()
    the_globe.build()
    global_news.build()
    
    print("running cron")
    
    links = the_star.article_urls() + cbc.article_urls() + the_globe.article_urls() + global_news.article_urls()
    
    articles = NewsPlease.from_urls(links[:10])
    
    for article in articles.values():
        if article.title is None or article.description is None or article.maintext is None:
            pass
        print(article.title)
        print(article.description)
        Feed.objects.create(title=article.title, description=article.description, image=article.image_url, date=article.date_publish)

    
    
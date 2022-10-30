# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from .db import session, engine
from .models import News, Author


class NewsAggrigatorPipeline:
    def process_item(self, item, spider):
        # Check if the news is already in the database
        if not session.query(News).filter_by(title=item['title']).first():
            # If not, add it to the database
            if item['author'] != 'Unknown':
                author = session.query(Author).filter_by(name=item['author']).first()
                if not author:
                    author = Author(name=item['author'])
                    session.add(author)
                    session.commit()

            news = News(
                img_url=item['image'],
                title=item['title'],
                content=item['content'],
                date=item['date'],
                author=item['author']
            )
            session.add(news)
            session.commit()
        return item

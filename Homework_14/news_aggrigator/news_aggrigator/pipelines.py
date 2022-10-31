# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from sqlalchemy.orm import sessionmaker
from .db_config import engine
from .models import News, Author, Base


class NewsAggrigatorPipeline:
    def process_item(self, item, spider):
        Base.metadata.create_all(engine)
        session = sessionmaker(bind=engine)()
        with session as db:
            # Check if the news is already in the database
            if not db.query(News).filter_by(title=item['title']).first():
                # If not, add it to the database
                if item['author'] != 'Unknown':
                    author = db.query(Author).filter_by(name=item['author']).first()
                    if not author:
                        author = Author(name=item['author'])
                        db.add(author)
                        db.commit()
                        print('Author added to the database')

                author = db.query(Author).filter_by(name=item['author']).first()
                news = News(
                    img_url=item['image'],
                    title=item['title'],
                    content=item['content'],
                    date=item['date'],
                )
                news.author.append(author)
                db.add(news)
                db.commit()
                print('News added to the database')

        print('Item added to the database')
        return item

from datetime import datetime

import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime


base_url = 'https://forklog.com/news'
response = requests.get(base_url)



# soup = BeautifulSoup(response.text, 'lxml')
soup = BeautifulSoup(response.text, 'html.parser')
posts = soup.find_all('div', class_='post_item')

news = []

for post in posts:
    result = {}

    # image = post.find('img', class_='image_blk')
    image = post.select('img', attrs={'class': 'lazyloaded'})
    for img in image:
        result['image'] = img['src']

    title = post.select('div[class="text_blk"]')
    for el in title:
        result['title'] = el.find('p').text

    result['content'] = post.find('span', class_='post_excerpt').text

    result['author'] = post.find('a', class_='author_lnk').text

    date = post.find('span', class_='post_date').text

    try:
        result['date'] = datetime.strptime(date, '%d.%m.%Y').isoformat()
    except ValueError:
        print(f'Error! {date} format is not correct!')
        continue
    news.append(result)

with open('news.json', 'w',encoding='utf-8') as file:
    json.dump(news, file, indent=4, ensure_ascii=False)


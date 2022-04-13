import requests
import bs4
import re

HEADERS = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
}
KEYWORDS = ['дизайн', 'фото', 'web', 'Python', 'Урбанизм', 'Я пиарюсь']

url = 'https://habr.com/ru/all/'

response = requests.get(url, headers=HEADERS)
text = response.text

soup = bs4.BeautifulSoup(text, features='html.parser')

articles = soup.find_all('article')

for article in articles:
    hubs = article.find_all(class_='tm-article-snippet__hubs-item')
    hubs = set(hub.text.strip() for hub in hubs)
    for hub in hubs:
        if set(re.findall(r'^\w+', hub)) & set(KEYWORDS):
            href = article.find(class_='tm-article-snippet__hubs-item-link').attrs['href']
            link = url + href
            public_date = article.find('span', class_='tm-article-snippet__datetime-published').find('time').attrs['title']
            print(f'Дата: {public_date} - Заголовок: {hub} - Ссылка: {link}')


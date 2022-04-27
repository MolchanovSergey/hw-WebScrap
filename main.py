import requests
import bs4
import re
from Logger import get_logs # Импорт декоратора - логгера

HEADERS = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
}
KEYWORDS = ['дизайн', 'фото', 'web', 'Python', 'Урбанизм', 'Я пиарюсь']

FILE_PATH = 'decorlogs.txt'

@get_logs(FILE_PATH) # Декоратор - логгер
def get_link(url):

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
                result = f'Дата: {public_date} - Заголовок: {hub} - Ссылка: {link}'
                return result

if __name__ == '__main__':
    get_link('https://habr.com/ru/all/')
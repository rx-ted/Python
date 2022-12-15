import requests

from bs4 import BeautifulSoup


url = 'http://www.biquw.com/book/94/'

headers = {

    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/76.0.3809.100 Chrome/76.0.3809.100 Safari/537.36'
}

response = requests.get('http://www.biquw.com/book/94/',headers=headers).text

soup = BeautifulSoup(response, 'lxml')
data_list = soup.find('ul')

for book in data_list.find_all('a'):
    print('{}:{}'.format(book.text, url + book['href']))
    book_url = url+book['href']
    data_book=requests.get(book_url).text
    soup = BeautifulSoup(data_book,'lxml')
    data = soup.find('div', {'id': 'htmlContent'}).text
    # print(data)
    with open(f'书架/剑道独尊/{book.text}.txt','w',encoding='utf-8')as f:
        f.write(data)
        f.close()


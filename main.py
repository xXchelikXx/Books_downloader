import requests
import argparse
import pathlib
from bs4 import BeautifulSoup
import os
from urllib.parse import urljoin, unquote, urlsplit

def check_for_redirect(response):
    if response.history:
        raise requests.exceptions.HTTPError

def download_txt(name_book,url,folder='books/'):
    os.makedirs(folder,exist_ok=True)
    response = requests.get(url)
    response.raise_for_status()
    check_for_redirect(response)
    with open(f'books/{name_book.strip()}.txt', 'wb') as file:
        file.write(response.content)

def download_image(image_url, folder='images/'):
    os.makedirs(folder,exist_ok=True)
    response = requests.get(image_url)
    response.raise_for_status()
    check_for_redirect(response)
    image_name = urlsplit(image_url).path.split('/')[-1]
    file_path = os.path.join(folder, image_name)
    with open(unquote(file_path), 'wb') as file:
        file.write(response.content)

def parse_book_page(response, book_url):
    soup = BeautifulSoup(response.text, 'html.parser')
    title = soup.find('h1').text
    name_book,author = title.split('::')
    image_url = soup.find('div', class_='bookimage').find('img')['src']
    image_url = urljoin(book_url, image_url)
    book_comments = soup.find_all('div', class_='texts')
    comments = [comment.find('span', class_='black').text for comment in book_comments]
    book_genres = soup.find('span', class_='d_book').find_all('a')
    genres = [genre.text for genre in book_genres]
    book_parameters = {'name_book':name_book, 'author':author, 'image_url':image_url, 'comments':comments, 'genres':genres}
    return book_parameters

def main():
    parser = argparse.ArgumentParser(description='Скачавает книги с сайта с ID от-до')
    parser.add_argument('--start_id', help='Первое ID', type=int, default=1)
    parser.add_argument('--end_id', help='Второе ID', type=int, default=11)
    args = parser.parse_args()
    for number in range(args.start_id, args.end_id):
        try:
            url = f"https://tululu.org/txt.php?id={number}"
            book_url = f'https://tululu.org/b{number}/'
            response = requests.get(book_url)
            response.raise_for_status()
            check_for_redirect(response)
            book_parameters = parse_book_page(response, book_url)
            download_txt(book_parameters['name_book'],url)
            download_image(book_parameters['image_url'])
        except:
            print('Книга не найдена')
            
if __name__ == "__main__":
	main()
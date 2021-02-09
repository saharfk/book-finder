import requests
from bs4 import BeautifulSoup
import re


def get_key(val):
    for key, value in namePrice.items():
        if val == value:
            return key

    return "key doesn't exist"


headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
    'accept-language': 'fa-IR,fa;q=0.9,en-US;q=0.8,en;q=0.7'}

text1 = input('print your book name or writer :  ').replace(' ', '+')
print('please wait...\nat the end the dictionary and the best price is typed : \n')
# text1 = 'jg+ballard'
r = requests.get(
    'https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Dstripbooks-intl-ship&field-keywords=' + text1,
    headers=headers)
soup = BeautifulSoup(r.text, 'lxml')
texts = soup.select('.s-latency-cf-section')
nameWriter = {}
namePrice = {}
for i in texts:
    book_name = i.find_all('span', {'class': 'a-size-medium a-color-base a-text-normal'})
    book_writer = i.find_all('span', {'class': 'a-size-base'})
    paper_back = i.find_all('div', {'class': 'a-section a-spacing-none a-spacing-top-small'})
    p = 0
    n = 0
    bookName = ''
    bookWriter = ''
    bookPrice = ''
    try:
        print(book_name[0].get_text())
        bookName = book_name[0].get_text()
        n += 1
        p += 1
    except:
        pass
    try:
        j = 0
        while True:

            if str(book_writer[j].get_text().strip()) == 'by':
                pass
            elif str(book_writer[j].get_text().strip()) == 'and' or str(
                    book_writer[j].get_text().strip()) == '|' or str(book_writer[j].get_text().strip()).isdigit():
                book_writer = i.find_all('a', {'class': 'a-size-base a-link-normal'})
                print(book_writer[0].get_text().replace(' ', '').replace('\n', ''))
                bookWriter = book_writer[0].get_text().replace(' ', '').replace('\n', '')
                n += 1
                break
            else:
                print(book_writer[j].get_text().strip())
                bookWriter = book_writer[j].get_text().strip()
                n += 1
                break
            j += 1
    except:
        try:
            book_writer = i.find_all('a', {'class': 'a-size-base a-link-normal'})
            print(book_writer[0].get_text().replace(' ', '').replace('\n', ''))
            n += 1
            bookWriter = book_writer[0].get_text().replace(' ', '').replace('\n', '')
            break
        except:
            pass
    if n == 2:
        nameWriter[bookName] = bookWriter

    if 'Paperback' in str(i):
        try:
            bookPrice = float(re.findall(r'span class="a-offscreen">\$(.*?)<\/span', str(i))[0])
            print(float(re.findall(r'span class="a-offscreen">\$(.*?)<\/span', str(i))[0]))
            p += 1
        except:
            pass
    if p == 2:
        namePrice[bookName] = bookPrice
    print('***************************************************')
print(nameWriter,
      end='\n--------------------------------------------------------\n')
lst = sorted(namePrice.values())
for i in lst:
    if i != 0.0:
        print('{',get_key(i), ' : ', namePrice[get_key(i)],'}')
        break

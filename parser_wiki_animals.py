import requests
from bs4 import BeautifulSoup

url = "https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту"

page = requests.get(url).text

animals = []

while 'Ящурки' not in animals:
    soup = BeautifulSoup(page, 'lxml')
    names = soup.find('div', class_='mw-category-group').find_all('a')
    for name in names:
        print(name.text)
        animals.append(name.text)
    links = soup.find('div', id='mw-pages').find_all('a')
    for a in links:
        if a.text == 'Следующая страница':
            url = 'https://ru.wikipedia.org/' + a.get('href')
            page = requests.get(url).text

with open("animals_list.txt", "w") as output:
    output.write(str(animals))

animals_capital_letter = [elem[:1] for elem in animals]

with open("animals_capital_letter.txt", "w") as output:
    output.write(str(animals_capital_letter))

letters_for_count = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Э', 'Ю', 'Я']
for letter in letters_for_count:
    count = animals_capital_letter.count(letter)
    print('Количество животных на букву',letter,':', count, 'шт.')
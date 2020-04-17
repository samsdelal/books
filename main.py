import xml.etree.ElementTree as ET

tree = ET.parse("books.xml")
root = tree.getroot()

info = []

root.iter('BOOK')
for ok in root.findall('Book'):
    z = {}
    z['id'] = (ok.attrib)['id']
    z['EAN'] = ok.find('EAN').text
    z['ISBN'] = ok.find('ISBN').text
    z['Author'] = ok.find('Author').text
    z['Title'] = ok.find('Title').text
    z['Publisher'] = ok.find('Publisher').text
    z['Printing'] = ok.find('Printing').text
    z['Year_of_publishing'] = ok.find('Year_of_publishing').text
    z['Format'] = ok.find('Format').text
    z['Price'] = ok.find('Price').text
    info.append(z)


def info_about_book(id):
    for i in info:
        if str(id).find('-') != -1:
            if id == i['ISBN']:
                text = f'id: {i["id"]}\nEAN: {i["EAN"]}\nISBN: {i["ISBN"]}\n' \
                       f'Author: {i["Author"]}\nTitle: {i["Title"]}\nPublisher: {i["Publisher"]}\n' \
                       f'Printing: {i["Printing"]}\nYear_of_publishing: {i["Year_of_publishing"]}\n' \
                       f'Format: {i["Format"]}\n' \
                       f'Price: {i["Price"]}\n'
                print(text)
                main()

        else:
            if id == i['id']:
                text = f'id: {i["id"]}\nEAN: {i["EAN"]}\nISBN: {i["ISBN"]}\n' \
                       f'Author: {i["Author"]}\nTitle: {i["Title"]}\nPublisher: {i["Publisher"]}\n' \
                       f'Printing: {i["Printing"]}\nYear_of_publishing: {i["Year_of_publishing"]}\n' \
                       f'Format: {i["Format"]}\n' \
                       f'Price: {i["Price"]}\n'
                print(text)
                main()


def same_years_book(year):
    t = 0
    for i in info:
        if year == i['Year_of_publishing']:
            t += 1

    print(f'Количество книг по заданному году издания: {t}')
    main()


def mid_price():
    tot = {}
    for i in root.findall('Book'):
        publisher_name = i.find('Publisher').text
        tot[publisher_name] = ''
    for key in tot:
        total = 0
        count = 0
        for ds in info:
            if ds['Publisher'] == key:
                total += float(ds['Price'])
                count += 1
        tot[key] = round((total / count), 2)
    print('Средняя стоимость книг по каждому издательству.\n')
    for d in tot:
        print(d, ':', tot[d])
    main()


def the_biggest_price(publisher, year):
    z = []

    for i in info:
        if publisher == i['Publisher'] and year == i['Year_of_publishing']:
            z.append(int(i['Price']))
    for d in info:
        if publisher == d['Publisher'] and year == d['Year_of_publishing'] and max(z) == int(d['Price']):
            text = f'id: {d["id"]}\nEAN: {d["EAN"]}\nISBN: {d["ISBN"]}\n' \
                   f'Author: {d["Author"]}\nTitle: {d["Title"]}\nPublisher: {d["Publisher"]}\n' \
                   f'Printing: {d["Printing"]}\nYear_of_publishing: {d["Year_of_publishing"]}\n' \
                   f'Format: {d["Format"]}\n' \
                   f'Price: {d["Price"]}\n'

            print(text)
    main()


def main():
    print('''\n1. Вывести полную информацию по id книги.
2. Вывести полную информацию о книге по ISBN.
3. Подсчитать количество книг по заданному году издания.
4. Подсчитать среднюю стоимость книг по каждому издательству.
5. Вывести информацию о самой дорогой книге(ах) по заданным издательству и году издания.
-------
6. Закончить работу программы\n''')
    choose = int(input('Сделайте выбор - '))
    if choose == 1:
        id = input('Введите id книги - ')
        info_about_book(id)
    elif choose == 2:
        id = input('Введите ISBN книги - ')
        info_about_book(id)
    elif choose == 3:
        year = input('Введите год издания книги - ')
        same_years_book(year)
    elif choose == 3:
        mid_price()
    elif choose == 5:
        publ = input('Введите имя издательства')
        date = input('Введите год издания')
        the_biggest_price(publ, date)
    elif choose == 4:
        mid_price()
    elif choose == 6:
        print('\nСпасибо что воспользовались этой программой!')
        quit()


main()

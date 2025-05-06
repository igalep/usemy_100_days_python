from bs4 import BeautifulSoup

with open('website.html') as file:
    content = file.read()

    soup = BeautifulSoup(content, features='html.parser')

    # print(soup.prettify())
    print(soup.h3.string)
    # print(soup.find_all(name='a'))

    values = [val.get('href') for val in soup.find_all(name='a')]

    print(values)

    print(soup.select_one(selector='li').getText())
    print(soup.select_one(selector='#name').getText())
    print(soup.select(selector='.heading'))
import requests
from bs4 import BeautifulSoup


def get_web_page(url):
    response = requests.get(url)

    if response.status_code == 200:
        return response.text
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")
        return None


def foo1():
    site_to_scrap = 'https://news.ycombinator.com/news'
    html_content = get_web_page(url=site_to_scrap)
    soup = BeautifulSoup(html_content, features='html.parser')
    all_points = [int(point.getText().split()[0]) for point in soup.find_all(name='span', class_='score')]
    max_point = max(all_points)
    index = all_points.index(max_point)
    print(index)


def foo2():
    site_to_scrap = 'https://www.empireonline.com/movies/features/best-coming-of-age-movies'
    html_content = get_web_page(url=site_to_scrap)
    soup = BeautifulSoup(html_content, features='html.parser')

    all_titles_tag = soup.find_all(name='h2')
    list_of_titles = [title.getText().split('. ')[1] for title in all_titles_tag]

    reversed_list_of_titles = list_of_titles[::-1]  # Reverse the list

    with open('best_coming_of_age_movies.txt', 'w') as file:
        for title in reversed_list_of_titles:
            file.write(title + '\n')

# foo1()

foo2()
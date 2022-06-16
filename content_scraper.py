import pandas as pd
import requests
from bs4 import BeautifulSoup

from helpers import get_book_title, get_book_alternative_headline, get_book_author, get_book_category, \
    get_book_download_link


def main():
    """
    Scraper that gathers data from the first page of Chitanka(url below) and prints a Dataframe with the data.
    Second option with csv file creation is available and commented in the code.
    """
    url = "https://chitanka.info/new/books"
    page = requests.get(url)
    all_data = []

    soup = BeautifulSoup(page.content, "html.parser")
    book_cards = soup.find_all('div', class_='media-body')

    for element in book_cards:
        single_element_data = [get_book_title(element),
                               get_book_alternative_headline(element),
                               get_book_author(element),
                               get_book_category(element),
                               get_book_download_link(element)]

        all_data.append(single_element_data)

    df = pd.DataFrame(all_data, columns=['Заглавие', 'Алтернативно заглавие', 'Автор', 'Категория', 'Линк за сваляне'])
    # df.to_csv('books-data.csv', index=False, sep=';')
    # Execute line above to create csv file.
    # After that create a new excel file and import the data from the csv file to get a nice tabled format.
    print(df.to_string())


if __name__ == '__main__':
    main()

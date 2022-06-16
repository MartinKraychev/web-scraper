"""
Helpers functions to get a specific attribute from the Soup object.
They return '-' if the attribute is not present.
"""

missing_attribute = '-'


def get_book_title(el):
    title = el.find(attrs={"itemprop": "name"})
    if title:
        return title.text
    return missing_attribute


def get_book_alternative_headline(el):
    result = el.find(attrs={"itemprop": "alternativeHeadline"})
    if result:
        return result.text
    return missing_attribute


def get_book_author(el):
    div_author = el.find('div', class_='bookauthor')
    if div_author:
        author = div_author.find('a').text
        return author
    return missing_attribute


def get_book_category(el):
    div_category = el.find('div', class_='bookcat')
    category = div_category.find('a')
    if category:
        return category.text
    return missing_attribute


def get_book_download_link(el):
    domain = "https://chitanka.info"
    download_div = el.find('div', class_='download-links')
    path = download_div.find('a', class_='dl-fb2')
    if path:
        return domain + path['href']
    return missing_attribute

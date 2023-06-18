import wikipediaapi


def get_article(title):
    wiki_wiki = wikipediaapi.Wikipedia('en')
    page = wiki_wiki.page(title)
    if page.exists():
        return page.text
    else:
        return ""


def read_titles(filename):
    with open(filename, 'r') as file:
        for line in file:
            yield line.strip()


title_generator = read_titles("small.txt")
content = get_article(next(title_generator))
distinct_letters = list({char.upper() for char in set(content) if char.isalpha()})
print(distinct_letters)

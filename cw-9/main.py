import wikipediaapi
from collections import Counter


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


def count_char_occurrences(title):
    article_content = get_article(title)
    return dict(Counter(char.upper() for char in article_content if char.isalpha()))


title_generator = read_titles("small.txt")
all_characters_count = {}

for article_title in title_generator:
    char_occurrences = count_char_occurrences(article_title)
    for key in char_occurrences:
        all_characters_count.setdefault(key, {"occurrences": 0, "articles": 0})
        all_characters_count[key]["articles"] += 1
        all_characters_count[key]["occurrences"] += char_occurrences[key]

character_per_article = {
    key: all_characters_count[key]["occurrences"] / all_characters_count[key]["articles"]
    for key in all_characters_count
}

print(character_per_article)
import requests
from lxml import html

# Hacker News example
news = []  # empty list to add parsed data
response = requests.get('https://news.ycombinator.com/')  # HTTP GET request

dom = html.fromstring(response.text)  # parsing HTML from previous request
table_el = dom.cssselect('table.itemlist')[0]  # using CSS selector to select parsed elements from DOM
title_els = table_el.cssselect('td.title:last-of-type')  # list of selected parsed element from DOM

# Parsing each DOM element selected before
for title_el in title_els:
    news.append({
        'title': title_el.text_content(),
        'url': title_el.cssselect('a')[0].get('href')
    })
print(news)

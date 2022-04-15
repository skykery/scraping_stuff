import json
import requests
from lxml import html

# Autovit JSON in source example
response = requests.get('https://www.autovit.ro/autoturisme/bmw/bmw-alpina')  # HTTP GET request

dom = html.fromstring(response.text)  # parsing HTML from response
script_el = dom.cssselect('script#__NEXT_DATA__')[0]  # getting the script element using a CSS selector
data = json.loads(script_el.text_content())  # parsing the JSON found in script element



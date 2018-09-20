# www.dailysmarty.com/topics/python
#Select all links that go to posts (ie the headings)
#Convert link into a page title
#Output the list
#Hints:
##Requests library
##Inflection Library
##Beautiful Soup4
import requests
from bs4 import BeautifulSoup
import inflection

r = requests.get('http://www.dailysmarty.com/topics/python')
soup = BeautifulSoup(r.text, "html.parser")
post_link_a_tags = soup.select(".post-link-title > h2 > a")
for tag in post_link_a_tags:
    link = tag.get("href")
    link = link.replace("-","_")
    link = link.replace("/posts/","")
    print(inflection.titleize(link))

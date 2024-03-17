import requests
from bs4 import BeautifulSoup

url = 'https://www.amazon.in/'


response = requests.get(url)

# Get the Html
htmlContent = response.content
print(htmlContent)

# Parse the Html
soup = BeautifulSoup(response.text, 'html.parser')
print(soup.prettify)

# Extracting data from html using tags and class names

# Get the title of the html web page
title = soup.title

print(title)
print(type(title))   # Tag
print(type(title.string))     # NavigableString
print(type(soup))       # BeautifulSoup
markeup = "<p><!--this is a Comment--></p>"    # Comment
soup2 = BeautifulSoup(markeup)
print(type(soup2.p.string))
exit()

# Extract Information (Get all the Headlines from the web page)
headlines = soup.find_all('h2', class_='headline')

for headline in headlines:
    print(headline.text.strip())

# Get all the achors
anchors = soup.find_all('a')
# print(anchors)
anchors = soup.find_all('a')[:5]    # Getting only first five links
print(anchors)
for link in anchors:
    print(link.get('href'))    # To get complete link


print(soup.find('p'))    # find a single paragraph

# Get the text from soup
print(soup.get_text())

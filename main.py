import requests
 

api_key = '3b319c643ace403e9d87dbd08f2fb587'
url  = 'https://newsapi.org/v2/everything?q=tesla&from=2024-10-05&'\
       'sortBy=publishedAt&apiKey=3b319c643ace403e9d87dbd08f2fb587'

# Made request to the NewsAPI
request = requests.get(url)

# Got a dictionary with data
content = request.json()

# Accessed and printed the article titles and description
for article in content['articles']:
    print(article['title'])
    print(article['description'])
    
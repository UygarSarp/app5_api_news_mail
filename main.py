import requests
from send_mail import send_email

api_key = "18a8b092b82c4baa81cabfa5124bac45"
url = "https://newsapi.org/v2/everything?q=tesla&from=" \
      "2024-08-14&sortBy=publishedAt&apiKey=18a8b092b82c4baa81cabfa5124bac45"

request = requests.get(url)
content = request.json()
body = ""
for article in content["articles"]:
    if article["title"] is not None:
        body = body + article["title"] + "\n" + article["description"] + 2*"\n"

gdr = body.encode("utf-8")
send_email(gdr)

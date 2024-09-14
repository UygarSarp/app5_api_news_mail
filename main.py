import requests
from send_mail import send_email

topic = "tesla"
api_key = "18a8b092b82c4baa81cabfa5124bac45"
url = f"https://newsapi.org/v2/everything?q={topic}&from=" \
      "2024-08-14&sortBy=publishedAt&apiKey=18a8b092b82c4baa81cabfa5124bac45&language=en"

request = requests.get(url)
content = request.json()
body = ""
for article in content["articles"][:20]:
    if article["title"] is not None:
        body = "Subject: News" + "\n" + body + article["title"] + "\n" + article["description"] + "\n" + article["url"]\
               + 2*"\n"

gdr = body.encode("utf-8")
send_email(gdr)

import requests

url = "https://static.wikia.nocookie.net/wwenetwork/images/7/72/Dwayne_The_Rock_Johnson_pro.png"
image = requests.get(url)

with open("image.png", "wb") as file:
    file.write(image.content)
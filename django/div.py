import requests as r
from bs4 import BeautifulSoup

response = r.get("https://www.learningpeople.com/au/resources/blog/advantages-of-learning-python-in-coding/")

if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")
    div = soup.find("div", class_="RichTextstyles__Content-sc-128b8yo-4 kFKNXo")
    if div:
        para = div.find("p")
        print(para)

    else:
        print("Not found")
else:
    print("Unable to get the data from the given URL")

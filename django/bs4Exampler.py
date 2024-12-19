import requests as r
from bs4 import BeautifulSoup

response = r.get("https://www.tecnrt.org/management.php")

if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")
    div = soup.find_all("div", class_="col-sm-10")
    if div:
        para = div[0].find("p")
        print(para)

    else:
        print("Not found")
else:
    print("Unable to get the data from the given URL")


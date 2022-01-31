from bs4 import BeautifulSoup
import time
import csv

starturl = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser = webdriver.Chrome("chromedriver.exe")
browser.get(starturl)
time.sleep(10)
def scrap():
    headers = ["name", "distance", "mass", "radius"]
    stardata=[]
    soup = BeautifulSoup(browser.page_source,"html.parser")
    for tr_tag in soup.find_all("tr"):
        td_tags=tr_tag.find_all("td")
        stardata.append(td_tags)
        #^ if doesn't work try td_tags.contents[0]
    with open("starscrapper.csv","w") as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(stardata)
scrap()
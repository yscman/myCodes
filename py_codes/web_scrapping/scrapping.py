import urllib.request
from bs4 import BeautifulSoup


class Scraper:
    def __init__(self, site):
        self.site = site
        self.links = set()
        self.celebs = {}

    def get_links(self, number_of_pages):
        for i in range(1, number_of_pages):
            r = urllib.request.urlopen(self.site + str(i))
            soup = BeautifulSoup(r.read(), "html.parser")
            for a in soup.find_all('a', href=True):
                link = a['href']
                if '-net-worth/' in link:
                    self.links.add(link)
            print(self.links)

    def scrape_networth(self, number_of_pages):
        self.get_links(2)
        for link in self.links:
            r = urllib.request.urlopen(link)
            soup = BeautifulSoup(r.read(), "html.parser")
            try:
                self.celebs[soup.findAll("div", {"class": "title"})[0].text] = soup.findAll("div", {"class": "value"})[0].text
            except IndexError:
                pass
        print(self.celebs)

scrape = Scraper('https://www.celebritynetworth.com/category/richest-celebrities/page/')
scrape.scrape_networth(4)
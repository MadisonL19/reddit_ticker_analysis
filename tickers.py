# Dependencies
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

# Create Ticker class for object setup


class Ticker():
    def __init__(self, abbrev, name):
        self.abbrev = abbrev
        self.name = name


query_list = []


def scrape_tickers():

    # Enter page URL where you will scrape tickers and company names from
    url = "http://stockanalysis.com/stocks"

    req = Request(url, headers={'User-Agent': 'Chrome/88.0.4324.192'})
    # Open the webpage
    page = urlopen(req)

    # Pass webpage to BeautifulSoup
    soup = BeautifulSoup(page, 'html.parser')

    # Find list of tickers
    ticker_list = soup.find("ul", class_="no-spacing")

    tickers = ticker_list.find_all("li")

    for ticker in tickers:
        ticker_text = ticker.text.strip()
        split_ticker = ticker_text.split(" - ")
        query_list.append(Ticker(split_ticker[0], split_ticker[1]))

# Dependencies
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

# Create Ticker class for object setup


class Ticker():
    def __init__(self, abbrev, name):
        self.abbrev = abbrev
        self.name = name


query_list = []
recent_IPO_list = []
upcoming_IPO_list = []


# Scrape for Stocks and ETFs
def scrape_tickers():

    # Enter page URL where you will scrape tickers and company names from
    urls = ["http://stockanalysis.com/stocks",
            "https://stockanalysis.com/etf"]

    for url in urls:
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


# Scrape for recent and upcoming IPOs
def scrape_IPOs():

    # Enter page URL where you will scrape recent IPOs from
    url = "https://stockanalysis.com/ipos/"

    req = Request(url, headers={'User-Agent': 'Chrome/88.0.4324.192'})
    # Open the webpage
    page = urlopen(req)

    # Pass webpage to BeautifulSoup
    soup = BeautifulSoup(page, 'html.parser')

    # Find list of tickers
    recent_IPO_table = soup.find("table", class_="maintable tablesort")

    # Grab cells for each row
    recent_IPO_items = recent_IPO_table.find_all("td")

    # Using a counter to determine which fields are pulled and saved
    counter = 1
    for item in recent_IPO_items:
        if counter == 2:
            item_ticker = item.text
            counter = counter + 1
        elif counter == 3:
            item_name = item.text
            recent_IPO_list.append(Ticker(item_ticker, item_name))
            counter = counter + 1
        elif counter == 6:
            counter = 1
        else:
            counter = counter + 1

# Function to remove tickers from recent IPOs if found on stock page


def remove_duplicates():

    # Create empty list for stock tickers from scrape_tickers
    query_abbrev = []

    # Loop through list of stock tickers for scrape_tickers to get abbrev
    for ticker in query_list:
        query_abbrev.append(ticker.abbrev)

    # Loop through list of recent IPOs and remove if abbrev is found in query_abbrev
    for IPO in recent_IPO_list:
        IPO_abbrev = IPO.abbrev
        if IPO_abbrev in query_abbrev:
            recent_IPO_list.remove(IPO)

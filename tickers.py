# Dependencies
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

# Create Ticker class for object setup


class Ticker():
    def __init__(self, label, abbrev, name):
        # , count, total_sentiment, avg_sentiment):
        self.label = label
        self.abbrev = abbrev
        self.symbol = "$" + abbrev
        self.name = name
    # self.count = count
    #     self.total_sentiment = total_sentiment
    #     self.avg_sentiment = avg_sentiment

    # def update_count(self, value):
    #     return self.count + value

    # def update_total_sentiment(self, value):
    #     return self.total_sentiment + value

    # def update_avg_sentiment(self):
    #     return self.count / self.total_sentiment


query_list = []
recent_IPO_list = []
upcoming_IPO_list = []

# Function to scrape all stocks, ETFs, and IPOs - calls functions


def scrape_tickers():
    scrape_stocks()
    scrape_IPOs()


# Scrape for Stocks and ETFs
def scrape_stocks():

    # Enter page URL where you will scrape tickers and company names from
    urls = ["http://stockanalysis.com/stocks",
            "https://stockanalysis.com/etf"]

    counter = 1
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
            if counter == 1:
                ticker_label = "Stock"
            else:
                ticker_label = "ETF"
            ticker_text = ticker.text.strip()
            split_ticker = ticker_text.split(" - ")
            query_list.append(
                Ticker(ticker_label, split_ticker[0], split_ticker[1]))

    counter = counter + 1


def scrape_IPOs():
    scrape_recent_IPOs()
    scrape_upcoming_IPOs()


# Scrape for recent and upcoming IPOs
def scrape_recent_IPOs():

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

    ticker_label = "Recent IPO"

    # Using a counter to determine which fields are pulled and saved
    counter = 1
    for item in recent_IPO_items:
        if counter == 2:
            item_ticker = item.text
            counter = counter + 1
        elif counter == 3:
            item_name = item.text
            recent_IPO_list.append(
                Ticker(ticker_label, item_ticker, item_name))
            counter = counter + 1
        elif counter == 6:
            counter = 1
        else:
            counter = counter + 1

    # remove duplicates from IPO list if found in stock list
    remove_duplicates()


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

# Function to scrape upcoming IPOs


def scrape_upcoming_IPOs():

    # Enter page URL where you will scrape recent IPOs from
    url = "https://stockanalysis.com/ipos/calendar/"

    req = Request(url, headers={'User-Agent': 'Chrome/88.0.4324.192'})
    # Open the webpage
    page = urlopen(req)

    # Pass webpage to BeautifulSoup
    soup = BeautifulSoup(page, 'html.parser')

    # Find list of tickers
    upcoming_IPO_tables = soup.find_all("table", class_="maintable")

    ticker_label = "Upcoming IPO"

    for table in upcoming_IPO_tables:
        # Grab cells for each row
        upcoming_IPO_items = table.find_all("td")
        counter = 1
        for item in upcoming_IPO_items:
            if counter == 2:
                item_ticker = item.text
                counter = counter + 1
            elif counter == 3:
                item_name = item.text
                upcoming_IPO_list.append(
                    Ticker(ticker_label, item_ticker, item_name))
                counter = counter + 1
            elif counter == 6:
                counter = 1
            else:
                counter = counter + 1
        # Using a counter to determine which fields are pulled and saved


scrape_tickers()

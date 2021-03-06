# Dependencies
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

# Enter page URL where you will scrape tickers and company names from
url = "http://stockanalysis.com/stocks"

req = Request(url, headers={'User-Agent': 'Chrome/88.0.4324.192'})
# Open the webpage
page = urlopen(req)

# Pass webpage to BeautifulSoup
soup = BeautifulSoup(page, 'html.parser')

# Extract the HTML from the page
#html_bytes = page.read()
#html = html_bytes.decode("utf-8")

# Find list of tickers
ticker_list = soup.find("ul", class_="no-spacing")

tickers = soup.find_all("li")

for ticker in tickers:
    title = ticker.text.strip()
    print(title)

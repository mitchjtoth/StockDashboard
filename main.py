import requests
from dotenv import load_dotenv
import analyze
import os

# load .env file and get the api key from it
load_dotenv()
api_key = os.getenv("ALPHA_VANTAGE_API_KEY")
if not api_key:
    raise ValueError("API key not found. Did you forget to create or load your .env file?")

# function to call the api and receive the data
def fetchStockData(symbol):
    print(f"fetching data for {symbol}\n")

    r = requests.get(f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&outputsize=compact&apikey={api_key}")
    data = r.json()
    
    return data

def main():
    symbols = ["AAPL", "TSLA"]

    # for each symbol, call the api and clean the data.
    for symbol in symbols:
        rawData = fetchStockData(symbol)

        # This line grabs the stock data and essentially filters out the rest of the json string that's unnecessary
        timeSeries = rawData["Time Series (Daily)"]

        cleanedData = analyze.cleanData(timeSeries, symbol)



if __name__ == "__main__":
    main()

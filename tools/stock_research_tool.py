import os
os.environ["HTTP_PROXY"] = ""
os.environ["HTTPS_PROXY"] = ""

import yfinance
from dataclasses import dataclass
from crewai.tools import tool
@dataclass
class Stock_Research():
    stock: str
    price: str
    change: str

@tool("Live stock information tool")
def get_stock_price(stock_symbol:str)-> Stock_Research:
    """
        Retrieves the latest stock price and other relevant info for a given stock symbol using Yahoo Finance.

        Parameters:
            stock_symbol (str): The ticker symbol of the stock (e.g., AAPL, TSLA, MSFT).

        Returns:
            str: A summary of the stock's current price, daily change, and other key data.
        """
    stock = yfinance.Ticker(stock_symbol)
    info = stock.info

    current_price = info.get("regularMarketPrice")
    change = info.get("regularMarketChange")
    change_percent = info.get("regularMarketChangePercent")
    currency = info.get("currency", "USD")

    if current_price is None:
        return f"Could not fetch price for {stock_symbol}. Please check the symbol."

    return Stock_Research(
        stock = stock_symbol,
        price = f"{current_price} {currency}",
        change = f"{change} ({round(change_percent, 2)}%)"
    )

#print(str(get_stock_price("AAPL")))


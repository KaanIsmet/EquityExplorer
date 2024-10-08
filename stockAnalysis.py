import pandas as pd
import numpy as np
import yfinance as yf
from datetime import date, timedelta
from matplotlib import pyplot as plt

def myPrint():
     print("Stock Analysis Service\n" + 
          "~~~~~~~~~~~~~~~~~~~~~~")

def Input():
    return input("Enter the stock you want to analyize")

def getClosingPrice(ticker, Start, End):
    Asset = pd.DataFrame(yf.download(ticker, start=Start, end=End)['Adj Close'])
    return Asset.reset_index()

def showPlot(stock):
    plt.figure(figsize=(10, 5))
    plt.plot(stock['Date'], stock['Adj Close'], label = "Adjusted Close Price")
    plt.title("Stock Price over Time")
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.grid()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

 
def main():
    
    myPrint()
    stockName = Input()
    
    Start = (date.today() - timedelta(365)).strftime("%Y-%m-%d")
    End = (date.today() + timedelta(2)).strftime("%Y-%m-%d")

    stock = getClosingPrice(stockName, Start, End)

    showPlot(stock)





if __name__ == '__main__':
    main()




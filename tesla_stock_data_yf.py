#extracting tesla stock data using yfinance
import yfinance as yf
import pandas as pd
import requests
from bs4 import BeautifulSoup
import plotly.graph_objects as go
from plotly.subplots import make_subplots

tesla=yf.Ticker('TSLA')
tesla_data=tesla.history(period="max")
tesla_data.reset_index(inplace=True)
print(tesla_data.head(5))


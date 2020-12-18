import yfinance as yf
import numpy as np
import pandas as pd


msft = yf.Ticker("MSFT")
example = msft.history(period='max')
example.to_csv('msft.csv')

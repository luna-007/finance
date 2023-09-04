import re
import os
import requests
import json 
import pandas as pd
import html

def scrape(url, **kwargs):

    session = requests.Session()
    session.headers.update(
        {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'}
    )

    response = requests.get(url, **kwargs)
    return response

def etl(response):
    

    print(html.escape(response.text))




response = scrape('https://www.moneycontrol.com/financials/manappuramfinance/balance-sheetVI/MGF01')
etl(response)
# print(df)

# print(data.text)
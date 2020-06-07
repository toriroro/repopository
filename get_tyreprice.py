# codeing: utf-8
import re
import urllib
from bs4 import BeautifulSoup
import sys
#from requests_oauthlib import OAuth1Session
import time
import requests

from pandas import Series, DataFrame
import pandas as pd
import numpy as np
import csv

def main():
    ##Wiggle
    # アクセスするURL
    #url = "http://www.wiggle.jp/continental-grand-prix-4000s-ii-folding-road-tyre/"
    url = "http://www.wiggle.jp/continental-grand-prix-5000-tyre/" # gp5000    

    # URLにアクセスする htmlが帰ってくる
    html = urllib.request.urlopen(url)

    # htmlをBeautifulSoupで扱う
    soup = BeautifulSoup(html, "html.parser")

    # 要素を取得する
    # タイヤの値段を抽出する
    tyre_price_tag = soup.find_all('p', class_="bem-pricing__product-price js-unit-price")

    # 要素の文字列を取得する
    tyre_prices = str(tyre_price_tag[0].string)

    print('wiggle : ' + tyre_prices)

    #1秒停止
    time.sleep(1)

if __name__ == '__main__':
    main()
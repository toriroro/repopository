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
    # value:23c=5360642523 25c=5360642531
    #tyre_price = soup.find('option',valubem-sku-selector__price pull-righte="5360642523")

    # ↓23c無いとき？
    tyre_price_tag = soup.find_all('p', class_="bem-pricing__product-price js-unit-price")

    print(tyre_price_tag[0].string)
    # 要素の文字列を取得する
    tyre_width_23c = str(tyre_price_tag[0].string)

    # 23c
    #print('wiggle ' + wiggle_width_23c[33:37])
    print('wiggle : ' + tyre_width_23c)

    #1秒停止
    time.sleep(1)

if __name__ == '__main__':
    main()
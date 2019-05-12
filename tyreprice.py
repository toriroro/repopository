# codeing: utf-8
import re
import urllib
from bs4 import BeautifulSoup
import sys
from requests_oauthlib import OAuth1Session
import time
import requests

from pandas import Series, DataFrame
import pandas as pd
import numpy as np
import csv

#gp4000s2の値段
print('gp4000s2 23cの値段')

#################################################################
##Wiggle
# アクセスするURL
url = "http://www.wiggle.jp/continental-grand-prix-4000s-ii-folding-road-tyre/"

# URLにアクセスする htmlが帰ってくる
html = urllib.request.urlopen(url)

# htmlをBeautifulSoupで扱う
soup = BeautifulSoup(html, "html.parser")

# 要素を取得する
# タイヤの値段を抽出する
# value:23c=5360642523 25c=5360642531
#tyre_price = soup.find('option',valubem-sku-selector__price pull-righte="5360642523")

# ↓23c無いとき？
tyre_price = soup.find_all('span',class_="bem-sku-selector__price pull-right")

# 要素の文字列を取得する
wiggle_width_23c = tyre_price[1].string

# 23c
#print('wiggle ' + wiggle_width_23c[33:37])
print('wiggle ' + wiggle_width_23c[1:5])

#1秒停止
time.sleep(1)

#################################################################
#Excelに書き出す
import datetime

#データ取得日の日付
today = datetime.date.today()
today_date = str(today.year) + '/' + str(today.month) + '/' + str(today.day)


#gp4000s2 23c
df1 = DataFrame(
    {'Wiggle': [wiggle_width_23c[1:5]]
    },
    columns=['Wiggle','CRC','Merlin','PBK'],
    index=[today_date],
)

with open('gp4000s2_price_changes.csv', 'a') as f:
    df1.to_csv(f)

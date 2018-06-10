# codeing: utf-8
import re
import urllib
from bs4 import BeautifulSoup
import sys
from requests_oauthlib import OAuth1Session
import time
import requests

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
##CRC
# アクセスするURL
url = "http://www.chainreactioncycles.com/jp/ja/continental-grand-prix-4000s-ii/rp-prod120460"
#url = url.encode('utf-8')


# URLにアクセスする htmlが帰ってくる
#html = urllib.request.urlopen(url)
html = requests.get(url)

# htmlをBeautifulSoupで扱う
soup = BeautifulSoup(html.text, "lxml")

# 要素を取得する
title_tag = soup.find_all('script')

# 要素の文字列を取得する
title = title_tag[52].string

#25cの値段
num_25c = title.find('RP')
#CRC_width_25c = title[num_25c+6:num_25c+10]

#23cの値段
title2 = title[num_25c+1510:]
num_23c = title2.find('RP')
CRC_width_23c = title2[num_23c+6:num_23c+10]

print('CRC ' + CRC_width_23c)

#1秒停止
time.sleep(1)
#################################################################
##Merlin　Cycles

# アクセスするURL
url = 'https://www.merlincycles.com/continental-grand-prix-4000-s-ii-clincher-road-tyre-gp4000s-ii-69890.html'

# URLにアクセスする htmlが帰ってくる
html = urllib.request.urlopen(url)

# htmlをBeautifulSoupで扱う
soup = BeautifulSoup(html, "html.parser")

# 要素を取得する
# タイヤの値段を抽出
tyre_price = soup.find_all('span',class_="price")

# 要素の文字列を取得する
# [0]:23c [1]:25c [2]:28c
Merlin_width_23c = tyre_price[0].string

#title = title_tag.find("priceEach")
#soup.prettify()
#
#print(title_tag)
#print('Merlin ' + Merlin_width_23c)

#1秒停止
time.sleep(1)
#################################################################
#PBK
# アクセスするURL
url = "https://www.probikekit.jp/bicycle-tyres/continental-grand-prix-4000-s-ii-clincher-road-tyre/10918169.html"

# URLにアクセスする htmlが帰ってくる
html = urllib.request.urlopen(url)

# htmlをBeautifulSoupで扱う
soup = BeautifulSoup(html, "html.parser")

# 要素を取得する
tyre_price = soup.find_all('span',class_="productPrice_schema")

# 要素の文字列を取得する
# [0]:JPY [1]:price [2]:price
PBK_all_tyreprice = tyre_price[1].string

print('PBK ' + PBK_all_tyreprice)

#################################################################
#################################################################

#corsa tu 25cの値段
print('vittoria corsa tu 25cの値段')

#################################################################
##Wiggle
# アクセスするURL
url = "http://www.wiggle.co.uk/vittoria-corsa-g-tubular-graphene-tyre/"

# URLにアクセスする htmlが帰ってくる
html = urllib.request.urlopen(url)

# htmlをBeautifulSoupで扱う
soup = BeautifulSoup(html, "html.parser")

# 要素を取得する
# 25cタイヤの値段を抽出する
#tyre_price_Anthracite = soup.find('option',value="5360765905")
#tyre_price_Tan = soup.find('option',value="5360735219")

# ↓23c無いとき？
tyre_price_color = soup.find_all('span',class_="bem-sku-selector__price pull-right")
tyre_price_Anthracite = tyre_price_color[0]
tyre_price_Tan = tyre_price_color[2]

# 要素の文字列を取得する
# [0]:23c [1]:25c [2]:20c [3]:28c
wiggle_25c_Anth = tyre_price_Anthracite.string
wiggle_25c_Tan = tyre_price_Tan.string

# 25c
#print('corsa 25c')
#print('wiggle Anth ' + wiggle_25c_Anth[28:32])
#print('wiggle Tan ' + wiggle_25c_Tan[28:32])

print('corsa 25c')
print('wiggle Anth ' + wiggle_25c_Anth[1:5])
print('wiggle Tan ' + wiggle_25c_Tan[1:5])


#1秒停止
time.sleep(1)
#################################################################


#############################################
#Excelに書き出す
import datetime

#データ取得日の日付
today = datetime.date.today()
today_date = str(today.year) + '/' + str(today.month) + '/' + str(today.day)

from pandas import Series, DataFrame
import pandas as pd
import numpy as np
import csv

#gp4000s2 23c
df1 = DataFrame(
    {'Wiggle': [wiggle_width_23c[1:5]],
    'CRC': [CRC_width_23c],
    'Merlin': [Merlin_width_23c],
    'PBK': [PBK_all_tyreprice]},
    columns=['Wiggle','CRC','Merlin','PBK'],
    index=[today_date],
)

with open('gp4000s2_price_changes.csv', 'a') as f:
    df1.to_csv(f)

#coras tu
df2 = DataFrame(
    {'wiggle Anth 25c': [wiggle_25c_Anth[1:5]],
    'wiggle Tan 25c': [wiggle_25c_Tan[1:5]]},
    columns=['wiggle Anth 25c','wiggle Tan 25c'],
    index=[today_date],
)

with open('corsa_tu_price_changes.csv', 'a') as f:
    df2.to_csv(f)

import requests
from bs4 import BeautifulSoup
import urllib.request
import xml.etree.ElementTree as ET
import datetime

def get_url(location):

    # XMLファイル解析からメッセージ作成　球磨村　葦北の情報のみ
    url = "http://agora.ex.nii.ac.jp/cps/weather/warning/"
    res = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(res, 'html.parser')


    #「熊本県」の情報を取得するまでの無限ループ
    loop = True
    i = 0
    while loop == True:
        parent_div = soup.find_all('div', class_='item')[i]
        prefecture = parent_div.find('div', class_='title').text
        if(prefecture == '熊本県'):
            loop = False
            # 処理をするのにかかったループ数をprint
            print("process_count:", i)
        else:
            i += 1

    #「熊本県」に発令された最新の警報情報を取得
    recent_alert = parent_div.find('div', class_='level2').text
    date = parent_div.find('div', class_='time').text
    alert_date = date.replace("-", "/")
    print(recent_alert)
    print(alert_date)
    
    # 今日の日付を取得
    time = str(datetime.datetime.now())
    today = time.replace("-", "/")
    print(today)

    message = f"現在、発令されている最新の警報は\n『{recent_alert}』です。\n（{alert_date} 発令）"

    return message
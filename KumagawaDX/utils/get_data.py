import requests
from bs4 import BeautifulSoup
import urllib.request
import xml.etree.ElementTree as ET
import datetime

def get_url(message):

    # XMLファイル解析からメッセージ作成　(球磨村、葦北の情報のみ ←もう一回スクレイピングする必要あり)
    url = "http://agora.ex.nii.ac.jp/cps/weather/warning/"
    res = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(res, 'html.parser')

    #urlをスクレイピングして「熊本県」の情報を取得するまでの無限ループ　(もし最後まで検索して無い場合は、そこで終了)
    loop = True
    i = 0
    while loop == True:
        # item内のdivのtitleを取得して、「熊本県」の情報を取得していく
        len_div = len(soup.find_all('div', class_='item'))
        parent_div = soup.find_all('div', class_='item')[i]
        prefecture = parent_div.find('div', class_='title').text
        if(prefecture == '熊本県'):
            loop = False
            # 処理をするのにかかったループ数をprint
            print("process_count:", i)
        else:
            # divの数だけ繰り返す
            if(i==len_div-1):
                loop = False
            else:
                i += 1

    #「熊本県」に発令された最新の警報情報を取得 (最後まで検索して無い場合は、messageを「現在、警報は発令されていません」にする)
    if(prefecture == '熊本県'):
        recent_alert = parent_div.find('div', class_='level2').text
        time = parent_div.find('div', class_='time')
        date = time.text
        alert_date = date.replace("-", "/")
        message = f"現在、発令されている最新の警報は\n『{recent_alert}』です。\n（{alert_date} 発令）"
        # recent_alertの内容によって、colorが変わる
        if("警報" in recent_alert):
            color = "#ff6347"
        else:
            color = "#ffff00"
    else:
        message = "現在、警報は発令されていません。"
        color = "#87cefa"

    """今日の日付を取得
    time = str(datetime.datetime.now())
    today = time.replace("-", "/")
    print("today:"+today)"""

    messages = [message, color]

    return messages
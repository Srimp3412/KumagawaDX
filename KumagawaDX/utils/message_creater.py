import requests
import json
from utils.get_data import get_url

# 送信メッセージ（ボタンテンプレート）
def return_message(message):
    #get_url(message) → return ["メッセージ文", "背景色"]
    ans_message = get_url(message)

    button_template = [
        {
            "type": "template",
            "altText": "最新の警報・注意報情報",
            "template": {
                "type": "buttons",
                "thumbnailImageUrl": "https://puk-loveratory.com/wp/wp-content/uploads/2022/08/kumagawaDX2-1024x780.jpg", # 画像何がいい？
                "imageAspectRatio": "rectangle",
                "imageSize": "contain",
                "imageBackgroundColor": ans_message[1], # ＜背景色＞ 警報→赤、注意報→黄、警報なし→青
                "title": "最新の警報・注意報情報",
                "text": ans_message[0],
                # 画像タップの際の処理
                "defaultAction": {
                "type": "uri",
                "label": "View detail",
                "uri": "https://kumadx.com/live-camera/konose/"
                },
                # 画像下のメッセージ、urlの情報はこれでOK？
                "actions": [
                {
                    "type": "uri",
                    "label": "カメラを見る",
                    "uri": "https://kumadx.com/live-camera/konose/" # くまがわLIVEカメラ
                },
                {
                    "type": "uri",
                    "label": "水位データを見る",
                    "uri": "https://kumadx.com/flood-data/" # KumaNet水位情報
                }
                ]
            }
        }
    ]
    return button_template
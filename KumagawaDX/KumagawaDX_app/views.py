from django.shortcuts import render
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt

from utils import message_creater
from KumagawaDX_app.line_message import LineMessage

@csrf_exempt
def index(request):
    if request.method == 'POST':
        request = json.loads(request.body.decode('utf-8'))
        data = request['events'][0]
        message = data['message']
        reply_token = data['replyToken']
        messages = [LineMessage(message_creater.create_single_text_message(message['text'])), LineMessage(message_creater.test(message['text']))]
        for i in range(1):
            line_message = messages[i]
            line_message.reply(reply_token)
        return HttpResponse("ok")


from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

import os
import json
import boto3

client = boto3.client('lex-runtime')
lex_client = boto3.client('lexv2-runtime')

line_bot_api = LineBotApi('ZCwfLbimj+Mg3O3EHbM3OX80Wj0IOS2a4iPxSbVeLGWUrd9ENit9TEYinJLGc/P7wD//QTC+8oJNzjs5rqRcdneGHBhBPgjASY7v8vbX7mtibtZggWrU4DCnv35jUtxKLqgHZsd8FWbblqdAJD7kkgdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('e901421abca30d6fc6b40a2faa351ff5')
    

def lambda_handler(event, context):
    @handler.add(MessageEvent, message=TextMessage)

    
    def handle_message(event: MessageEvent):
        response = lex_client.recognize_text(
            botId = '',
            botAliasId = '',
            localeId = 'zh_CN',
            sessionId=event.source.user_id,
            text=event.message.text)
        
        for message in response['messages']:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text=message['content']))
       
    # get X-Line-Signature header value
    signature = event['headers']['x-line-signature']
    
    # get request body as text
    body = event['body']

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        return {
            'statusCode': 502,
            'body': json.dumps("Invalid signature. Please check your channel access token/channel secret.")
            }
    return {
        'statusCode': 200,
        'body': json.dumps("Hello from Lambda!")
        }

from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import *
import os

app = Flask(__name__)

line_bot_api = LineBotApi(os.environ['GpBNxICx2tD3RbQ0zqlN/3tK2Q+SwJvauSTw1DVlsSQOrh5kPafXsmncY7gAcXfHhAjsbfKkr9XNFGN0Ml0LBIcFa2ldVI/ls8HuRQsDBy4ejkX0+mb0aHJ3rMoeESu2dbga/LqN5OV+sn0Rg6izpQdB04t89/1O/w1cDnyilFU='])
handler = WebhookHandler(os.environ['66b81b9ec7ea7864ce387e55cb019b41'])


@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = TextSendMessage(text=event.message.text)
    line_bot_api.reply_message(event.reply_token, message)

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
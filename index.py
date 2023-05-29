from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('/U+H4cEZC+0hMe4N9pUu73MZBMMzPiVRagJMgbTx7im5mOUXJ5G8QBbOILLFhbIeR0Gtoq4IJeSMyMAXwGeQJWPnWRxKHY+Ouzv4oR430QEl3JAIBNGpIEr+/RdyQIphOCnZr7lnR1FWU9LMAsj+FgdB04t89/1O/w1cDnyilFU=
/U+H4cEZC+0hMe4N9pUu73MZBMMzPiVRagJMgbTx7im5mOUXJ5G8QBbOILLFhbIeR0Gtoq4IJeSMyMAXwGeQJWPnWRxKHY+Ouzv4oR430QEl3JAIBNGpIEr+/RdyQIphOCnZr7lnR1FWU9LMAsj+FgdB04t89/1O/w1cDnyilFU=')
handler1 = WebhookHandler('7b30a4d67878cda6f3f376ea1a9286dc 7b30a4d67878cda 6f3f376ea1a9286dc')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler1.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler1.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run()

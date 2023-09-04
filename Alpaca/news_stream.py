import websocket, json
from keys import *

data = None

def on_open(ws):
    print("opened")
    auth_data = {
        "action": "auth",
        "key": API_KEY,
        "secret": SECRET_KEY
    }

    ws.send(json.dumps(auth_data))

    listen_news = {"action":"subscribe","news":["*"]}

    ws.send(json.dumps(listen_news))

def on_message(ws, message):
    global data
    print("received a message")
    data = json.loads(message)
    for i in data[0]:
        if (i == 'headline'):
            print("================= Headline ================== \n", data[0]['headline'], '\n')
            print("================= Summary ================== \n", data[0]['summary'])
            print("Content: ", data[0]['content'])


socket = "wss://stream.data.alpaca.markets/v1beta1/news"

ws = websocket.WebSocketApp(socket, on_open=on_open, on_message=on_message)
ws.run_forever()
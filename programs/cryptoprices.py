import json
import websocket
import pandas as pd

assets = ['ADAUSD', 'RSRUSD', 'BTCUSD', 'EOSUSD']
assets = [coin.lower() + '@kline_1m' for coin in assets]
assets = '/'.join(assets)

def on_message(ws,message):
    message = json.loads(message)
    print(message)

socket = "wss://stream.binance.com:9443/stream?streams="+assets

ws = websocket.WebSocket(socket, on_message=on_message())
ws.run_forever()
print(type(websocket))
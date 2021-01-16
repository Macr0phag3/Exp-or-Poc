import websocket  # pip install websocket-client

target = '*4.*54.*74.*73'
port = '80'

ws = websocket.WebSocket()
ws.connect(f'ws://{target}:{port}/ws/ops/tasks/log/')
ws.send(b'{"task":"/opt/jumpserver/logs/jumpserver"}')
for _ in range(10):
    print(ws.recv())

# output
'''
{"message": "\r\n"}
{"message": "2020-05-19 17:54:39 [signal_handler DEBUG] Work ready signal recv\r\n2020-05-19 17:54:39 [signal_handler DEBUG] Start need start
...
'''

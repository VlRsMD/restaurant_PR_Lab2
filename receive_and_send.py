import random
import requests
import json
import sent_order
from types import SimpleNamespace

stack = []

def receive_order():
    global stack
    receive = requests.get("http://127.0.0.1:3900/get")
    rec_order = json.loads(receive.json(), object_hook=lambda d: SimpleNamespace(**d))
    ## add received order to stack
    stack.append(rec_order)
    print(receive.json())

def send_order():
    global stack
    l = len(stack)
    while l >= 0:
        order = stack.pop()
        order_id = order.order_id
        client_id = order.client_id
        restaurant_id = random.randrange(5)+1
        priority = order.priority_id
        items = order.items
        max_wait = order.max_wait
        generation_time = order.generation_time
        cooking_time = max_wait
        cook = random.randrange(8)+1
        order_ready = sent_order.orderOut(order_id, client_id, restaurant_id, priority, items, max_wait,
                                          generation_time, cooking_time, cook)
        order_to_json = json.dumps(order_ready.__dict__)
        ## send prepared order to food ordering service
        send = requests.post('http://127.0.0.1:3800/restaurant', json=order_to_json)
        print(send.json())

print('List of orders received by the restaurant: ')
receive_order()
print('List of orders sent by the restaurant: ')
send_order()




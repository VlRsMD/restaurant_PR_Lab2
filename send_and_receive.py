import random
import requests
import json
import sent_order
import received_order

stack = []

def receive_order():
    global stack
    receive = requests.get("http://127.0.0.1:3900/get")
    rec_order = json.loads(receive, object_hook=received_order.orderIn)
    ## add received order to stack
    stack.append(rec_order)

def send_order():
    global stack
    l = len(stack)
    while l >= 0:
        order = stack.pop()
        order_id = order.order_id
        client_id = order.client_id
        restaurant_id = random.randrange(1, 6, 0)
        priority = order.priority_id
        items = order.items
        max_wait = order.max_wait
        generation_time = order.generation_time
        cooking_time = max_wait
        cook = random.randrange(1, 8, 0)
        order_ready = sent_order.orderOut(order_id, client_id, restaurant_id, priority, items, max_wait,
                                          generation_time, cooking_time, cook)
        order_to_json = json.dumps(order_ready.__dict__)
        ## send prepared order to food ordering service
        requests.post('http://127.0.0.1:3800/restaurant', json=order_to_json)






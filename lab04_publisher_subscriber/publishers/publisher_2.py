import zmq
from time import time, sleep
import random

context = zmq.Context()
pub = context.socket(zmq.PUB)
pub.connect("tcp://proxy:5554")

while True:
    message = random.randint(1, 6)
    print(f"p2 published message: {message}", flush=True)
    pub.send_string("p2 " + str(message))
    sleep(5)

pub.close()
context.close()

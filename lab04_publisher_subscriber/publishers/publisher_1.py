import zmq
from time import time, sleep

context = zmq.Context()
pub = context.socket(zmq.PUB)
pub.connect("tcp://proxy:5555")

while True:
    message = str(time())
    print(f"p1 published message: {message}", flush=True)
    pub.send_string("p1 " + message)
    sleep(5)

pub.close()
context.close()

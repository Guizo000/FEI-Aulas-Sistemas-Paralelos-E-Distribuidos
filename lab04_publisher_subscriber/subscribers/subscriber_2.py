import os
import zmq
from time import sleep

context = zmq.Context()
sub = context.socket(zmq.SUB)
filter_value = "p2"
sub.setsockopt_string(zmq.SUBSCRIBE, filter_value)
sub.connect("tcp://proxy:5557")

while True:
    message = sub.recv_string()
    print(f"message: {message}", flush=True)

sub.close()
context.close()

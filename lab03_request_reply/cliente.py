import zmq
import json
from time import sleep

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://broker:5555")

def Request(command, text=""):
    request = [command, text]

    print(f"Sending Request To {command}", flush=True)
    socket.send(json.dumps(request).encode("utf-8"))

    if(command == "List"):
        todoListBytes = socket.recv()
        todoList = json.loads(todoListBytes.decode("utf-8"))

        for i in range(len(todoList)):
            print(f"{i+1}. {todoList[i]}", flush=True)

    else:
        mensagem = socket.recv().decode("utf-8")
        print(f"{mensagem}", flush=True)
    
    print(f"==================================", flush=True)
    sleep(3)

#Testing the requests
Request("Add", "Do the dishes")
Request("Add", "Do the laundry")
Request("List")
Request("Remove", "Do the dishes")
Request("Remove", "Task that doesn't exist")
Request("List")
Request("Remove", "Do the laundry")
Request("List")







    


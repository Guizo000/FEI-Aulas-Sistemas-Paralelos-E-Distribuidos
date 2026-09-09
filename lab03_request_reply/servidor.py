import zmq
import json

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.connect("tcp://broker:5556")

try:
    with open("todo_list.json", "r") as file:
        todoList = json.load(file)
except (FileNotFoundError, json.JSONDecodeError):
    todoList = []

while True:
    requestBytes = socket.recv()
    request = json.loads(requestBytes.decode("utf-8"))
    
    if(request[0] == "Add"):
        print(f"Adding: \"{request[1]}\"", flush=True)

        todoList.append(request[1])
        with open("todo_list.json", "w") as file:
            json.dump(todoList, file)

        socket.send_string("Success")

    elif(request[0] == "Remove"):
        print(f"Removing: \"{request[1]}\"", flush=True)

        try:
            if todoList:
                todoList.remove(request[1])

            with open("todo_list.json", "w") as file:
                json.dump(todoList, file)
            
            socket.send_string("Success")

        except ValueError:
            socket.send_string(f"Item not found: \"{request[1]}\"")


    elif(request[0] == "List"):
        print(f"Returning Todo List", flush=True)
        socket.send(json.dumps(todoList).encode("utf-8"))

    else:
        print(f"Unknown command: {request}", flush=True)
        socket.send_string("Fail")
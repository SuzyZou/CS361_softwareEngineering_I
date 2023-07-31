import socket

HEADER = 64
PORT = 5051
SERVER = 'localhost'
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
ADDR = (SERVER, PORT)

# Create a socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


def send(msg):
    #encode the msg to UFT-8 format and store it into variable message
    message = msg.encode(FORMAT)
    # get the legth of the message
    msg_length = len(message)
    # encode the lenght 
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' '*(HEADER - len(send_length))

    # send_length = send_length + ( b' '*(HEADER - len(send_length)) )
    print("Sending the message from project to microservice........")
    client.send(send_length)
    print(f"sending the message 1: {send_length}")
    client.send(message)
    print(f"sending the message 2: {message}")

def response():
    print("entering the response")
    #response_length = int(client.recv(HEADER).decode(FORMAT))
    #print(f"Response length: {response_length}")
    response = client.recv(int(1)).decode(FORMAT)
    print(f"Response: {response}")
    return response

# calll the send funcation  and pass the string
send("X9ssawirnoa oawpha;jva")

#gets data back 
server_response = response()
print(f"Response from server: {server_response}")
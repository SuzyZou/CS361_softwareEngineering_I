import socket
import threading
import os
import fcntl

HEADER = 64
PORT = 5051
#SERVER = socket.gethostbyname(socket.gethostname(""))
SERVER = 'localhost'
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

total_threads = 0

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def encript():
    pass

def SaveToFile(msg, conn, addr):
    #take message and save it the curret working dir
    file_path = os.path.dirname(os.path.abspath(__file__))

    # name the output text file based on which thread numb
    document_name = f"/output_{str(total_threads)}.txt" 
    # Concatenate together in the file_path variable
    file_path = file_path + document_name
    try:
        with open(file_path, 'w') as file:
            file.write(msg)
        print("password was successfully saved to file")
         # Send the boolean 1 back to the project to indicate a sucss 
        

        conn.send("1".encode(FORMAT))
    except Exception as e:
        print(f"Error occurred while saving string to file {e}")
       # Send the boolean 0 back to the project to indicate a failure
        conn.send("0".encode(FORMAT))

def ListenFunction(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    # keep tracking how many threads are created
    global total_threads
    total_threads += 1

    connected = True
    while connected:
        # receving the message 1 nof length 
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            print(f"The message 1 recived from project: {msg_length}")
            msg_length = int(msg_length)
            
            # recevie the real password which is message 2
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False
            
            print(f"The message 2 recived from the partner'project {addr}] {msg}")
            # call the SaveToFile function
            SaveToFile(msg, conn, addr)
    # close the connection
    conn.close()
        

def start():
    server.listen()
    while True:
        #Accept the connection 
        conn, addr = server.accept()
        #Creating  a thread 
        thread = threading.Thread(target= ListenFunction, args=(conn, addr))
        # start the thread
        thread.start()


if __name__ == "__main__":
    start()
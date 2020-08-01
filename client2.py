import socket
from threading import Thread
import time


# import tkinter

def receive():
    while True:
        try:
            msg = client_socket.recv(BUFSIZ).decode("utf8")
            print(msg)
        except OSError:
            print("You have disconnected from chat")
            break


def send():
    time.sleep(1)
    msg = input('Enter your name:\n')
    client_socket.send(bytes(msg, "utf8"))
    while msg != "{quit}":
        time.sleep(1)
        msg = input('Enter message:\n')
        client_socket.send(bytes(msg, "utf8"))
    client_socket.close()


if __name__ == "__main__":
    HOST = input('Enter host: ')
    PORT = input('Enter port: ')
    if not HOST:
        HOST = "127.0.0.1"

    if not PORT:
        PORT = 33000
    else:
        PORT = int(PORT)

    BUFSIZ = 1024
    ADDR = (HOST, PORT)

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(ADDR)

    receive_thread = Thread(target=receive)
    receive_thread.start()

    send_thread = Thread(target=send)
    send_thread.start()

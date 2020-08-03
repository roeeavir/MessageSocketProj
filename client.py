import socket


import tkinter

BUFSIZ = 1024


def receive(chat):
    while True:
        try:
            msg = client_socket.recv(BUFSIZ).decode("utf8")
            for i in msg.split('!'):
                chat.insert(tkinter.END, i + "\n")
            chat.yview_pickplace("end")
            # print(msg)
            # new_msg = chat.cget("text") + msg
            # chat.update_idletasks()
            # tkinter.mainloop()
        except OSError:
            break


def send(client_message_box, m):
    msg = client_message_box.get("1.0", tkinter.END)
    if client_message_box.compare("end-1c", "==", "1.0"):
        return
    client_socket.send(bytes(msg, "utf8"))
    client_message_box.delete('1.0', tkinter.END)
    if msg == "{quit}":
        m.destroy()


def set_connection(client_host, client_port, client_name, n):
    host = client_host.get()
    port = client_port.get()
    if not host:
        host = "127.0.0.1"
    if not port:
        port = 33000
    else:
        port = int(port)

    addr = (host, port)

    global client_socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(addr)

    msg = client_name.get()

    client_socket.send(bytes(msg, "utf8"))

    n.destroy()


def on_closing(m):
    client_socket.send(bytes("{quit}", "utf8"))
    m.destroy()





import tkinter

import client
from threading import Thread


n = tkinter.Tk()

n.title('Henji Messenger')
n.geometry('260x160')

# my_msg = tkinter.StringVar()
label1 = tkinter.Label(n, text='Enter host')
label2 = tkinter.Label(n, text='Enter port')
label3 = tkinter.Label(n, text='Enter your Name')
client_host = tkinter.Entry(n, justify='center')
client_port = tkinter.Entry(n, justify='center')
client_name = tkinter.Entry(n, justify='center')
connect_btn = tkinter.Button(n, text='Set name', command=lambda: client.set_connection(client_host, client_port,
                                                                                       client_name, n))

label1.pack()
client_host.pack()

label2.pack()
client_port.pack()

label3.pack()
client_name.pack()

connect_btn.pack()

n.mainloop()

m = tkinter.Tk()
mm = tkinter.Frame(m)

mm.pack()

m.title('Best chat in the neighborhood')
# Set a fixed size for the Chat window SO YOU WONT FUCK IT UP
m.geometry("450x270")

chat = tkinter.Text(mm, width=48, height=10, bg="LightBlue3")
chat.configure(state="disabled")
send_bt = tkinter.Button(m, text='Send', height=1, width=15, command=lambda: client.send(client_message_box, m))
scroll_bar = tkinter.Scrollbar(mm, orient="vertical")
scroll_bar.config(command=chat.yview)
client_message_box = tkinter.Text(m, width=50, height=3)

chat.pack(side="left", fill="y")
scroll_bar.pack(side="right", fill="y")
client_message_box.pack()
send_bt.pack()

receive_thread = Thread(target=lambda: client.receive(chat))
receive_thread.start()

m.protocol("WM_DELETE_WINDOW", lambda: client.on_closing(m))

m.mainloop()

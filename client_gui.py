
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
m.title('Best chat in the neighborhood')

send_bt = tkinter.Button(m, text='Send', height=3, width=9, command=lambda: client.send(client_message_box, m))
scroll_bar = tkinter.Scrollbar(mm)
chat = tkinter.Listbox(mm, width=50, height=10, bg='ghost white', yscrollcommand=scroll_bar.set)

client_message_box = tkinter.Text(m, width=50, height=3)

send_bt.grid(row=1, column=1)
chat.grid(row=0, column=0)

client_message_box.grid(row=1, column=0)

scroll_bar.grid(row=0, column=0)

mm.grid(row=0, column=0)

receive_thread = Thread(target=lambda: client.receive(chat))
receive_thread.start()

m.protocol("WM_DELETE_WINDOW", lambda: client.on_closing(m))

m.mainloop()

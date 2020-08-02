from tkinter import *

root = Tk()
root.geometry('260x80')
root.title('Henji Messenger')

label1 = Label(text='Enter your Name')
client_name = Entry(justify='center')
connect_btn = Button(text='Connect')

label1.pack()
client_name.pack()
connect_btn.pack()

root.mainloop()


from tkinter import *

root = Tk()

root.geometry('500x300')
root.title("Henji Messenger App")
root.resizable(0, 0)

send_text_btn = Button(root, height=3, width=9, text="Send")
user_message_box = Text(root, width=50, height=3)
# Centering the the windows
label1 = Label(text="  ")
chat = Text(root,state=DISABLED, width=50, height=10, bg='ghost white')


label1.grid(row=0, column=0)
user_message_box.grid(row=5, column=50)
send_text_btn.grid(row=5, column=51)
chat.grid(row=4, column=50)

root.mainloop()

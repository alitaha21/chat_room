import socket
from _thread import start_new_thread
from tkinter import Tk, Button, Label, Entry, END

host = "127.0.0.1"
port = 8080

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))

window = Tk()
window.title("Client-Server Chat: Chatting")
window.geometry("500x150")

entry = Entry(window, width="83")
entry.grid(column = 3, row = 1)

label = Label(window)
label.grid(column=3, row=4)

def submit():
    message = entry.get()
    client_socket.send(message.encode('utf-8'))    
    entry.delete(0, END)    

button = Button(window, width=7, height=1, bg="blue", text="Send", fg="black", command=submit)
button.grid(column = 3,  row = 2)

def message_receive(client_socket):
    while True:
        message_received = client_socket.recv(2048)
        label["text"] = f"Server: {message_received.decode('utf-8')}"
start_new_thread(message_receive, (client_socket,))
window.mainloop()
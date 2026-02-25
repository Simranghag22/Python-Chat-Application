#Importing the required modules

import socket
from tkinter import*

#defining a function to send message to Client

def send(listbox,entry):
    message=entry.get()
    listbox.insert('end',"Server:"+ message)      #Display message in Listbox
    entry.delete(0,END)                           #Clear entry box after sending
    client.send(bytes(message, "utf-8"))          #Send message to client

#defining a function to recieve message from Client

def recieve(listbox):
    message_from_client = client.recv(50)       #Recive 50 bytes
    listbox.insert('end',"Client:"+ message_from_client.decode("utf-8"))  #decode bytes to string and displays it in Listbox

    #print("Client" + message_from_client.decode("utf-8"))


#Creating GUI Window

root = Tk()                 #Create main window

#Creating GUI Widgets

#Entry Widget
entry = Entry()
entry.pack(side=BOTTOM)

#Listbox(To display message)
listbox = Listbox(root)
listbox.pack()

#Send Button
button = Button(root, text = "Send", command = lambda:send(listbox,entry))
button.pack(side = BOTTOM)

#Receive Button
rbutton = Button(root, text = "Recieve", command = lambda:recieve(listbox))
rbutton.pack(side = BOTTOM)

root.title("Server")        # Set window title


# Creating Socket Server
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#Allow the reuse of address
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,True)

HOST_NAME = socket.gethostname()
PORT = 12345

#Bind socket to host and port

s.bind((HOST_NAME,PORT))
s.listen(4)
client,address = s.accept()

#Start GUI Main Loop

root.mainloop()

#while True:
    #message_from_client = client.recv(50)
    #print("Client" + message_from_client.decode("utf-8"))
    #message=input("Server:")
    #client,address = s.accept()
    #client.send(bytes("Hey there, whats up?","utf-8"))
    #client.send(bytes("How there, I am learning to code, I am very confident.","utf-8"))
    #client.send(bytes(message,"utf-8"))




    #print(address)
    #client.close()


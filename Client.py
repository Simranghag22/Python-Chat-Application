#Importing the required modules
import socket
from tkinter import*

#Function to Send Message to Server
def send(listbox,entry):
    message=entry.get()
    listbox.insert('end',"Client:"+ message)
    entry.delete(0,END)
    s.send(bytes(message, "utf-8"))
    recieve(listbox)

#Function to Receive Message from Server
def recieve(listbox):
    message = s.recv(50)              # Receive up to 50 bytes from server
    listbox.insert('end',"server: " + message.decode("utf-8"))

#Create GUI Window
root = Tk()

#Create GUI Widgets
entry = Entry()
entry.pack(side=BOTTOM)

listbox = Listbox(root)
listbox.pack()

button = Button(root, text = "Send", command = lambda:send(listbox,entry))
button.pack(side = BOTTOM)

rbutton = Button(root, text = "Recieve", command = lambda:recieve(listbox))
rbutton.pack(side = BOTTOM)

root.title("Client")

#Create TCP Socket and Connect to Server
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

HOST_NAME = socket.gethostname()
PORT = 12345

#Connect to server
s.connect((HOST_NAME,PORT))

#Start GUI Main Loop
root.mainloop()



#msg = s.recv(100)
#msg1=s.recv(10)
#print(msg.decode('utf-8'))
#print(msg1.decode('utf-8'))


#while True:
    #message = ''
    #while True:
        #msg = s.recv(10)
        #if len(msg)<=0:
            #break
        #message += msg.decode("utf-8")
    #if len(message)>0:
        #print(message)
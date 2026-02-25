# Python-Chat-Application

# Introduction
This project implements a basic Client–Server Chat Application using Python.It demonstrates how two systems can communicate using:
- TCP Sockets
- GUI Interface
- Message Encoding/Decoding

The goal of the project is to understand networking fundamentals along with GUI programming.

# The application allows:

- Sending messages from Server to Client
- Sending messages from Client to Server
- Displaying chat messages in a graphical interface

# Technologies Used
 - Python 3.14
 - Socket(TCP Protocol)
 - Tkinter(for GUI)

# How This Project Works

## The Server:
- Creates a TCP socket
- Binds to host and port
- Listens for incoming connections
- Accepts client connection
- Sends and receives messages

## The Client:
- Creates a TCP socket
- Connects to the server
- Sends and receives messages

## Both use:
- Tk() for GUI window
- Entry widget for typing messages
- Listbox to display chat
- Button to send/receive messages

# How to Run this Project
## Step 1: Download the Project file.
- Download the .zip file.
- Go to your Downloads folder.
- Right-click on PythonProject2.zip.
- Click Extract All.
- A folder named PythonProject2 will be created.

## Step 2: Open the Project in PyCharm
- Open PyCharm.
- Click Open.
- Select the extracted PythonProject2 folder.
- Wait for the project to load.

## Step 3: Run the Files (Important Order ⚠️)

- Run Server.py first.
- Then run Client.py.

## Step 4: Start Chatting 💬
- Two GUI windows will appear on the screen.
- In the Server window: Type a message -> Click Send.
- In the Client window: Click Receive to see the message.
- You can also send messages from the client to the server in the same way.







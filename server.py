import socket,threading

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('',50564))
s.listen(1)
lock = threading.Lock()
print("Connect at localhost:50564")
msg = """you have entered into a telnet session. Here are your options:
1. hello
2. help
3. exit
"""
class daemon(threading.Thread):
    def __init__(self, (socket,address)):
        threading.Thread.__init__(self)
        self.socket = socket
        self.address = address
    def run(self):
        self.socket.send(msg)

        while(True):
            data = self.socket.recv(2048)
            if data[0] =='1':
                data = "Hola dude"
	    elif data[0] == '2':
		data = "this is help"
	    elif data[0] == '3':
		break;
	    else:
		data = msg
            self.socket.send(data)
	self.socket.shutdown(1)
        self.socket.close()

while True:
    daemon(s.accept()).start()

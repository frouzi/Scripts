import socket
from unittest import result

from regex import D
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', 8888))
s.listen(5)
client, addr = s.accept()
while 1:
    command = str(input('Enter command:'))
    client.sent(command.encode())
    if command.lower() == 'exit':
        break
    result_output = client.recv(4096).decode()
    print(result_output)
client.close()
s.close()
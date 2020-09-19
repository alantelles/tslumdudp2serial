# python
# server UDP que captura os eventos de tally e envia para a porta serial especificada
# porta serial precisa ser passada no parâmetro 1
# Uso: python [udp_port] [serial_port] 

import socket, serial, sys

ip = ""
try:
    port = int(sys.argv[1])

except:
    raise Exception('UDP listening port not specified')

buffer = 1024

sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
sock.bind((ip, port))
print("UDP server up and listening all incoming at port:", port)

try:
    ser_port = sys.argv[2]

except:
    raise Exception ('Serial port not specified')

ser = serial.Serial(ser_port, 9600)

try:
    while(True):
        bytes_addr = sock.recvfrom(buffer)
        message = bytes_addr[0]
        cam = message[0] - 0x80
        status = bin(message[1])[2:]
        tally_state = hex(message[1])
        # print(tally_state)
        if tally_state == '0x31':
            status = 'ON'

        elif tally_state == '0x30':
            status = 'OFF'

        else:
            status = 'Hello! I\'m up'
        
        print('Cam: {}, status: {}'.format(cam, status))
        # print(message)
        ser.write(message)

finally:
    ser.close()
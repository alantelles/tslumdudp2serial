import socket, time, random

SERVER_ADDRESS_PORT = ("localhost", 8900)

# Create a UDP socket at client side
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

def hex_print(byte_seq):
    for b in byte_seq:
        print(hex(b), end=' ')
    print('')

def get_message(cam, status):
    bmsg = [0x80 + cam]
    text = 'CAM ' + str(cam) +' '
    if status:
        text += 'ON '
    else:
        text += 'OFF'
    text += '       '
    
    status = 0x31 if status else 0x30
    bmsg.append(status)
    # bmsg.extend([0x63, 0x63, 0x63, 0x63, 0x63, 0x63, 0x63, 0x63, 0x63, 0x63, 0x63, 0x63, 0x63, 0x63, 0x63, 0x63])
    for t in text:
        bmsg.append(int.from_bytes(t.encode(), byteorder='big'))
    return bmsg

def send_message(seq):
    # Send to server using created UDP socket
    UDPClientSocket.sendto(seq, SERVER_ADDRESS_PORT)        

last = 0
for i in range(5):
    msg = get_message(i+1, False)
    send_message(bytearray(msg))

while True:
    now = random.randrange(5) + 1
    while now == last:
        now = random.randrange(5) + 1
    print('Change:', now)
    on = get_message(now, True)
    off = get_message(last, False)
    last = now
    hex_print(on)
    send_message(bytearray(on))
    wipe = random.randrange(9)
    if wipe == 7:
        m = random.randrange(6) + 1
        print('wipe:', m)
        time.sleep(m)
    hex_print(off)
    send_message(bytearray(off))
    
    print()
    time.sleep(2)

#client.py

import socket
import sys
def send_message(message):
    client = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
    client.connect(("10:f6:0a:fe:46:37",8 ))

    try:
        client.send(message.encode("utf-8"))
    
    except OSError as e:
        print(f"Error: {e}")

    finally:
        client.close()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        # print("Usage: python client.py <message>")
        sys.exit(1)
    msg = sys.argv[1]
    send_message(msg)

import sys
import socket

def main():
    # Meminta input host, port, dan file dari pengguna
    host = input("Masukkan alamat host: ")
    port = int(input("Masukkan port: "))
    filename = input("Masukkan nama file: ")

    # First try-except block -- create socket
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as e:
        print("Error creating socket: %s" % e)
        sys.exit(1)
        
    # Second try-except block -- connect to the given host/port
    try:
        s.connect((host, port))
    except socket.gaierror as e:
        print("Address-related error connecting to server: %s" % e)
        sys.exit(1)
    except socket.error as e:
        print("Connection error: %s" % e)
        sys.exit(1)

    # Third try-except block -- sending data
    try:
        msg = "GET %s HTTP/1.0\r\n\r\n" % filename
        s.sendall(msg.encode('utf-8'))
    except socket.error as e:
        print("Error sending data: %s" % e)
        sys.exit(1)

    while True:
        # Fourth try-except block -- waiting to receive data from the remote host
        try:
            buf = s.recv(2048)
        except socket.error as e:
            print("Error receiving data: %s" % e)
            sys.exit(1)
        if not len(buf):
            break
        # Write the received data
        sys.stdout.write(buf.decode('utf-8'))

if __name__ == '__main__':
    main()

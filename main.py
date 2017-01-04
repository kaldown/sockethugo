import socket
import os

PORT = int(os.environ['PORT'])

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('localhost', PORT))
        s.listen(1)
        conn, addr = s.accept()
        with conn:
            print('connected by', addr)
            while True:
                data = conn.recv(1024)
                if not data:
                    s.close()
                    break
                conn.sendall(data)

if __name__ == '__main__':
    main()
    

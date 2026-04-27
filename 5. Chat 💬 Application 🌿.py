# chat_server.py
import socket
import threading

HOST = '127.0.0.1'
PORT = 65432

def receive_messages(conn, addr):
    while True:
        try:
            message = conn.recv(1024).decode('utf-8')
            if not message:
                break
            print(f"{addr[0]}: {message}")
        except:
            break
    conn.close()

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()
    print(f"Server listening on {HOST}:{PORT}")

    while True:
        conn, addr = server.accept()
        print(f"New connection from {addr}")
        thread = threading.Thread(target=receive_messages, args=(conn, addr))
        thread.start()

if __name__ == "__main__":
    main()
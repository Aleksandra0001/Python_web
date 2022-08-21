import socket
from threading import Thread

HOSTNAME = socket.gethostname()
SERVER_IP = socket.gethostbyname(HOSTNAME)
SERVER_PORT = 5005
separator_token = '<SEP> '

s = socket.socket()
client_sockets = set()


def handle_client(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode()
            message = message.replace(separator_token, ': ')
            print(f"[*]-{client_socket.getpeername()} Received message: {message}")
            for client_socket in client_sockets:
                client_socket.send(message.encode())
        except Exception as e:
            print(f"[-] {client_socket.getpeername()} is disconnected. - {e}")
            client_sockets.remove(client_socket)
            break


def run_server():
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((SERVER_IP, SERVER_PORT))
    s.listen(10)
    print(f"[*] Listening as {HOSTNAME}:{SERVER_PORT}")
    while True:
        client_socket, client_address = s.accept()
        print(f"[*] Connection from {client_address}")
        client_sockets.add(client_socket)
        t = Thread(target=handle_client, args=(client_socket,))
        t.start()


if __name__ == '__main__':
    run_server()
    for cs in client_sockets:
        cs.close()
    s.close()

import socket
from threading import Thread

SERVER_HOST = "0.0.0.0"
SERVER_PORT = 5002
separator_token = "<SEP>"


def start_server():
    client_sockets = set()

    def listen_for_client(client_socket: socket.socket):
        while True:
            try:
                msg = client_socket.recv(1024).decode()
                if not msg:
                    print(f"[-] Client {client_socket.getpeername()} is offline")
                    client_sockets.remove(client_socket)
                    break
                else:
                    msg = msg.replace(separator_token, ": ")
                    print(f"[+] Received message from {client_socket.getpeername()}: {msg}")

                for cs in client_sockets:
                    cs.send(msg.encode())

            except Exception as e:
                print(f"[!] Error: {e}")
                client_sockets.remove(client_socket)

    s = socket.socket()
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((SERVER_HOST, SERVER_PORT))
    s.listen(5)
    print(f"[*] Listening as {SERVER_HOST}:{SERVER_PORT}")

    try:
        while True:
            client_socket, client_address = s.accept()
            print(f"[+] {client_address} connected.")
            client_sockets.add(client_socket)
            t = Thread(target=listen_for_client, args=(client_socket,), daemon=True)
            t.start()
    except Exception as e:
        print(f"[!] Server error: {e}")
        for cs in client_sockets:
            cs.close()
        s.close()


if __name__ == "__main__":
    start_server()
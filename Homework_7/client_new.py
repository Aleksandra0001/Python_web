import socket
import random
from threading import Thread
from datetime import datetime
from colorama import Fore, init, Back

init()

colors = [Fore.BLUE, Fore.CYAN, Fore.GREEN, Fore.LIGHTBLACK_EX,
          Fore.LIGHTBLUE_EX, Fore.LIGHTCYAN_EX, Fore.LIGHTGREEN_EX,
          Fore.LIGHTMAGENTA_EX, Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX,
          Fore.LIGHTYELLOW_EX, Fore.MAGENTA, Fore.RED, Fore.WHITE, Fore.YELLOW
          ]

client_color = random.choice(colors)

SERVER_HOST = "127.0.0.1"
SERVER_PORT = 5002
separator_token = "<SEP>"


def start_client():
    def listen_for_messages():
        while True:
            msg = s.recv(1024).decode()
            print(msg)

    s = socket.socket()
    print(f"[*] Connecting to {SERVER_HOST}:{SERVER_PORT}...")
    s.connect((SERVER_HOST, SERVER_PORT))
    print("[+] Connected.")

    name = input(f"{Fore.GREEN}Enter your name: ")

    t = Thread(target=listen_for_messages, daemon=True)
    t.start()

    try:
        while True:
            message = input(f'{Fore.GREEN}>>> ')
            if message.lower() == 'q':
                break

            date_now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            message = f"{client_color}[{date_now}] {name}{separator_token}{message}{Fore.RESET}"
            s.send(message.encode())
    except KeyboardInterrupt:
        print(f"[*] Disconnected from {SERVER_HOST}:{SERVER_PORT}.")
        s.close()
    except Exception as e:
        print(f"[*] Disconnected from {SERVER_HOST}:{SERVER_PORT}. Error: {e}")
        s.close()


if __name__ == "__main__":
    start_client()
import socket
import random
from threading import Thread
from colorama import init, Fore, Back, Style
from datetime import datetime

init()
colors = [Fore.BLUE, Fore.CYAN, Fore.GREEN, Fore.LIGHTBLACK_EX,
          Fore.LIGHTBLUE_EX, Fore.LIGHTCYAN_EX, Fore.LIGHTGREEN_EX,
          Fore.LIGHTMAGENTA_EX, Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX,
          Fore.LIGHTYELLOW_EX, Fore.MAGENTA, Fore.RED, Fore.WHITE, Fore.YELLOW
          ]

client_color = random.choice(colors)
separator_token = '<SEP> '

SERVER_IP = '127.0.0.1'
SERVER_PORT = 5005

s = socket.socket()


def waiting_for_messages():
    while True:
        try:
            message = s.recv(1024).decode()
            print(f"[*] Received message: {message}")
        except Exception as e:
            print(f"[-] Error: {e}")
            break


def send_message(name):
    while True:
        try:
            message = input(f'{client_color}>>> ')
            date_now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            message = f"{client_color}[{date_now}] {name}{separator_token}{message}{Fore.RESET}"
            s.send(message.encode())
        except Exception as e:
            print(f"[-] Error: {e}")
            break


def run_client():
    print(f"[*] Connecting to {SERVER_IP}:{SERVER_PORT}...")
    s.connect((SERVER_IP, SERVER_PORT))
    print("[+] Connected.")
    name = input(f"{Fore.LIGHTGREEN_EX}Enter your name:{Fore.RESET} ")

    t1 = Thread(target=waiting_for_messages, daemon=True)
    t1.start()

    t2 = Thread(target=send_message, args=(name,), daemon=True)
    t2.start()

    t1.join()
    t2.join()


if __name__ == '__main__':
    run_client()
    s.close()

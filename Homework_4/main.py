from pathlib import Path
import file_parser as parser


def start():
    path = input("Enter path to folder: ").strip()
    if len(path) < 1:
        print("Path is empty.Try again!")
        start()
    if not Path(path).exists():
        print("Path is not exists.Try again!")
        start()
    else:
        folder_path = Path(path)
        folder = folder_path.resolve()
        parser.scan(folder)
        parser.handlers_switcher(folder)
        print('Done!')


if __name__ == '__main__':
    start()

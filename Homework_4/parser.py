import shutil
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
from normalize import normalize
from time import sleep
from random import random


def folder_parse(folder: Path) -> None:
    for item in folder.iterdir():
        if item.is_dir():
            folder_parse(item)
        else:
            file_parse(item, folder)


def file_parse(file: Path, folder: Path) -> None:
    with ThreadPoolExecutor(max_workers=10) as executor:
        if not file.suffix:
            executor.submit(handle_other, file, folder)
        if file.suffix in ('.jpeg', '.jpg', '.png', '.svg'):
            print(f"start 1 {file}")
            sleep(random())
            future = executor.submit(handle_media, file, folder / 'images')
            future.result()
            print(f"end 1 {file}")
        if file.suffix in ('.mp3', '.ogg', '.wav', '.amr'):
            print(f"start 2 {file}")
            sleep(random())
            future = executor.submit(handle_media, file, folder / 'audio')
            future.result()
            print(f"end 2 {file}")
        # if file.suffix in ('.pdf', '.doc', '.docx', '.xlsx', '.txt', '.pptx'):
        #     print(f"start 3 {file}")
        #     sleep(random())
        #     future = executor.submit(handle_documents, file, folder / 'documents')
        #     future.result()
        #     print(f"end 3 {file}")
        # if file.suffix in ('.zip', '.tar', '.gz'):
        #     print(f"start 4 {file}")
        #     sleep(random())
        #     future = executor.submit(handle_archive, file, folder / 'archives')
        #     future.result()
        #     print(f"end 4 {file}")
        # if file.suffix in ('.mp4', '.avi', '.mkv', '.mov'):
        #     print(f"start 5 {file}")
        #     sleep(random())
        #     future = executor.submit(handle_media, file, folder / 'video')
        #     future.result()
        #     print(f"end 5 {file}")
        else:
            print(f"start 6 {file}")
            sleep(random())
            future = executor.submit(handle_other, file, folder / 'unknown')
            future.result()
            print(f"end 6 {file}")


def handle_media(filename: Path, target_folder: Path):
    target_folder.mkdir(exist_ok=True, parents=True)
    filename.replace(target_folder / normalize(filename.name))


def handle_documents(filename: Path, target_folder: Path):
    target_folder.mkdir(exist_ok=True, parents=True)
    filename.replace(target_folder / normalize(filename.name))


def handle_other(filename: Path, target_folder: Path):
    target_folder.mkdir(exist_ok=True, parents=True)
    filename.replace(target_folder / normalize(filename.name))


def handle_archive(filename: Path, target_folder: Path):
    target_folder.mkdir(exist_ok=True, parents=True)
    folder_for_file = target_folder / normalize(filename.name.replace(filename.suffix, ''))
    folder_for_file.mkdir(exist_ok=True, parents=True)
    try:
        shutil.unpack_archive(str(filename.resolve()), str(folder_for_file.resolve()))
    except shutil.ReadError:
        print(f'Обман - это не архив {filename}!')
        folder_for_file.rmdir()
        return None
    filename.unlink()

import asyncio
from parser import folder_parse
from aiopath import AsyncPath
from time import time


async def start():
    path = input("Enter path to folder: ").strip()
    folder = AsyncPath(path)
    if await folder.exists() and len(path) > 0:
        try:
            start_time = time()
            await folder_parse(folder, folder)
            print("Done!")
            print(f'Time: {time() - start_time}')
        except Exception as e:
            print(f'Error: {e}')
    else:
        print("Folder not found. Please, try again.")
        await start()


if __name__ == '__main__':
    asyncio.run(start())

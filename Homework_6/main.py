import parser as parser
from aiopath import AsyncPath


async def start():
    path = input("Enter path to folder: ").strip()
    print(f'You entered {type(path)}')
    folder = AsyncPath(path)
    if await folder.exists() and len(path) > 0:
        try:
            await parser.folder_parse(folder, folder)
            print("Done!")
        except Exception as e:
            print(f"Error: {e}")
    else:
        print("Folder not found. Please, try again.")
        await start()


if __name__ == '__main__':
    import asyncio

    asyncio.run(start())

import asyncio
import shutil
from aiopath import AsyncPath
from normalize import normalize
from aiologger import Logger

# logger = Logger.with_default_handlers(name='parser', level='INFO')


async def folder_parse(source_folder: AsyncPath, output_folder: AsyncPath) -> None:
    tasks = []
    async for item in source_folder.iterdir():
        if await item.is_dir():
            # await logger.info(f'Start parsing folder {item}')
            tasks.append(asyncio.create_task(folder_parse(item, output_folder)))
        else:
            # await logger.info(f'Start copying file {item}')
            tasks.append(asyncio.create_task(copy_file(item, output_folder)))

    await asyncio.gather(*tasks)

    if output_folder != source_folder:
        await handle_delete_folder(source_folder)


async def copy_file(file: AsyncPath, output_folder: AsyncPath) -> None:
    file_folder = file.suffix[1:].upper()
    if file.suffix in ('.jpeg', '.jpg', '.png', '.svg'):
        await handle_media(file, output_folder / 'Images' / file_folder)
    elif file.suffix in ('.mp3', '.ogg', '.wav', '.amr'):
        await handle_media(file, output_folder / 'Audio' / file_folder)
    elif file.suffix in ('.mp4', '.avi', '.mkv', '.mov'):
        await handle_media(file, output_folder / 'Video' / file_folder)
    elif file.suffix in ('.pdf', '.doc', '.docx', '.xlsx', '.txt', '.pptx', '.xml'):
        await handle_documents(file, output_folder / 'Documents' / file_folder)
    elif file.suffix in ('.zip', '.tar', '.gz'):
        await handle_archive(file, output_folder / 'Archives')
    else:
        await handle_other(file, output_folder / 'Trash')


async def handle_media(filename: AsyncPath, target_folder: AsyncPath):
    await target_folder.mkdir(exist_ok=True, parents=True)
    await filename.replace(str(target_folder / normalize(filename.name)))


async def handle_documents(filename: AsyncPath, target_folder: AsyncPath):
    await target_folder.mkdir(exist_ok=True, parents=True)
    await filename.replace(str(target_folder / normalize(filename.name)))


async def handle_other(filename: AsyncPath, target_folder: AsyncPath):
    await target_folder.mkdir(exist_ok=True, parents=True)
    await filename.replace(str(target_folder / normalize(filename.name)))


async def handle_archive(filename: AsyncPath, target_folder: AsyncPath):
    await target_folder.mkdir(exist_ok=True, parents=True)
    folder_for_file = target_folder / normalize(filename.name.replace(filename.suffix, ''))
    await folder_for_file.mkdir(exist_ok=True, parents=True)
    try:
        shutil.unpack_archive(str(filename), str(folder_for_file))
    except shutil.ReadError:
        print(f'{filename} is not a archive!')
        await folder_for_file.rmdir()
        return None
    await filename.unlink()


async def handle_delete_folder(folder: AsyncPath):
    # await logger.info(f'Start deleting {folder}')
    if await folder.is_dir():
        try:
            await folder.rmdir()
        except OSError:
            print(f'Folder {folder} was not deleted!')
    else:
        print(f'{folder} is not a folder!')

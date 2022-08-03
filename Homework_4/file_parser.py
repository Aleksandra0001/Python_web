import shutil
from pathlib import Path
from normalize import normalize


JPEG_IMAGES = []
JPG_IMAGES = []
PNG_IMAGES = []
SVG_IMAGES = []

MP3_AUDIO = []
OGG_AUDIO = []
WAV_AUDIO = []
AMR_AUDIO = []

AVI_VIDEO = []
MP4_VIDEO = []
MOV_VIDEO = []
MKV_VIDEO = []

DOC_DOCUMENTS = []
DOCX_DOCUMENTS = []
TXT_DOCUMENTS = []
PDF_DOCUMENTS = []
XLSX_DOCUMENTS = []
PPTX_DOCUMENTS = []

ARCHIVES = []

OTHER = []

REGISTER_EXTENSIONS = {
    'JPEG': JPEG_IMAGES,
    'PNG': PNG_IMAGES,
    'JPG': JPG_IMAGES,
    'SVG': SVG_IMAGES,
    'MP3': MP3_AUDIO,
    'OGG': OGG_AUDIO,
    'WAV': WAV_AUDIO,
    'AMR': AMR_AUDIO,
    'AVI': AVI_VIDEO,
    'MP4': MP4_VIDEO,
    'MOV': MOV_VIDEO,
    'MKV': MKV_VIDEO,
    'DOC': DOC_DOCUMENTS,
    'DOCX': DOCX_DOCUMENTS,
    'TXT': TXT_DOCUMENTS,
    'PDF': PDF_DOCUMENTS,
    'XLSX': XLSX_DOCUMENTS,
    'PPTX': PPTX_DOCUMENTS,
    'ZIP': ARCHIVES,
    'GZ': ARCHIVES,
    'TAR': ARCHIVES
}

FOLDERS = []
EXTENSIONS = set()
UNKNOWN = set()


def get_extension(filename: str) -> str:
    return Path(filename).suffix[1:].upper()


def scan(folder: Path) -> None:
    # with ThreadPoolExecutor(max_workers=5) as executor:
        for item in folder.iterdir():
            if item.is_dir():
                if item.name not in ('archives', 'video', 'audio', 'documents', 'images', 'OTHER'):
                    FOLDERS.append(item)
                    # print(f'Папка {item} добавлена в очередь')
                    # sleep(randint(0, 5))
                    # future = executor.submit(scan, item)
                    # future.result()
                    # print(f'Папка {item} просканирована')
                    scan(item)
                continue
            ext = get_extension(item.name)
            fullname = folder / item.name
            if not ext:
                OTHER.append(fullname)
            else:
                try:
                    container = REGISTER_EXTENSIONS[ext]
                    EXTENSIONS.add(ext)
                    container.append(fullname)
                except KeyError:
                    UNKNOWN.add(ext)
                    OTHER.append(fullname)


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
    folder_for_file = target_folder / \
                      normalize(filename.name.replace(filename.suffix, ''))

    folder_for_file.mkdir(exist_ok=True, parents=True)
    try:
        shutil.unpack_archive(str(filename.resolve()),
                              str(folder_for_file.resolve()))
    except shutil.ReadError:
        print(f'Обман - это не архив {filename}!')
        folder_for_file.rmdir()
        return None
    filename.unlink()


def handle_delete_folder(folder: Path):
    try:
        folder.rmdir()
    except OSError:
        print(f'Не удалось удалить папку {folder}')


def handlers_switcher(folder: Path):
        for file in JPEG_IMAGES:
            handle_media(file, folder / 'images' / 'JPEG')
        for file in JPG_IMAGES:
            handle_media(file, folder / 'images' / 'JPG')
        for file in PNG_IMAGES:
            handle_media(file, folder / 'images' / 'PNG')
        for file in SVG_IMAGES:
            handle_media(file, folder / 'images' / 'SVG')

        for file in MP3_AUDIO:
            handle_media(file, folder / 'audio' / 'MP3')
        for file in OGG_AUDIO:
            handle_media(file, folder / 'audio' / 'OGG')
        for file in WAV_AUDIO:
            handle_media(file, folder / 'audio' / 'WAV')
        for file in AMR_AUDIO:
            handle_media(file, folder / 'audio' / 'AMR')

        for file in MP4_VIDEO:
            handle_media(file, folder / 'video' / 'MP4')
        for file in MOV_VIDEO:
            handle_media(file, folder / 'video' / 'MOV')
        for file in AVI_VIDEO:
            handle_media(file, folder / 'video' / 'AVI')
        for file in MKV_VIDEO:
            handle_media(file, folder / 'video' / 'MKV')

        for file in DOC_DOCUMENTS:
            handle_documents(file, folder / 'documents' / 'DOC')
        for file in DOCX_DOCUMENTS:
            handle_documents(file, folder / 'documents' / 'DOCX')
        for file in TXT_DOCUMENTS:
            handle_documents(file, folder / 'documents' / 'TXT')
        for file in PDF_DOCUMENTS:
            handle_documents(file, folder / 'documents' / 'PDF')
        for file in XLSX_DOCUMENTS:
            handle_documents(file, folder / 'documents' / 'XLSX')
        for file in PPTX_DOCUMENTS:
            handle_documents(file, folder / 'documents' / 'PPTX')

        for file in OTHER:
            handle_other(file, folder / 'OTHER')

        for file in ARCHIVES:
            handle_archive(file, folder / 'archives')

        for folder in FOLDERS[::-1]:
            handle_delete_folder(folder)

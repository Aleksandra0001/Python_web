import shutil
from pathlib import Path
from normalize import normalize
from concurrent.futures import ThreadPoolExecutor


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
    for item in folder.iterdir():
        if item.is_dir():
            if item.name not in ('archives', 'video', 'audio', 'documents', 'images', 'OTHER'):
                FOLDERS.append(item)
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
    filename.replace(target_folder / filename.name)


def handle_documents(filename: Path, target_folder: Path):
    target_folder.mkdir(exist_ok=True, parents=True)
    filename.replace(target_folder / filename.name)


def handle_other(filename: Path, target_folder: Path):
    target_folder.mkdir(exist_ok=True, parents=True)
    filename.replace(target_folder / filename.name)


def handle_archive(filename: Path, target_folder: Path):
    target_folder.mkdir(exist_ok=True, parents=True)
    folder_for_file = target_folder / filename.name.replace(filename.suffix, '')

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
    with ThreadPoolExecutor(max_workers=10) as executor:
        features = []
        for feature in features:
            feature.result()

        for file in JPEG_IMAGES:
            features.append(executor.submit(handle_media, file, folder / 'images'/'JPEG'))
        for file in JPG_IMAGES:
            features.append(executor.submit(handle_media, file, folder / 'images'/'JPG'))
        for file in PNG_IMAGES:
            features.append(executor.submit(handle_media, file, folder / 'images'/'PNG'))
        for file in SVG_IMAGES:
            features.append(executor.submit(handle_media, file, folder / 'images'/'SVG'))

        for file in MP3_AUDIO:
            features.append(executor.submit(handle_media, file, folder / 'audio'/'MP3'))
        for file in OGG_AUDIO:
            features.append(executor.submit(handle_media, file, folder / 'audio'/'OGG'))
        for file in WAV_AUDIO:
            features.append(executor.submit(handle_media, file, folder / 'audio'/'WAV'))
        for file in AMR_AUDIO:
            features.append(executor.submit(handle_media, file, folder / 'audio'/'AMR'))

        for file in MP4_VIDEO:
            features.append(executor.submit(handle_media, file, folder / 'video'/'MP4'))
        for file in MOV_VIDEO:
            features.append(executor.submit(handle_media, file, folder / 'video'/'MOV'))
        for file in AVI_VIDEO:
            features.append(executor.submit(handle_media, file, folder / 'video'/'AVI'))
        for file in MKV_VIDEO:
            features.append(executor.submit(handle_media, file, folder / 'video'/'MKV'))

        for file in DOC_DOCUMENTS:
            features.append(executor.submit(handle_documents, file, folder / 'documents'/'DOC'))
        for file in DOCX_DOCUMENTS:
            features.append(executor.submit(handle_documents, file, folder / 'documents'/'DOCX'))
        for file in TXT_DOCUMENTS:
            features.append(executor.submit(handle_documents, file, folder / 'documents'/'TXT'))
        for file in PDF_DOCUMENTS:
            features.append(executor.submit(handle_documents, file, folder / 'documents'/'PDF'))
        for file in XLSX_DOCUMENTS:
            features.append(executor.submit(handle_documents, file, folder / 'documents'/'XLSX'))
        for file in PPTX_DOCUMENTS:
            features.append(executor.submit(handle_documents, file, folder / 'documents'/'PPTX'))

        for file in OTHER:
            features.append(executor.submit(handle_other, file, folder / 'my other'))

        for file in ARCHIVES:
            features.append(executor.submit(handle_archive, file, folder / 'archives'))

        for folder in FOLDERS[::-1]:
            features.append(executor.submit(handle_delete_folder, folder))
            handle_delete_folder(folder)

#!/usr/bin/env python3

from os import scandir
from pathlib import Path

SUBDIRECTORIES = {
    "DOCUMENTS": ['.pdf', '.rtf', '.txt'],
    "AUDIO": ['.m4a', '.m4b', '.mp3'],
    "VIDEOS": ['.mov', '.avi', '.mp4', '.mkv', '.m4v'],
    "IMAGES": ['.jpg', '.jpeg', '.png'],
    "ARCHIVES": ['.zip', '.rar', '.tar', '.gz']
}

def pickDir(value):
    for category, suffixes in SUBDIRECTORIES.items():
        for suffix in suffixes:
            if suffix == value:
                return category
    return 'MISC'

def orginizeDir(*args):
    numargs = len(args)

    # initialize parameters
    if numargs < 1:
        raise TypeError(f'expected at least 1 argument, got {numargs}')
    elif numargs == 1:
        directory = args[0]
        mode = 'r'
    elif numargs == 2:
        (directory, mode) = args
        if mode not in ('r', 'w'):
            raise ValueError(f'expecting "r" - to read or "w" to write directories')
    else: 
        raise TypeError(f'expected at most 2 arguments, got {numargs}')
    
    try:
        scandir(directory)
    except Exception:
        print(f'either you specify not a directory or directory doesn\'t exists')
    else:
        # if we need to read files and check their category
        if mode == 'r':
            filesWithTypes = dict()
            for item in scandir(directory):
                fileType = Path(item).suffix.lower()
                filesWithTypes.setdefault(pickDir(fileType), [])
                filesWithTypes[pickDir(fileType)].append(item.name)
            return filesWithTypes
        # if we need to create new directories and write files there
        elif mode == 'w':
            for item in scandir(directory):
                filePath = Path(item)
                fileType = filePath.suffix.lower()
                newDir = pickDir(fileType)
                directoryPath = Path(directory + newDir)
                if directoryPath.is_dir() != True:
                    directoryPath.mkdir()
                filePath.rename(directoryPath.joinpath(filePath.name))
                
def main():
    downloads = orginizeDir('../../Documents/TESTING/', 'r')
    print(downloads['VIDEOS'])
    
    #orginizeDir('../../Documents/TESTING/', 'w')

if __name__ == '__main__':
    main()

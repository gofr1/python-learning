import os 
from os import path
import shutil
from shutil import make_archive
from zipfile import ZipFile

some_file = "somefile.txt"
new_file = "anotherfile.txt"
zip_file = "test.zip"
zip_file_base = "somearchive"

all_files = list([some_file, new_file, zip_file, zip_file_base+'.zip', some_file+'.bak'])

with open(some_file, 'w+') as fout:
    fout.write("Hello world!")

# create a copy of file
if path.exists(some_file):
    # get the path of the file
    src = path.realpath(some_file)

    # lets make a backup copy
    dst = src + '.bak'

    # copy 
    shutil.copy(src, dst)
    shutil.copystat(src, dst)

    # rename
    os.rename(some_file, new_file)
    os.rename(new_file, some_file)

    # put it in archive
    root_dir, tail = path.split(src)
    shutil.make_archive(base_name=zip_file_base, format="zip", root_dir= root_dir)

    # more fine-grained control over zip
    with ZipFile(zip_file, "w") as newzip:
        newzip.write(some_file)
        newzip.write(some_file+'.bak')

# clear
for fl in all_files:
    os.remove(fl) if path.exists(fl) else None

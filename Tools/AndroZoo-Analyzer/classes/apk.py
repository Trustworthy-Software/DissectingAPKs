import io
import zipfile

from .file import File
from contextlib import closing
from collections import Counter


# ---------------------------------------------------------------------- #

# Returns list of files from API response
def unpack(response):
    files = []
    try:
        with closing(response), zipfile.ZipFile(io.BytesIO(response.content)) as z:
            for f in z.filelist:
                try:
                    if f.file_size > 0:
                        try:
                            with zipfile.ZipFile(io.BytesIO(z.read(f))) as zz:
                                print(f"{f.filename} - File is a zip file")
                                files.append(File(f, z.read(f), compressed=True))
                                files.extend([File(ff, zz.read(ff), in_compressed=f.filename.split(".")[-1])
                                              for ff in zz.filelist if ff.file_size > 0])
                        except zipfile.BadZipfile:
                            files.append(File(f, z.read(f)))
                except:
                    pass
    except zipfile.BadZipfile:
        pass
    return files


# Returns dictionary type/language - count
def count_by_magic_and_extension(files):
    return dict(Counter(file.magic_type for file in files)), \
        dict(Counter(file.mime_type for file in files)), \
        dict(Counter(file.encoding for file in files)), \
        dict(Counter(file.extension for file in files))


# Returns dictionary type/language - added size
def size_by_magic_and_extension(files):
    dict1 = {}
    dict2 = {}
    dict3 = {}
    dict4 = {}
    for file in files:
        if file.magic_type not in dict1:
            dict1.setdefault(file.magic_type, 0)
        if file.mime_type not in dict2:
            dict2.setdefault(file.mime_type, 0)
        if file.encoding not in dict3:
            dict3.setdefault(file.encoding, 0)
        if file.extension not in dict4:
            dict4.setdefault(file.extension, 0)
        dict1[file.magic_type] += file.size
        dict2[file.mime_type] += file.size
        dict3[file.encoding] += file.size
        dict4[file.extension] += file.size
    return dict1, dict2, dict3, dict4


# ---------------------------------------------------------------------- #

class APK:
    def __init__(self, info, response):
        self.info = info
        self.response = response
        self.files = []
        self.counts = {}
        self.sizes = {}
        self.relations = {}

    def analyze(self):
        self.files = unpack(self.response)
        self.counts = count_by_magic_and_extension(self.files)
        self.sizes = size_by_magic_and_extension(self.files)
        self.relations = dict(Counter([f.relation for f in self.files]))

    def __str__(self):
        return ("=================================================================\n"
                + self.info[0] + "\n"
                + "=================================================================\n")

# ---------------------------------------------------------------------- #


import os
import magic
import pathlib

from .magic_type import MagicType


# ---------------------------------------------------------------------- #

# Returns file name
def get_name(path):
    return os.path.basename(path)


# Returns name, mime_type and encoding from content
def get_magic(content):
    mag = magic.detect_from_content(content)
    return MagicType(mag.name).parsed_magic_type, mag.mime_type, mag.encoding


# Returns file extension from file name
def get_extensions(filename, compressed, in_compressed):
    extensions = pathlib.Path(filename).suffixes
    extensions = [ext.lower() for ext in extensions]
    extension = extensions[-1] if len(extensions) else ""
    extensions = extensions + [":"] if compressed else extensions
    extensions = [in_compressed + ":"] + extensions if in_compressed else extensions
    return extension, extensions


# ---------------------------------------------------------------------- #

class File:
    def __init__(self, file, content, compressed=False, in_compressed=""):
        self.file = file
        self.content = content
        self.compressed = compressed
        self.in_compressed = in_compressed
        self.path = file.filename
        self.size = file.file_size
        self.name = get_name(self.path)
        self.magic_type, self.mime_type, self.encoding = get_magic(self.content)
        self.extension, self.extensions = get_extensions(self.name, self.compressed, self.in_compressed)
        self.relation = self.encoding + "/" + self.mime_type + "/" + self.magic_type + "/" + "".join(self.extensions)

    def __str__(self):
        return self.relation

# ---------------------------------------------------------------------- #

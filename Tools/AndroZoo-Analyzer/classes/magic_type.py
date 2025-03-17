
# ---------------------------------------------------------------------- #

def parse(raw_type):
    raw_type = raw_type.split(',')[0]
    raw_type = raw_type.split(';')[0]
    raw_type = raw_type.split(':')[0]
    raw_type = raw_type.split('/')[0]
    raw_type = raw_type.split(" -")[0]
    raw_type = raw_type.split(" (")[0]
    raw_type = raw_type.split(" [")[0]
    raw_type = raw_type.split(" \'")[0]
    raw_type = raw_type.split(" \"")[0]
    raw_type = raw_type.split(" title:")[0]
    raw_type = raw_type.split(" Title:")[0]
    raw_type = raw_type.split(" version")[0]
    raw_type = raw_type.split(" Version")[0]
    raw_type = "dBase" if "dBase" in raw_type else raw_type
    raw_type = "firmware" if "firmware" in raw_type else raw_type
    raw_type = "Linux rev" if "Linux rev" in raw_type else raw_type
    raw_type = "Git commit" if "Git commit" in raw_type else raw_type
    raw_type = "GEM Image data" if "GEM Image data" in raw_type else raw_type
    raw_type = "HA archive data" if "HA archive data" in raw_type else raw_type
    raw_type = "compress\'d data" if "compress\'d data" in raw_type else raw_type
    raw_type = "Targa image data" if "Targa image data" in raw_type else raw_type
    raw_type = "XML document" if "XML" in raw_type and "document" in raw_type else raw_type
    raw_type = "Linux/i386 core file" if "Linux/i386 core file" in raw_type else raw_type
    raw_type = "GEM NOSIG Image data" if "GEM NOSIG Image data" in raw_type else raw_type
    raw_type = "Bio-Rad .PIC Image File" if "Bio-Rad .PIC Image File" in raw_type else raw_type
    raw_type = "Apple DiskCopy 4.2 image" if "Apple DiskCopy 4.2 image" in raw_type else raw_type
    raw_type = "StarOffice Gallery theme" if "StarOffice Gallery theme" in raw_type else raw_type
    raw_type = "AppleWorks Word Processor" if "AppleWorks Word Processor" in raw_type else raw_type
    raw_type = "DOS 2.0-3.2 backed up sequence" if "DOS 2.0-3.2 backed up sequence" in raw_type else raw_type
    raw_type = "DOS EPS Binary File Postscript" if "DOS EPS Binary File Postscript" in raw_type else raw_type
    return raw_type


# ---------------------------------------------------------------------- #

class MagicType:
    def __init__(self, magic_type):
        self.raw_magic_type = magic_type
        self.parsed_magic_type = parse(magic_type)

# ---------------------------------------------------------------------- #

import io
import zipfile

from contextlib import closing
from androguard.core.bytecodes.axml import AXMLPrinter


# ---------------------------------------------------------------------- #

# Returns list of files from API response
def unpack(response):
    with closing(response), zipfile.ZipFile(io.BytesIO(response.content)) as z:
        return z.read("AndroidManifest.xml")


# ---------------------------------------------------------------------- #

class APK:
    def __init__(self, info, response):
        self.info = info
        self.response = response
        self.sdks = {}
        self.permissions = []

    def analyze(self):
        file = unpack(self.response)
        axml = AXMLPrinter(file)
        xml = axml.get_xml_obj()

        uses_sdks = xml.find("uses-sdk")
        uses_permissions = xml.findall("uses-permission")

        keys = ["{http://schemas.android.com/apk/res/android}versionCode",
                "{http://schemas.android.com/apk/res/android}minSdkVersion",
                "{http://schemas.android.com/apk/res/android}targetSdkVersion",
                "{http://schemas.android.com/apk/res/android}maxSdkVersion",
                "{http://schemas.android.com/apk/res/android}compileSdkVersion",
                "{http://schemas.android.com/apk/res/android}compileSdkVersionCodename",
                "platformBuildVersionCode", "platformBuildVersionName"]

        for key in keys:
            item = None
            if xml is not None:
                item = xml.attrib.get(key)
            if item is None and uses_sdks is not None:
                item = uses_sdks.attrib.get(key)
            self.sdks[key.split('}')[-1]] = item

        if uses_permissions is not None:
            for permission in uses_permissions:
                self.permissions.append(permission.attrib.values()[0])

    def __str__(self):
        return ("=================================================================\n"
                + self.info[0] + "\n"
                + "=================================================================\n")

# ---------------------------------------------------------------------- #

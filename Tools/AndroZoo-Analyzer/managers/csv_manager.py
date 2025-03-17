import os
import csv

from .args_manager import ARGS


# ---------------------------------------------------------------------- #

fields = ["sha256", "apk_size", "pkg_name", "vt_detection", "dex_size", "sdk", "permissions",
          "magic_type_count", "mime_type_count", "encoding_count", "extension_count",
          "magic_type_size", "mime_type_size", "encoding_size", "extension_size", "relations"]

# ---------------------------------------------------------------------- #

# Writes csv file (write or append mode)
def write_csv(path, data, mode="w"):
    with open(path, mode) as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        if os.path.getsize(path) == 0:
            writer.writeheader()
        writer.writerow(data)


# Updates csv file with obtained information
def update_csv(apk):
    output = {"sha256": apk.info[0], "apk_size": apk.info[1], "pkg_name": apk.info[2], "vt_detection": apk.info[3],
              "dex_size": apk.info[4], "sdk": apk.info[5], "permissions": apk.info[6],
              "magic_type_count": apk.counts[0], "mime_type_count": apk.counts[1], "encoding_count": apk.counts[2],
              "extension_count": apk.counts[3], "magic_type_size": apk.sizes[0], "mime_type_size": apk.sizes[1],
              "encoding_size": apk.sizes[2], "extension_size": apk.sizes[3], "relations": apk.relations}
    write_csv(ARGS.output, output, "a")

# ---------------------------------------------------------------------- #

import os
import csv

from .args_manager import ARGS

# ---------------------------------------------------------------------- #

fields = ["sha256", "sha1", "md5", "dex_date", "apk_size", "pkg_name",
          "vercode", "vt_detection", "vt_scan_date", "dex_size", "markets",
          "sdks", "permissions"]


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
    output = {"sha256": apk.info[0], "sha1": apk.info[1], "md5": apk.info[2], "dex_date": apk.info[3],
              "apk_size": apk.info[4], "pkg_name": apk.info[5], "vercode": apk.info[6], "vt_detection": apk.info[7],
              "vt_scan_date": apk.info[8], "dex_size": apk.info[9], "markets": apk.info[10], "sdks": apk.sdks,
              "permissions": apk.permissions}
    write_csv(ARGS.output, output, "a")

# ---------------------------------------------------------------------- #

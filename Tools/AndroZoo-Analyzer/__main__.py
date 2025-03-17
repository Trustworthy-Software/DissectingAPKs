import time

from classes.apk import APK
from managers.args_manager import ARGS
from managers.api_manager import request
from managers.csv_manager import update_csv


# ---------------------------------------------------------------------- #

start = time.time()
info = ARGS.input[0].split(",")
apk = APK(info, request(ARGS.key, info[0]))
try:
    apk.analyze()  # Trigger analysis
except:
    print("------------------------ ANALYSIS FAILED ------------------------")
update_csv(apk) if ARGS.output else None
end = time.time() - start
a = "-" if end < 10 else ""
print(f"{apk}{a}------------------------ {str(round(end, 4))} seconds ------------------------\n")

# ---------------------------------------------------------------------- #

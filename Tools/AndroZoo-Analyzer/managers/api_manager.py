import requests


# ---------------------------------------------------------------------- #

# Returns an API response (APK)
def request(key, sha256):
    params = {"apikey": key, "sha256": sha256}
    try:
        r = requests.get("http://serval10.uni.lu/api/download", params=params, timeout=0.5)
    except:
        print("Serval10 - Timeout")
        r = requests.get("http://androzoo.uni.lu/api/download", params=params, timeout=1.5)
    return r

# ---------------------------------------------------------------------- #

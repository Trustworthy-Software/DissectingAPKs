import requests


# ---------------------------------------------------------------------- #

# Returns an API response (APK)
def request(key, sha256):
    params = {"apikey": key, "sha256": sha256}
    return requests.get("http://serval10.uni.lu/api/download", params=params)

# ---------------------------------------------------------------------- #

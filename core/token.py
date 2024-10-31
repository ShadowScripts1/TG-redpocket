import requests

from smart_airdrop_claimer import base
from core.headers import headers


def get_token(data, proxies=None):
    url = "https://api.redpocket.io/auth/login"
    payload = {
        "initData": data,
        "refCode": "none",
        "wallet": "",
        "chain": None,
        "appName": None,
    }

    try:
        response = requests.post(
            url=url, headers=headers(), json=payload, proxies=proxies, timeout=20
        )
        data = response.json()
        token = data["data"]["token"]["access"]
        return token
    except:
        return None

import requests

from smart_airdrop_claimer import base
from core.headers import headers


def get_info(token, proxies=None):
    url = "https://api.redpocket.io/user/me"

    try:
        response = requests.get(
            url=url, headers=headers(token=token), proxies=proxies, timeout=20
        )
        data = response.json()
        balance_sniff_point = data["data"]["balance_sniff_point"] / 10
        balance_sniff_coin = int(data["data"]["balance_sniff_coin"]) / 10
        balance_scratch_card = data["data"]["balance_scratch_card"]
        balance_usdt = data["data"]["balance_usdt"]

        base.log(
            f"{base.green}$SNIFF: {base.white}{balance_sniff_coin:,} - {base.green}SNIFF COINS: {base.white}{balance_sniff_point:,} - {base.green}USDT: {base.white}{balance_usdt} - {base.green}Scratch Card: {base.white}{balance_scratch_card}"
        )

        return balance_scratch_card
    except Exception as e:
        base.log(f"{base.red}Error: {e}")
        return None

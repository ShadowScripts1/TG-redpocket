import requests
import time

from smart_airdrop_claimer import base
from core.headers import headers
from core.info import get_info


def open_card(token, proxies=None):
    url = "https://api.redpocket.io/scratch-card/open"
    payload = {}

    try:
        response = requests.post(
            url=url,
            headers=headers(token=token),
            json=payload,
            proxies=proxies,
            timeout=20,
        )
        data = response.json()
        reward = data["data"]["his"]["reward"]
        reward_type = data["data"]["his"]["typeReward"]

        return reward, reward_type
    except Exception as e:
        base.log(f"{base.red}Error: {e}")
        return None, None


def process_open_card(token, proxies=None):
    while True:
        balance_scratch_card = get_info(token=token, proxies=proxies)
        if balance_scratch_card is not None:
            if balance_scratch_card > 0:
                reward, reward_type = open_card(token=token, proxies=proxies)

                if reward:
                    if reward_type == "SNIFF_POINT":
                        reward = int(reward) / 10
                        reward_type = "SNIFF COINS"
                    base.log(
                        f"{base.white}Auto Open Card: {base.green}Success | {reward} {reward_type}"
                    )
                    time.sleep(1)
                else:
                    base.log(f"{base.white}Auto Open Card: {base.red}Fail")
                    break
            else:
                base.log(f"{base.white}Auto Open Card: {base.red}No card to open")
                break
        else:
            base.log(f"{base.white}Auto Open Card: {base.red}Card data not found")
            break

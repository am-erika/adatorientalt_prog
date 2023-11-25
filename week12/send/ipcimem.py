#!/usr/bin/env python3
import re
from typing import Any

import requests


def get_ip_address(url: str) -> Any:
    r = requests.get(url)
    text_from_url = r.text
    ip_address_from_url = re.search(r'"ip\"\:\"[\w.]+\"', text_from_url)
    ip_address_before_list = ip_address_from_url.group()  # type: ignore
    ip_address_list = ip_address_before_list.split(":")
    ip_add_before_format = ip_address_list[1]
    ip_match = re.search(r"[\w.]+", ip_add_before_format)
    ip_address = ip_match.group()  # type: ignore
    return ip_address


def main() -> None:
    url = "https://jsonip.com/"
    print(f"Your IP address: {get_ip_address(url)}")


################################################

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
import json
from typing import Any


def load_json(file: Any) -> Any:
    with open(file, "r") as input_file:
        dict_json = json.load(input_file)
    return dict_json


def get_url(dict_json: Any) -> list[str]:
    url_list = []
    for child in dict_json["data"]["children"]:
        url_list.append(child["data"]["url"])
    return url_list


def resolution(dict_json: Any, url: str) -> tuple[int, int]:
    for child in dict_json["data"]["children"]:
        if child["data"]["url"] == url:
            width = child["data"]["preview"]["images"][0]["source"]["width"]
            height = child["data"]["preview"]["images"][0]["source"]["height"]
    return width, height


def main() -> None:
    file = "szep.json"
    dict_json = load_json(file)
    url_list = get_url(dict_json)
    print(f"URL_list: {url_list}")
    for img_url in url_list:
        print(resolution(dict_json, img_url))


################################################

if __name__ == "__main__":
    main()

#!/usr/bin/env python3


def order_last(tuple_data: tuple[int, str, str, int]) -> int:
    return tuple_data[-1]


def order_user(user_info: str) -> int:
    return int(user_info.split(":")[0])


def order_last_col(list_data: list[int]) -> int:
    return list_data[1]


def main() -> None:
    data = [
        (1, "Albany", "NY", 162692),
        (121, "Wyoming", "NY", 8722),
        (3, "Allegany", "NY", 11986),
        (123, "Yates", "NY", 5094),
    ]

    users = ["10:User1", "80:User2", "100:User3", "00:User4", "45:User5"]

    matrix = [[2, 6], [1, 3], [5, 4]]

    print("With functions:")
    print(sorted(data, key=order_last))
    print(sorted(users, key=order_user, reverse=True))
    print(sorted(matrix, key=order_last_col))

    print("With lambda function:")
    print(sorted(data, key=lambda tuple_data: tuple_data[-1]))
    print(
        sorted(users, key=lambda user_info: int(user_info.split(":")[0]), reverse=True)
    )
    print(sorted(matrix, key=lambda list_data: list_data[1]))


################################################

if __name__ == "__main__":
    main()

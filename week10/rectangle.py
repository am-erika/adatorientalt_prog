#!/usr/bin/env python3
from functools import total_ordering


@total_ordering
class Rectangle(object):
    def __init__(self, width: int, length: int) -> None:
        self.width = width
        self.length = length

    def area(self) -> float:
        return self.width * self.length

    def bool(self) -> bool:
        return self.area > 0

    def __str__(self) -> str:
        return f"Rectangle({self.width}, {self.length})"

    def __eq__(self, other) -> bool:
        if isinstance(other, Rectangle):
            return self.area() == other.area()

    def __lt__(self, other) -> bool:
        if isinstance(other, Rectangle):
            return self.area() < other.area()


def main():
    r1 = Rectangle(0, 5)
    r2 = Rectangle(10, 20)
    if r1:  # r1.__bool__() will be called
        print("r1 is considered to be true (truthy)")
    else:
        print("r1 is considered to be false (falsy)")
    print("-" * 20)
    print(r1 < r2)  # r1.__lt__(r2) will be called
    print(r2 < r1)


################################################

if __name__ == "__main__":
    main()

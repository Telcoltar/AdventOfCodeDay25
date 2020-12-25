import logging
from logging.config import fileConfig
from typing import TextIO
from math import sqrt, ceil

fileConfig("log.ini")

logger = logging.getLogger("dev")


def get_input_data(filename: str) -> tuple[int, int]:
    f: TextIO = open(filename)

    card_public_key: int = int(f.readline())
    door_public_key: int = int(f.readline())

    f.close()

    return card_public_key, door_public_key


def discrete_log(order: int, gen: int, ele: int) -> int:
    m: int = ceil(sqrt(order))
    table: dict[int, int] = {}
    for j in range(m):
        table[pow(gen, j, order)] = j
    gamma: int = ele
    for i in range(m):
        if gamma in table:
            return i * m + table[gamma]
        gamma = (gamma * pow(gen, -m, order)) % order
    return -1


def solution_part_1(filename: str) -> int:
    card_public_key, door_public_key = get_input_data(filename)
    logger.debug(f"{card_public_key}, {door_public_key}")
    card_loop_size = discrete_log(20201227, 7, card_public_key)
    door_loop_size = discrete_log(20201227, 7, door_public_key)
    logger.debug(f"{card_loop_size}, {door_loop_size}")
    return pow(door_public_key, card_loop_size, 20201227)


if __name__ == '__main__':
    logger.debug(solution_part_1("inputData.txt"))

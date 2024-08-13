"""
    NW - N - NE
    W  - M - E
    SW - S - SE
"""


def get_adyacent_boxes_in_mid_board(id: int, columns: int) -> list[int]:
    adyacent_boxes = []
    for num in [1, -1, 0]:
        for col in [columns, -columns, 0]:
            adyacent_boxes.append(id + num + col)
    adyacent_boxes.pop()
    return adyacent_boxes


def get_adyacent_boxes_in_north_side(id: int, columns: int) -> list[int]:
    adyacent_boxes = []
    for num in [1, -1, 0]:
        for col in [columns, 0]:
            adyacent_boxes.append(id + num + col)
    adyacent_boxes.pop()
    return adyacent_boxes


def get_adyacent_boxes_in_south_side(id: int, columns: int) -> list[int]:
    adyacent_boxes = []
    for num in [1, -1, 0]:
        for col in [-columns, 0]:
            adyacent_boxes.append(id + num + col)
    adyacent_boxes.pop()
    return adyacent_boxes


def get_adyacent_boxes_in_west_side(id: int, columns: int) -> list[int]:
    adyacent_boxes = []
    for num in [1, 0]:
        for col in [columns, -columns, 0]:
            adyacent_boxes.append(id + num + col)
    adyacent_boxes.pop()
    return adyacent_boxes


def get_adyacent_boxes_in_east_side(id: int, columns: int) -> list[int]:
    adyacent_boxes = []
    for num in [-1, 0]:
        for col in [columns, -columns, 0]:
            adyacent_boxes.append(id + num + col)
    adyacent_boxes.pop()
    return adyacent_boxes


def get_adyacent_boxes_in_northeast_corner(id: int, columns: int) -> list[int]:
    adyacent_boxes = []
    for num in [-1, 0]:
        for col in [columns, 0]:
            adyacent_boxes.append(id + num + col)
    adyacent_boxes.pop()
    return adyacent_boxes


def get_adyacent_boxes_in_northwest_corner(id: int, columns: int) -> list[int]:
    adyacent_boxes = []
    for num in [1, 0]:
        for col in [columns, 0]:
            adyacent_boxes.append(id + num + col)
    adyacent_boxes.pop()
    return adyacent_boxes


def get_adyacent_boxes_in_southeast_corner(id: int, columns: int) -> list[int]:
    adyacent_boxes = []
    for num in [-1, 0]:
        for col in [-columns, 0]:
            adyacent_boxes.append(id + num + col)
    adyacent_boxes.pop()
    return adyacent_boxes


def get_adyacent_boxes_in_southwest_corner(id: int, columns: int) -> list[int]:
    adyacent_boxes = []
    for num in [1, 0]:
        for col in [-columns, 0]:
            adyacent_boxes.append(id + num + col)
    adyacent_boxes.pop()
    return adyacent_boxes


get_adyacent_boxes_by_id = {
    "N": get_adyacent_boxes_in_north_side,
    "S": get_adyacent_boxes_in_south_side,
    "W": get_adyacent_boxes_in_west_side,
    "E": get_adyacent_boxes_in_east_side,
    "NW": get_adyacent_boxes_in_northwest_corner,
    "NE": get_adyacent_boxes_in_northeast_corner,
    "SW": get_adyacent_boxes_in_southwest_corner,
    "SE": get_adyacent_boxes_in_southeast_corner,
    "M": get_adyacent_boxes_in_mid_board,
}

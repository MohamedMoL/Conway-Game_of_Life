def determine_position_of_a_box_in_board(rows: int, columns: int, id: int) -> str:
    board_size = rows * columns
    # There are a total of 9 possibilities: 4 laterals, 4 corners and mid
    if id % columns == 0:  # East side
        if id == columns:  # Southwest's corner
            return "NE"
        if id == board_size:  # Southeast's corner
            return "SE"
        return "E"  # Mid east
    if (id - 1) % columns == 0:  # West side
        if id == 1:  # Northwest's corner
            return "NW"
        if id == board_size - (columns - 1):  # Southwest's corner
            return "SW"
        return "W"  # Mid west
    if id < columns:
        return "N"  # Mid north
    if board_size > id > board_size - columns:
        return "S"  # Mid south
    return "M"  # Middle of the board

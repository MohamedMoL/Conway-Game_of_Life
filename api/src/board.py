from cells import Cell


class Board:
    def __init__(self, rows: int, columns: int, alive_cells_ids: list[int]) -> None:
        self.rows: int = rows
        self.columns: int = columns
        self.cells: dict[int, Cell] = {}
        self.alive_cells_ids: list[int] = alive_cells_ids

    def insert_cell(self, cell: Cell) -> None:
        self.cells.update({cell.id: cell})

    def is_there_already_a_cell(self, id: int) -> bool:
        if self.cells.get(id):
            return False
        return True

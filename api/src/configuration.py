from cells import Cell
from board import Board
from game import Game
from helpers.determine_position_in_board import determine_position_of_a_box_in_board


class Configuration:
    def __init__(self, conf: dict) -> None:
        self.rows: int = conf["rows"]
        self.columns: int = conf["columns"]
        self.generations: int = conf["generations"]
        self.alive_cells_ids: list[int] = conf["alive_cells"]

    def initializing_board(self) -> Board:
        board = Board(self.rows, self.columns, self.alive_cells_ids)

        # This creates all cells
        for id in range(1, self.rows * self.columns + 1):
            new_cell = self.create_cell(id)
            board.insert_cell(new_cell)

        # Set alive cells
        for id in self.alive_cells_ids:
            board.cells[id].is_alive = True

        return board

    def create_cell(self, id: int) -> Cell:
        new_cell = Cell(id)
        current_position = determine_position_of_a_box_in_board(
            self.rows, self.columns, id
        )
        new_cell.set_position(current_position)
        return new_cell

    def create_game(self):
        game = Game(self.initializing_board(), self.generations)
        return game

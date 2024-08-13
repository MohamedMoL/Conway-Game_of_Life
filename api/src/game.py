from board import Board
from helpers.get_adyacent_boxes_in_board_by_id import get_adyacent_boxes_by_id


class Game:
    def __init__(self, board: Board, amount_of_generations: int) -> None:
        self.board = board
        self.amount_of_generations = amount_of_generations
        self.generations: list[list[int]] = []

    def link_cells_with_their_adyacent_ones(self):
        for id, cell in self.board.cells.items():
            adyacent_boxes = get_adyacent_boxes_by_id[cell.position](
                id, self.board.columns
            )
            for adyacent_id in adyacent_boxes:
                cell.link_cells(self.board.cells[adyacent_id])

    def start_game(self):
        alive_cells_ids = self.board.alive_cells_ids

        for _ in range(0, self.amount_of_generations):

            alive_cells = [self.board.cells[id] for id in alive_cells_ids]

            important_cells = {id: self.board.cells[id] for id in alive_cells_ids}
            for cell in alive_cells:
                for ady_cell in cell.adyacent_cells:
                    important_cells[ady_cell.id] = ady_cell

            for cell in important_cells.values():
                cell.i_will_live_or_die()

            alive_cells_ids = []

            for cell in important_cells.values():
                is_alive = cell.update_state_after_a_gen()
                if is_alive:
                    alive_cells_ids.append(cell.id)

            self.generations.append(alive_cells_ids)

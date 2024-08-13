class Cell:
    def __init__(self, id: int) -> None:
        self.is_alive: bool = False
        self.adyacent_cells: list["Cell"] = []
        self.id: int = id
        self.position: str
        self.will_live: bool = False

    def link_cells(self, ad_cell: "Cell") -> None:
        self.adyacent_cells.append(ad_cell)

    def set_position(self, position: str) -> None:
        self.position = position

    def i_will_live_or_die(self) -> None:
        adyacent_alive_cells = len(
            ["" for cell in self.adyacent_cells if cell.is_alive == True]
        )
        # The cell is alive in this generation
        if self.is_alive:
            if adyacent_alive_cells == 2 or adyacent_alive_cells == 3:
                self.will_live = True
        # The cell isn't alive in this generation
        else:
            if adyacent_alive_cells == 3:
                self.will_live = True

    def update_state_after_a_gen(self) -> bool:
        self.is_alive = self.will_live
        self.will_live = False
        return self.is_alive

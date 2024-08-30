import { create_board } from "./create_board.js";
import {
	board,
	column_cells,
	create_board_btn,
	row_cells,
} from "./document_items.js";

create_board_btn.addEventListener("click", function () {
	const rows = row_cells.value;
	const columns = column_cells.value;
	create_board(board, rows, columns);
});

board.addEventListener("click", (event) => {
	let color = event.target.style.backgroundColor;

	if (event.target.dataset.cell_id != undefined) {
		if (color == "black" || color == "") {
			event.target.style.backgroundColor = "white";
		} else {
			event.target.style.backgroundColor = "black";
		}
	}
});

import { create_board } from "./create_board.js";
import {
	create_board_btn,
	row_cells,
	column_cells,
	board,
} from "./document_items.js";

create_board_btn.addEventListener("click", function () {
	const rows = row_cells.value;
	const columns = column_cells.value;
	create_board(board, rows, columns);
});

board.addEventListener("click", (event) => {
	let color = event.target.style.backgroundColor;
	if (color == "black" || color == "") {
		event.target.style.backgroundColor = "white";
	} else {
		event.target.style.backgroundColor = "black";
	}
});

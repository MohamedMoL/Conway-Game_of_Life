import { get_all_cells } from "../controller/get_all_cells.js";

export function update_board(alive_cells_ids) {
	const array_of_cells = [...get_all_cells()];

	array_of_cells.forEach((cell) => {
		cell.style.backgroundColor = "black";
	});

	alive_cells_ids.forEach((id) => {
		array_of_cells[id - 1].style.backgroundColor = "white";
	});
}

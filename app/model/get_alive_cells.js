export function get_alive_cells(cells) {
	let alive_cells_ids = [];
	cells.forEach((cell) => {
		if (cell.style.backgroundColor == "white") {
			alive_cells_ids.push(parseInt(cell.dataset.cell_id));
		}
	});
	return alive_cells_ids;
}

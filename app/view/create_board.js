/**
 * @param {HTMLElement} board
 * @param {Number} rows
 * @param {Number} columns
 */
export function create_board(board, rows, columns) {
	board.style.gridTemplateRows = `repeat(${rows}, 1fr)`;
	board.style.gridTemplateColumns = `repeat(${columns}, 1fr)`;

	let cells_in_board = "";
	for (let i = 1; i < rows * columns + 1; i++) {
		cells_in_board += `<div class="cell-div" data-cell_id="${i}" style="background-color: black;"></div>`;
	}
	board.innerHTML = cells_in_board;
}

import { get_alive_cells } from "../model/get_alive_cells.js";

/**
 *
 * @param {HTMLInputElement} row
 * @param {HTMLInputElement} column
 * @param {HTMLInputElement} generations
 * @param {NodeListOf<HTMLDivElement>} cells
 * @returns {JSON}
 */

export function get_configuration(row, column, generations, cells) {
	let configuration = {
		rows: parseInt(row.value),
		columns: parseInt(column.value),
		generations: parseInt(generations.value),
		alive_cells: get_alive_cells(cells),
	};
	return configuration;
}

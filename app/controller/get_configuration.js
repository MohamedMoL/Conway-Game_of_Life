import { get_alive_cells } from "../model/get_alive_cells.js";
/**
 *
 * @param {Number} row
 * @param {Number} column
 * @param {Number} generations
 * @param {*} cells
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

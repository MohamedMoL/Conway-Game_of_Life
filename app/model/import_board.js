import { create_board } from "../view/create_board.js";
import { update_board } from "./update_board.js";
import {
	row_cells,
	column_cells,
	generations,
	board,
} from "../view/document_items.js";

export function import_board(json_str_configuration) {
	let parsed_configuration = JSON.parse(json_str_configuration);

	row_cells.value = parsed_configuration.rows;
	column_cells.value = parsed_configuration.columns;
	generations.value = parsed_configuration.generations;

	create_board(board, row_cells.value, column_cells.value);
	update_board(parsed_configuration.alive_cells);
}

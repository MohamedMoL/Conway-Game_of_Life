import { get_configuration } from "../controller/get_configuration.js";
import {
	column_cells,
	row_cells,
	generations,
	export_board_btn,
} from "./document_items.js";
import { get_all_cells } from "../controller/get_all_cells.js";

export_board_btn.addEventListener("click", function () {
	const conf = get_configuration(
		row_cells,
		column_cells,
		generations,
		get_all_cells()
	);
	navigator.clipboard.writeText(JSON.stringify(conf));
});

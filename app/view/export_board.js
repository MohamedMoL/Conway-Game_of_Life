import { get_all_cells } from "../controller/get_all_cells.js";
import { get_configuration } from "../controller/get_configuration.js";
import {
	column_cells,
	export_board_btn,
	generations,
	popup_message,
	row_cells,
} from "./document_items.js";

export_board_btn.addEventListener("click", function () {
	const conf = get_configuration(
		row_cells,
		column_cells,
		generations,
		get_all_cells()
	);
	navigator.clipboard.writeText(JSON.stringify(conf));

	popup_message.classList.remove("hidden");
	popup_message.classList.add("not_hidden");

	setTimeout(() => {
		popup_message.classList.remove("not_hidden");
		popup_message.classList.add("hidden");
	}, 2000);
});

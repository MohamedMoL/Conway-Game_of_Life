import { import_board } from "../model/import_board.js";
import {
	import_board_btn,
	dialog,
	json_input,
	receive_json_btn,
} from "./document_items.js";

import_board_btn.addEventListener("click", () => {
	dialog.show();
});

receive_json_btn.addEventListener("click", () => {
	const configuration = json_input.value;
	if (json_input != "") {
		import_board(configuration);
		json_input.value = "";
	}

	dialog.close();
});

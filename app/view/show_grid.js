import { board, show_grid } from "./document_items.js";

show_grid.addEventListener("change", () => {
	if (show_grid.checked == true) {
		board.classList.add("gap");
	} else {
		board.classList.remove("gap");
	}
});

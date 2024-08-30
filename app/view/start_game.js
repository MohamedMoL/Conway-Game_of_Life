import { get_all_cells } from "../controller/get_all_cells.js";
import { get_configuration } from "../controller/get_configuration.js";
import { update_board } from "../model/update_board.js";
import {
	column_cells,
	gen_velocity,
	generations,
	row_cells,
	start_game_btn,
} from "./document_items.js";

async function testFetch() {
	try {
		const response = await fetch("http://127.0.0.1:8000/game/", {
			method: "POST",
			headers: {
				"Content-Type": "application/json",
			},
			mode: "cors",
			body: JSON.stringify(
				get_configuration(row_cells, column_cells, generations, get_all_cells())
			),
		});
		const data = await response.json();
		return data;
	} catch (error) {
		console.error("Error:", error);
	}
}

start_game_btn.addEventListener("click", async () => {
	let data = await testFetch();
	let velocity = parseInt(1000 / gen_velocity.value);

	let generationIndex = 0;

	const runGeneration = () => {
		if (generationIndex < data.length) {
			update_board(data[generationIndex]);
			generationIndex++;
		} else {
			clearInterval(generationInterval);
		}
	};

	// Run the first generation immediately
	runGeneration();

	// Set interval to run subsequent generations
	const generationInterval = setInterval(runGeneration, velocity); // Adjust time as needed
});

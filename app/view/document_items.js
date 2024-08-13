// ------------------ DOCUMENT ELEMENTS ------------------
// BUTTONS
export const import_board_btn = document.getElementById("import_board-btn");
export const export_board_btn = document.getElementById("export_board-btn");
export const receive_json_btn = document.getElementById("receive_json-btn");
export const create_board_btn = document.getElementById("create_board-btn");
export const start_game_btn = document.getElementById("start_game-btn");

// INPUTS
export const row_cells = document.getElementById("amount_of_rows-inp");
export const column_cells = document.getElementById("amount_of_columns-inp");
export const json_input = document.getElementById("imported_config-inp");
export const generations = document.getElementById("amount_of_generations-inp");
export const gen_velocity = document.getElementById("gen_velocity-inp");
export const show_grid = document.getElementById("show_grid-check");

// OTHERS
export const dialog = document.querySelector("dialog");
export const board = document.getElementById("board");

// ------------------ FUNCTIONS AND VARIABLES ------------------
export let alive_cells = [];

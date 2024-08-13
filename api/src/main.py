from configuration import Configuration
from time import perf_counter
from json import loads


if __name__ == "__main__":
    config = '{"rows":100,"columns":100,"generations":300,"alive_cells":[3920,3921,4021,4022,4121]}'

    parsed_config = loads(config)

    start_time = perf_counter()

    configuration = Configuration(parsed_config)
    game = configuration.create_game()
    game.link_cells_with_their_adyacent_ones()
    game.start_game()

    end_time = perf_counter()

    with open("./example2.txt", "w") as file:
        file.write(str(game.generations))
    print(f"\nThis lasts {end_time-start_time} seconds")

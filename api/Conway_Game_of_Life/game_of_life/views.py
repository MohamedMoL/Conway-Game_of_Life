from django.http import HttpResponse
from json import loads, dumps


def index(request):
    if request.method == "POST":

        # This whole block is used to import the functions in src folder
        import sys
        import os

        # Add the parent directory to sys.path
        sys.path.append(
            os.path.abspath(os.path.join(os.path.dirname(__file__), "../../src"))
        )
        from configuration import Configuration

        configuration = request.body.decode("utf-8")
        json_conf = loads(configuration)

        configuration = Configuration(json_conf)
        game = configuration.create_game()
        game.link_cells_with_their_adyacent_ones()
        game.start_game()
        return HttpResponse(dumps(game.generations))

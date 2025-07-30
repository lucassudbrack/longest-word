from src.longest_word.game import Game
import string

class TestGame:
    def test_game_initialization(self):
        # setup
        game = Game()

        # exercise
        game_grid = game.grid

        # verify
        assert isinstance(game_grid, list)
        assert len(game_grid) == 9
        for letter in game_grid:
            assert letter in string.ascii_uppercase

    def test_empty_word_is_invalid(self):
        # setup
        game = Game()

        # verify
        assert game.is_valid("") is False

    def test_is_valid(self):
        # setup
        game = Game()
        test_word = "BRACELO"
        test_grid = "BARCELONA"

        # exercise: usando o objeto que estamos testando
        game.grid = list(test_grid)

        # verify
        assert game.is_valid(test_word) is True

        # teardown: garantindo que o objeto testado nao foi modificado no teste
        assert game.grid == list(test_grid)

    def test_is_false(self):
        # setup
        game = Game()
        test_word = "LAMPEJOUNF"
        test_grid = "BARCELONA"

        # exercise: usando o objeto que estamos testando
        game.grid = list(test_grid)

        # verify
        assert game.is_valid(test_word) is False

        # teardown: garantindo que o objeto testado nao foi modificado no teste
        assert game.grid == list(test_grid)

    def test_unknown_word_is_invalid(self):
        """A word that is not in the English dictionary should not be valid"""
        new_game = Game()
        new_game.grid = list('KWIENFUQW') # Force the grid to a test case:
        assert new_game.is_valid('FEUN') is False

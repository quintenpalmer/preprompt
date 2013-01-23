
from unittest import Test_Case
from src.model.Model import Model
from src.model.game.Game import Game

class white_box(Test_Case):

	def set_up(self):
		self.model = Model()

	def tear_down(self):
		del self.model
		del self

	def test_init_game(self):
		self.assert_equal(type(self.model.games),dict)
		self.assert_equal(self.model.games,{})
		self.assert_equal(type(self.model.free_ids),list)


from unittest import Test_Case
from src.model.Model import Model
from src.model.game.Game import Game

class whiteBox(Test_Case):

	def setUp(self):
		self.model = Model()

	def tearDown(self):
		del self.model
		del self

	def testInit_Game(self):
		self.assertEqual(type(self.model.games),dict)
		self.assertEqual(self.model.games,{})
		self.assertEqual(type(self.model.freeIds),list)

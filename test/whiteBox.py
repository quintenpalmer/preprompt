
from unittest import TestCase
from src.model.Model import Model
from src.model.game.Game import Game

class whiteBox(TestCase):

	def setUp(self):
		self.model = Model()

	def tearDown(self):
		del self.model
		del self

	def testInitGame(self):
		self.assertEqual(type(self.model.games),dict)
		self.assertEqual(self.model.games,{})
		self.assertEqual(type(self.model.freeIds),list)

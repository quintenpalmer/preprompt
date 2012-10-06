
from unittest import TestCase
from src.model.Model import Model
from src.model.game.Game import Game

class whiteBox(TestCase):

	def setUp(self):
		self.model = Model(1)

	def tearDown(self):
		del self.model
		del self

	def testInitGame(self):
		self.assertIsInstance(self.model.games,dict)
		self.assertEqual(self.model.games,{})
		self.assertIsInstance(self.model.freeIds,list)

	def testStartGame(self):
		self.model.startGame(((26,13),(1,1)))
		self.assertEqual(self.model.games.keys()[0],0)
		self.assertIsInstance(self.model.games[0].game,Game)
		self.assertEqual(len(self.model.games),1)
		self.assertEqual(self.model.games[0].game.players[0].player.uid,26)
		self.assertEqual(self.model.games[0].game.players[1].player.uid,13)

	def testStopGame(self):
		self.model.startGame(((26,13),(1,1)))
		self.model.stopGame(0)
		self.assertEqual(len(self.model.games),0)

	def testStopSecondGame(self):
		self.model.startGame(((26,13),(1,1)))
		self.model.startGame(((25,12),(1,1)))
		self.assertEqual(self.model.games.keys()[0],0)
		self.assertIsInstance(self.model.games[0].game,Game)
		self.assertIsInstance(self.model.games[1].game,Game)
		self.assertEqual(len(self.model.games),2)
		self.assertEqual(self.model.games[0].game.players[0].player.uid,26)
		self.assertEqual(self.model.games[0].game.players[1].player.uid,13)
		self.assertEqual(self.model.games[1].game.players[0].player.uid,25)
		self.assertEqual(self.model.games[1].game.players[1].player.uid,12)
		self.model.stopGame(0)
		self.assertEqual(len(self.model.games),1)
		self.assertEqual(self.model.games.keys(),[1])
		self.assertEqual(self.model.games[1].game.players[0].player.uid,25)
		self.assertEqual(self.model.games[1].game.players[1].player.uid,12)

from src.model.clist import cltypes

class Action:
	def __init__(self):
		self.subActions = []
	def addAction(self,game,uid,cardEffect):
		self.subActions.append(Sub_Action(game,uid,cardEffect))
	def act(self):
		for subAction in self.subActions:
			subAction.accountFor_Board()
		for subAction in self.subActions:
			subAction.act()

class Sub_Action:
	def __init__(self,game,uid,cardEffect):
		self.me = game.getMe_FromUid(uid)
		self.them = game.getThem_FromUid(uid)
		self.element = None
		self.game = game
		self.damage = 0
		self.heal = 0
		self.moves = False
		self.src = None
		self.dst = None
		cardEffect.applyTo(self)

	def act(self):
		self.accountFor_Board()
		self.me.player.health += self.heal
		self.them.player.health -= self.damage
		if self.moves:
			print "i would be moving you from" + str(self.src) + "," + str(self.dst)

	def accountFor_Board(self):
		for card in self.me.collection.lists[cltypes.active].cards:
			print 3
		for card in self.them.collection.lists[cltypes.active].cards:
			print 2

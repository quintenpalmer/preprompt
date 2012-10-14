
class Action:
	def __init__(self):
		self.subActions = []
	def addAction(self,game,uid,cardEffect):
		self.subActions.append(SubAction(game,uid,cardEffect))
	def act(self):
		for subAction in self.subActions:
			subAction.accountForBoard()
		for subAction in self.subActions:
			subAction.act()

class SubAction:
	def __init__(self,game,uid,cardEffect):
		self.me = game.getMeFromUid(uid)
		self.them = game.getThemFromUid(uid)
		self.element = None
		self.game = game
		self.damage = 0
		self.heal = 0
		self.moves = False
		self.src = None
		self.dst = None
		cardEffect.applyTo(self)

	def act(self):
		self.accountForBoard()
		self.me.player.health += self.heal
		self.them.player.health -= self.damage
		if self.moves:
			print "i would be moving you from" + str(self.src) + "," + str(self.dst)

	def accountForBoard(self):
		pass

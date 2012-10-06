
class Action:
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

	def go(self):
		self.me.player.health += self.heal
		self.them.player.health -= self.damage

	def accountForBoard(self):
		pass

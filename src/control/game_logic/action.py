from src.model.clist import cltypes

class Action:
	def __init__(self):
		self.sub_actions = []
	def add_action(self,game,uid,card_effect):
		self.sub_actions.append(Sub_Action(game,uid,card_effect))
	def act(self):
		for sub_action in self.sub_actions:
			sub_action.account_for_board()
		for sub_action in self.sub_actions:
			sub_action.act()

class Sub_Action:
	def __init__(self,game,uid,card_effect):
		self.me = game.get_me_from_uid(uid)
		self.them = game.get_them_from_uid(uid)
		self.element = None
		self.game = game
		self.damage = 0
		self.heal = 0
		self.moves = False
		self.src = None
		self.dst = None
		card_effect.apply_to(self)
		self.base_damage = self.damage
		self.base_heal = self.heal
		self.base_moves = self.moves
		self.base_src = self.src
		self.base_dst = self.dst
		

	def act(self):
		self.account_for_board()
		self.me.player.health += self.heal
		self.them.player.health -= self.damage
		if self.moves:
			print "i would be moving you from" + str(self.src) + "," + str(self.dst)

	def account_for_board(self):
		for card in self.me.collection.lists[cltypes.active].cards:
			print "my card"
		for card in self.them.collection.lists[cltypes.active].cards:
			print "their card"

from model import cltypes
from pyplib.errors import PP_Game_Action_Error

class Action:
	def __init__(self):
		self.sub_actions = []
	def add_action(self,game,uid,card_effect):
		self.sub_actions.append(Sub_Action(game,uid,card_effect))
	def act(self):
		for sub_action in self.sub_actions:
			sub_action.act()
		return True

class Sub_Action:
	def __init__(self,game,uid,card_effect):
		self.me = game.get_me_from_uid(uid)
		self.them = game.get_them_from_uid(uid)
		self.elemental = None
		self.game = game
		self.damage = 0
		self.heal = 0
		self.moves = False
		self.src_list = None
		self.src_card = None
		self.dst_list = None
		self.dst_card = None
		card_effect.apply_to(self)
		self.base_damage = self.damage
		self.base_heal = self.heal
		self.base_moves = self.moves
		self.src_list = self.src_list
		self.src_card = self.src_card
		self.dst_list = self.dst_list
		self.dst_card = self.dst_card

	def act(self):
		self.account_for_board()
		self.me.player.health += self.heal
		self.them.player.health -= self.damage
		if self.moves:
			try:
				self.game
			except AttributeError:
				raise PP_Game_Action_Error("Loaded Card tried to move without src and dst specified")
			print "i would be moving you from" + str(self.src) + "," + str(self.dst)

	def account_for_board(self):
		for card in self.me.collection.lists[cltypes.active].cards:
			card.effect.pactivates.on_act(self,0)
		for card in self.them.collection.lists[cltypes.active].cards:
			card.effect.pactivates.on_act(self,1)

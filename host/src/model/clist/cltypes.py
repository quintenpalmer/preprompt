
deck = 0
hand = 1
active = 2
grave = 3
special = 4
other = 5

names = {}
names[deck]='deck'
names[hand]='hand'
names[active]='active'
names[grave]='grave'
names[special]='special'
names[other]='other'

size = len(names)+1

full = range(0,size)

class Visibility:
	def __init__(self):
		self.visible = range(0,size)
		self.visible[deck] = (False,False)
		self.visible[hand] = (True,False)
		self.visible[active] = (True,True)
		self.visible[grave] = (True,True)
		self.visible[special] = (False,False)
		self.visible[other] = (True,False)

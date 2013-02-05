
class Elementals:
	Fire = 0
	Water = 1
	Nature = 2
	Death = 3

elementals = {}
elementals['f'] = Elementals.Fire
elementals['w'] = Elementals.Water
elementals['n'] = Elementals.Nature
elementals['d'] = Elementals.Death
elementals['fire'] = Elementals.Fire
elementals['water'] = Elementals.Water
elementals['nature'] = Elementals.Nature
elementals['death'] = Elementals.Death

def get_elemental_from_string(string):
	return elementals[string]

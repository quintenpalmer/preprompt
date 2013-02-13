
fire = 0
water = 1
nature = 2
death = 3

elementals = {}
elementals['f'] = fire
elementals['w'] = water
elementals['n'] = nature
elementals['d'] = death
elementals['fire'] = fire
elementals['water'] = water
elementals['nature'] = nature
elementals['death'] = death

def get_elemental_from_string(string):
	return elementals[string]

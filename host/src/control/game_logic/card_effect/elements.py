
class Elements:
	Fire = 0
	Water = 1
	Nature = 2
	Death = 3

elements = {}
elements['f'] = Elements.Fire
elements['w'] = Elements.Water
elements['n'] = Elements.Nature
elements['d'] = Elements.Death
elements['fire'] = Elements.Fire
elements['water'] = Elements.Water
elements['nature'] = Elements.Nature
elements['death'] = Elements.Death

def get_element_from_string(string):
	return elements[string]

from src.control.gameHandle.card.DirectDamage import DirectDamage

def Effect(fullToParse):
	print fullToParse
	for toParse in fullToParse:
		toParse = toParse.split(',')
		print toParse
		if len(toParse) != 4:
			return DummyEffect()
		if toParse[0] == 'o':
			if toParse[1] == 'd':
				return DirectDamage(toParse[2],toParse[3])

class DummyEffect:
	def applyTo(self,action):
		pass

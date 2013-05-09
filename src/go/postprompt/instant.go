package postprompt

type instant struct {
	ieffect instantEffect
	iconds []instantCond
}

type instantList struct {
	instants []*instant
}

func (i *instant) applyTo(sub *subAction, g *game) error {
	playable := true;
	for _,icond := range i.iconds {
		playable = playable && icond.isValid(g,sub);
	}
	if playable {
		i.ieffect.applyTo(sub);
		return nil
	}
	return Newpperror("that card is not valid to play")
}

type instantEffect interface {
	applyTo(*subAction)
}

type instantCond interface {
	isValid(*game, *subAction) bool
}

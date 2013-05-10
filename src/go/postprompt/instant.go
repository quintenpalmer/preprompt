package postprompt

type Instant struct {
	effect InstantEffect
	conds []InstantCond
}

type InstantList struct {
	instants []*Instant
}

func (instant *Instant) applyTo(action *Action, game *Game) error {
	playable := true;
	for _,icond := range instant.conds {
		playable = playable && icond.isValid(game,action);
	}
	if playable {
		instant.effect.applyTo(action);
		return nil
	}
	return Newpperror("that card is not valid to play")
}

type InstantEffect interface {
	applyTo(*Action)
}

type InstantCond interface {
	isValid(*Game, *Action) bool
}

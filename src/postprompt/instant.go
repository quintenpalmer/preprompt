package postprompt

type Instant struct {
	effect InstantEffect
	conds []InstantCond
}

type InstantList struct {
	instants []*Instant
}

func (instant *Instant) applyTo(action *Action, uid int, game *Game) string {
	playable := true;
	for _,icond := range instant.conds {
		playable = playable && icond.isValid(game,uid,action);
	}
	if playable {
		instant.effect.applyTo(action);
		return "ok"
	}
	return "that action is not valid to perform"
}

type InstantEffect interface {
	applyTo(*Action)
}

type InstantCond interface {
	isValid(*Game, int, *Action) bool
}

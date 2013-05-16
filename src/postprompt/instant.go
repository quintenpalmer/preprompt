package postprompt

type InstantList []*Instant

type Instant struct {
	effect []InstantEffect
	conds []InstantCond
}

func (instant *Instant) applyTo(action *Action, game *Game, uid int) ([]*SubAction,error) {
	playable := true;
	for _,icond := range instant.conds {
		playable = playable && icond.isValid(game,uid,action);
	}
	if playable {
		subActions := make([]*SubAction,0)
		for _,ieffect := range instant.effect {
			subAction := NewSubAction()
			ieffect.applyTo(uid,subAction);
			subActions = append(subActions,subAction)
		}
		return subActions, nil
	}
	return nil, Newpperror("that action is not valid to play")
}

type InstantEffect interface {
	applyTo(int,*SubAction)
}

type InstantCond interface {
	isValid(*Game, int, *Action) bool
}

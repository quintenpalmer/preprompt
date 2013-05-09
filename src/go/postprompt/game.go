package postprompt

type game struct {
	players [2]*player
	controlState *controlState
}

func NewGame(uid1,did1,uid2,did2 int) (*game, error) {
	g := new(game)
	player, err := NewPlayer(uid1,did1)
	if err != nil { return nil, err }
	g.players[0] = player
	player, err = NewPlayer(uid2,did2)
	if err != nil { return nil, err }
	g.players[1] = player
	g.controlState = NewControlState(uid1,uid2)
	return g, nil
}

func (g *game) GetMeFromUid(uid int) (*player, error) {
	if g.players[0].uid == uid {
		return g.players[0], nil
	} else if g.players[1].uid == uid {
		return g.players[1], nil
	}
	return nil, Newpperror("not a uid playing this game")
}

func (g *game) GetThemFromUid(uid int) (*player, error) {
	if g.players[0].uid == uid {
		return g.players[1], nil
	} else if g.players[1].uid == uid {
		return g.players[0], nil
	}
	return nil, Newpperror("not a uid playing this game")
}

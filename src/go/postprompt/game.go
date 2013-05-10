package postprompt

type Game struct {
	players [2]*Player
	controlState *ControlState
}

func NewGame(uid1,did1,uid2,did2 int) (*Game, error) {
	g := new(Game)
	player, err := NewPlayer(uid1,did1)
	if err != nil { return nil, err }
	g.players[0] = player
	player, err = NewPlayer(uid2,did2)
	if err != nil { return nil, err }
	g.players[1] = player
	g.controlState = NewControlState(uid1,uid2)
	return g, nil
}

func (game *Game) GetMeFromUid(uid int) (*Player, error) {
	if game.players[0].uid == uid {
		return game.players[0], nil
	} else if game.players[1].uid == uid {
		return game.players[1], nil
	}
	return nil, Newpperror("not a uid playing this game")
}

func (game *Game) GetThemFromUid(uid int) (*Player, error) {
	if game.players[0].uid == uid {
		return game.players[1], nil
	} else if game.players[1].uid == uid {
		return game.players[0], nil
	}
	return nil, Newpperror("not a uid playing this game")
}

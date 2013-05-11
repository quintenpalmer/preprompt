package postprompt

type Game struct {
	players map[int]*Player
	controlState *ControlState
}

func NewGame(uid1,did1,uid2,did2 int) (*Game, error) {
	if uid1 == uid2 {
		return nil, Newpperror("Cannot start a game with yourself")
	}
	g := new(Game)
	g.players = make(map[int]*Player)
	player, err := NewPlayer(uid1,did1)
	if err != nil { return nil, err }
	g.players[uid1] = player
	player, err = NewPlayer(uid2,did2)
	if err != nil { return nil, err }
	g.players[uid2] = player
	g.controlState = NewControlState(uid1,uid2)
	return g, nil
}

func (game *Game) GetMeFromUid(uid int) (*Player, error) {
	if player, ok := game.players[uid]; ok {
		return player, nil
	}
	return nil, Newpperror("not a uid playing this game")
}

func (game *Game) GetThemFromUid(uid int) (*Player, error) {
	keys := make([]int,len(game.players))
	i := 0
	for k, _ := range game.players {
		keys[i] = k
		i ++
	}
	if uid == keys[0] {
		return game.players[keys[1]], nil
	} else if uid == keys[1] {
		return game.players[keys[0]], nil
	}
	return nil, Newpperror("not a uid playing this game")
}

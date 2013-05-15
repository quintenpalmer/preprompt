package postprompt

type Model struct {
	currentIndex int
	games map[int]*Game
}

func NewModel() *Model {
	model := new(Model)
	model.games = make(map[int]*Game)
	model.currentIndex = 0
	return model
}

func (model *Model) AddGame(uid1,did1,uid2,did2 int) (*Game, int, error) {
	gameId := model.currentIndex
	model.currentIndex += 1
	game, err := NewGame(uid1,did1,uid2,did2)
	if err != nil { return nil, 0, err }
	model.games[gameId] = game
	return game, gameId, nil
}

func (model *Model) GetGameFromGameId(gameId int) (*Game, error) {
	//TODO safety check this
	if val, ok := model.games[gameId]; ok {
		return val, nil
	}
	return nil, Newpperror("game does not exist")
}

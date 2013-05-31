package postprompt

import (
	"math/rand"
	"time"
)

type gameMapping map[int]*Game

type Model struct {
	currentIndex int
	games        gameMapping
	userGames    map[int]gameMapping
}

func NewModel() *Model {
	model := new(Model)
	model.games = make(gameMapping)
	model.currentIndex = 0
	model.userGames = make(map[int]gameMapping)
	rand.Seed(time.Now().UTC().UnixNano())
	return model
}

func (model *Model) AddGame(uid1, did1, uid2, did2 int) (*Game, int, error) {
	gameId := model.currentIndex
	model.currentIndex += 1
	game, err := NewGame(uid1, did1, uid2, did2)
	if err != nil {
		return nil, 0, err
	}
	model.bookKeepGame(game, gameId, uid1, uid2)
	return game, gameId, nil
}

func (model *Model) GetGameFromGameId(gameId int) (*Game, error) {
	if val, ok := model.games[gameId]; ok {
		return val, nil
	}
	return nil, Newpperror("game does not exist")
}

func (model *Model) bookKeepGame(game *Game, gameId int, uid1 int, uid2 int) {
	if _, ok := model.userGames[uid1]; !ok {
		model.userGames[uid1] = make(gameMapping)
	}
	if _, ok := model.userGames[uid2]; !ok {
		model.userGames[uid2] = make(gameMapping)
	}
	model.userGames[uid1][gameId] = game
	model.userGames[uid2][gameId] = game
	model.games[gameId] = game
}

func (model *Model) GetGameIdsFromUid(uid int) gameMapping {
	if games, ok := model.userGames[uid]; ok {
		return games
	}
	return make(gameMapping)
}

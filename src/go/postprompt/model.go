package postprompt

type model struct {
	currentIndex int
	games map[int]*game
}

func NewModel() *model {
	m := new(model)
	m.games = make(map[int]*game)
	m.currentIndex = 0
	return m
}

func AddGame(m *model, uid1,did1,uid2,did2 int) {
	i := m.currentIndex
	m.currentIndex += 1
	m.games[i] = NewGame(uid1,did1,uid2,did2)
}

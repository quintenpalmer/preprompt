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

func (m *model) AddGame(uid1,did1,uid2,did2 int) (*game, int, error) {
	i := m.currentIndex
	m.currentIndex += 1
	g, err := NewGame(uid1,did1,uid2,did2)
	if err != nil { return nil, 0, err }
	m.games[i] = g
	return g, i, nil
}

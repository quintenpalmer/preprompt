package postprompt

type game struct {
	players [2]PlayerContainer
}

func NewGame(uid1,did1,uid2,did2 int) *game{
	g := new(game)
	db := NewDatabase("pp_shared","developer","jfjfkdkdlslskdkdjfjf")
	SelectRows(db, "select * from play_card_names")
	return g
}

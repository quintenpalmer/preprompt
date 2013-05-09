package postprompt

//TODO possibly merge PlayerTypes with cltype
type PlayerType int

var PlayerTypeMe PlayerType = 0
var PlayerTypeThem PlayerType = 1

type player struct {
	health int
	uid int
	name string
	d *deck
}

func NewPlayer(uid, did int) (*player, error) {
	pc := new(player)
	pc.health = 50
	pc.uid = uid
	name, err := GetPlayerName(uid)
	if err != nil { return nil, err }
	pc.name = name
	deck, err := NewDeck(uid,did)
	if err != nil { return nil, err }
	pc.d = deck
	return pc, nil
}

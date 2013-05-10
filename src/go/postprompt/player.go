package postprompt

//TODO possibly merge PlayerTypes with cltype
type PlayerType int

var PlayerTypeMe PlayerType = 0
var PlayerTypeThem PlayerType = 1

type Player struct {
	health int
	uid int
	name string
	d *Collection
}

func NewPlayer(uid, did int) (*Player, error) {
	pc := new(Player)
	pc.health = 50
	pc.uid = uid
	name, err := GetPlayerName(uid)
	if err != nil { return nil, err }
	pc.name = name
	collection, err := NewCollection(uid,did)
	if err != nil { return nil, err }
	pc.d = collection
	return pc, nil
}

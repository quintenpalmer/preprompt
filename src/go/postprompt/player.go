package postprompt

//TODO possibly merge PlayerTypes with cltype
type PlayerType int

var PlayerTypeMe PlayerType = 0
var PlayerTypeThem PlayerType = 1

type Player struct {
	health int
	uid int
	name string
	//collection *Collection
	cardList map[CLType]*CardList
	visibility [numcl][2]bool
}

func NewPlayer(uid, did int) (*Player, error) {
	pc := new(Player)
	pc.health = 50
	pc.uid = uid
	name, err := GetPlayerName(uid)
	if err != nil { return nil, err }
	pc.name = name
	/*
	collection, err := NewCollection(uid,did)
	if err != nil { return nil, err }

	pc.collection = collection
	*/
	pc.visibility = [numcl][2]bool{
		{false,false},
		{true,false},
		{true,true},
		{true,true},
		{false,false},
		{true,false}}
	clnums, err := GetCardIds(uid,did)
	if err != nil { return nil, err }
	deck, err := NewCardList(clnums)
	if err != nil { return nil, err }
	pc.cardList = make(map[CLType]*CardList)
	pc.cardList[Deck] = deck
	pc.cardList[Hand] = EmptyCardList()
	pc.cardList[Active] = EmptyCardList()
	pc.cardList[Grave] = EmptyCardList()
	pc.cardList[Special] = EmptyCardList()
	pc.cardList[Other] = EmptyCardList()

	return pc, nil
}

package postprompt

//TODO possibly merge PlayerTypes with cltype
type PlayerType int

const (
	PlayerTypeMe PlayerType = iota
	PlayerTypeThem
	PlayerTypeBoth
)

type Player struct {
	health     int
	uid        int
	name       string
	cardList   map[CLType]CardList
	visibility [numcl][2]bool
}

func NewPlayer(uid, did int) (*Player, error) {
	pc := new(Player)
	pc.health = 50
	pc.uid = uid
	name, err := GetPlayerName(uid)
	if err != nil {
		return nil, err
	}
	pc.name = name
	pc.visibility = [numcl][2]bool{
		{false, false},
		{true, false},
		{true, true},
		{true, true},
		{false, false},
		{true, false}}
	clnums, err := GetCardIds(uid, did)
	if err != nil {
		return nil, err
	}
	deck, err := NewCardList(clnums)
	if err != nil {
		return nil, err
	}
	pc.cardList = make(map[CLType]CardList)
	pc.cardList[Deck] = deck
	pc.cardList[Hand] = EmptyCardList()
	pc.cardList[Active] = EmptyCardList()
	pc.cardList[Grave] = EmptyCardList()
	pc.cardList[Special] = EmptyCardList()
	pc.cardList[Other] = EmptyCardList()

	return pc, nil
}

func (player *Player) push(cltype CLType, card *Card, index int) error {
	player.cardList[cltype] = append(player.cardList[cltype], card)
	return nil
}

func (player *Player) pop(cltype CLType, index int) (*Card, error) {
	if index == -1 {
		index = len(player.cardList[cltype]) - 1
	}
	if index >= len(player.cardList[cltype]) {
		return nil, Newpperror("index out of range")
	}
	card := player.cardList[cltype][index]
	player.cardList[cltype] = append(player.cardList[cltype][:index], player.cardList[cltype][index+1:]...)
	return card, nil
}

func (player *Player) GetInstantList(index int) (InstantList, error) {
	if index >= len(player.cardList[Hand]) {
		return nil, Newpperror("index out of range")
	}
	return player.cardList[Hand][index].instants, nil
}

package postprompt

type Collection struct {
	cardList map[CLType]*CardList
	visibility [numcl][2]bool
}

func NewCollection(uid,did int) (*Collection, error) {
	coll := new(Collection)
	coll.visibility = [numcl][2]bool{
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
	coll.cardList = make(map[CLType]*CardList)
	coll.cardList[Deck] = deck
	coll.cardList[Hand] = EmptyCardList()
	coll.cardList[Active] = EmptyCardList()
	coll.cardList[Grave] = EmptyCardList()
	coll.cardList[Special] = EmptyCardList()
	coll.cardList[Other] = EmptyCardList()
	return coll, nil
}

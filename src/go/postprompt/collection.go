package postprompt

type Collection struct {
	cardList [numcl]*CardList
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
	coll.cardList = [numcl]*CardList{
		deck,
		EmptyCardList(),
		EmptyCardList(),
		EmptyCardList(),
		EmptyCardList(),
		EmptyCardList()}
	return coll, nil
}

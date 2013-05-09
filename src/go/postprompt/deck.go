package postprompt

const numcl = 6

type deck struct {
	cl [numcl]*cardList
	visibility [numcl][2]bool
}

func NewDeck(uid,did int) (*deck, error) {
	d := new(deck)
	d.visibility = [numcl][2]bool{
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
	d.cl = [numcl]*cardList{
		deck,
		EmptyCardList(),
		EmptyCardList(),
		EmptyCardList(),
		EmptyCardList(),
		EmptyCardList()}
	return d, nil
}

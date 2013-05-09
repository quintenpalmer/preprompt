package postprompt

type cardList struct {
	cards []*card
}

func EmptyCardList() *cardList {
	cl := new(cardList)
	cl.cards = []*card{}
	return cl
}

func NewCardList(cardIds []int) (*cardList, error) {
	cl := new(cardList)
	cl.cards = make([]*card,len(cardIds))
	for i,cardId := range cardIds {
		c, err := NewCard(cardId)
		if err != nil { return nil, err }
		cl.cards[i] = c
	}
	return cl, nil
}

package postprompt

type CardList []*Card

func EmptyCardList() CardList {
	return make([]*Card, 0)
}

func NewCardList(cardIds []int) (CardList, error) {
	cardList := make([]*Card, len(cardIds))
	for i, cardId := range cardIds {
		card, err := NewCard(cardId)
		if err != nil {
			return nil, err
		}
		cardList[i] = card
	}
	return cardList, nil
}

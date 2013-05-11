package postprompt

import "container/list"

type CardList struct {
	cards []*Card
	lcards list.List
}

func EmptyCardList() *CardList {
	cardList := new(CardList)
	cardList.cards = []*Card{}
	return cardList
}

func NewCardList(cardIds []int) (*CardList, error) {
	cardList := new(CardList)
	cardList.cards = make([]*Card,len(cardIds))
	for i,cardId := range cardIds {
		card, err := NewCard(cardId)
		if err != nil { return nil, err }
		cardList.cards[i] = card
	}
	return cardList, nil
}

func (cardList *CardList) push(card *Card, index int) error {
	return Newpperror("cannot push yet")
}

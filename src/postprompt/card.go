package postprompt

type Card struct {
	name string
	effect *Effect
}

func NewCard(id int) (*Card, error) {
	card := new(Card)
	cardInfo, err := GetCardInfo(id)
	if err != nil {
		return nil, err
	}
	card.name = cardInfo[0]
	card.effect = NewEffect(cardInfo[1])
	return card, nil
}

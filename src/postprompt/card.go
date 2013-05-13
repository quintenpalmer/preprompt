package postprompt

type Card struct {
	name string
	effect string
}

func NewCard(id int) (*Card, error) {
	card := new(Card)
	cardInfo, err := GetCardInfo(id)
	if err != nil {
		return nil, err }
	card.name = cardInfo[0]
	card.effect = cardInfo[1]
	return card, nil
}

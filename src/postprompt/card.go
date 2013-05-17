package postprompt

type Card struct {
	name string
	effect *Effect
}

func NewCard(id int) (*Card, error) {
	card := new(Card)
	cardInfo, err := GetCardInfo(id)
	if err != nil { return nil, err }
	card.name = cardInfo[0]
	card.effect, err = GetEffectFromString(cardInfo[1])
	if err != nil { return nil, err }
	return card, nil
}

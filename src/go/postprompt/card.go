package postprompt

type card struct {
	name string
	effect string
}

func NewCard(id int) (*card, error) {
	c := new(card)
	cardInfo, err := GetCardInfo(id)
	if err != nil { return nil, err }
	c.name = cardInfo[0]
	c.effect = cardInfo[1]
	return c, nil
}

package postprompt

type Card struct {
	name string
	instants InstantList
	persists PersistList
	triggers TriggerList
}

func NewCard(id int) (*Card, error) {
	cardName, cardEffectString, err := GetCardInfo(id)
	cardEffectRepr, err := loadJson([]byte(cardEffectString))
	if err != nil { return nil, err }
	card := new(Card)
	card.name = cardName
	card.instants, err = getInstants(cardEffectRepr["instants"])
	if err != nil { return nil, err }
	card.persists, err = getPersists(cardEffectRepr["persists"])
	if err != nil { return nil, err }
	card.triggers, err = getTriggers(cardEffectRepr["triggers"])
	if err != nil { return nil, err }
	return card, nil
}

func getTriggers(triggerRepr interface{}) (TriggerList, error) {
	triggerList := make(TriggerList,0)
	//fmt.Println(triggerRepr)
	return triggerList, nil
}

package postprompt

type InstantList []*Instant

type Instant struct {
	effect []InstantEffect
	conds  []InstantCond
}

type InstantEffect interface {
	applyTo(int, *SubAction)
}

type InstantCond interface {
	isValid(*Game, int, *Action) bool
}

func (instant *Instant) applyTo(action *Action, game *Game, uid int) ([]*SubAction, error) {
	playable := true
	for _, icond := range instant.conds {
		playable = playable && icond.isValid(game, uid, action)
	}
	if playable {
		subActions := make([]*SubAction, 0)
		for _, ieffect := range instant.effect {
			subAction := NewSubAction()
			ieffect.applyTo(uid, subAction)
			subActions = append(subActions, subAction)
		}
		return subActions, nil
	}
	return nil, Newpperror("that action is not valid to play")
}

func getInstants(instantRepr interface{}) (InstantList, error) {
	instantList := make(InstantList, 0)
	instantArray, ok := instantRepr.([]interface{})
	if !ok {
		return nil, Newpperror("Could not load instant array from json")
	}
	for _, instanti := range instantArray {
		instantRepr, ok := instanti.(map[string]interface{})
		if !ok {
			return nil, Newpperror("Could not load instant from json")
		}
		instantEffectRepr, ok := instantRepr["ieffect"].(map[string]interface{})
		if !ok {
			return nil, Newpperror("Could not load instant effect from json")
		}
		instantCondRepr, ok := instantRepr["icond"].(map[string]interface{})
		if !ok {
			return nil, Newpperror("Could not load instant cond from json")
		}
		instant := new(Instant)
		var err error
		instant.effect, err = getInstantEffectFromType(instantEffectRepr)
		if err != nil {
			return nil, err
		}
		instant.conds, err = getInstantCondFromType(instantCondRepr)
		if err != nil {
			return nil, err
		}
		instantList = append(instantList, instant)
	}
	return instantList, nil
}

func getInstantEffectFromType(instantEffectRepr map[string]interface{}) ([]InstantEffect, error) {
	effectType, ok := instantEffectRepr["type"].(string)
	if !ok {
		return nil, Newpperror("Could not load instant effect type from json")
	}
	switch effectType {
	case "DirectDamage":
		return getDirectDamageHelper(instantEffectRepr)
	case "NoInstant":
		return getDoNothing()
	default:
		return nil, Newpperror("Invalid Instant Effect Type found : " + effectType)
	}
	return nil, Newpperror("Invalid Instant Effect Type found : " + effectType)
}

func getInstantCondFromType(instantCondRepr map[string]interface{}) ([]InstantCond, error) {
	effectType, ok := instantCondRepr["type"].(string)
	if !ok {
		return nil, Newpperror("Could not load instant effect type from json")
	}
	switch effectType {
	case "AlwaysValid":
		return getAlwaysValid()
	default:
		return nil, Newpperror("Invalid Instant Effect Type found : " + effectType)
	}
	return nil, Newpperror("Invalid Instant Effect Type found : " + effectType)
}

func getDirectDamageHelper(instantEffectRepr map[string]interface{}) ([]InstantEffect, error) {
	elementString, ok := instantEffectRepr["element"].(string)
	if !ok {
		return nil, Newpperror("element in instant effect was not a string")
	}
	elementType, err := getElementTypeFromString(elementString)
	if err != nil {
		return nil, err
	}
	params, ok := instantEffectRepr["params"].(map[string]interface{})
	if !ok {
		return nil, Newpperror("Could not load instant effect params from json")
	}
	amountFloat, ok := params["amount"].(float64)
	if !ok {
		return nil, Newpperror("Could not load instant effect amount from json")
	}
	amount := int(amountFloat)
	if !ok {
		return nil, Newpperror("Could not load instant effect param amount from json")
	}
	return []InstantEffect{&directDamageInstantEffect{amount, elementType}}, nil
}

func getDoNothing() ([]InstantEffect, error) {
	return []InstantEffect{new(doNothing)}, nil
}

func getAlwaysValid() ([]InstantCond, error) {
	return []InstantCond{new(validInstant)}, nil
}

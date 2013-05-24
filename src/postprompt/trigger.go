package postprompt


type TriggerList []*Trigger

type Trigger struct {
	effect []TriggerEffect
	conds []TriggerCond
}

type TriggerEffect interface {
	applyTo(*SubAction, int)
}

type TriggerCond interface {
	isValid(*SubAction, *Action, *Game, int) bool
}

func (trigger *Trigger) applyTo(subAction *SubAction, action *Action, game *Game, uid int) error {
	playable := true;
	for _,icond := range trigger.conds {
		playable = playable && icond.isValid(subAction,action,game,uid);
	}
	if playable {
		for _,ieffect := range trigger.effect {
			ieffect.applyTo(subAction,uid);
		}
		return nil
	}
	return Newpperror("that action is not valid to play")
}

func getTriggers(triggerRepr interface{}) (TriggerList, error) {
	triggerList := make(TriggerList,0)
	triggerArray, ok := triggerRepr.([]interface{})
	if ! ok { return nil, Newpperror("Could not load trigger array from json") }
	for _, triggeri := range triggerArray {
		triggerRepr, ok := triggeri.(map[string]interface{})
		if ! ok { return nil, Newpperror("Could not load trigger from json") }
		triggerEffectRepr , ok := triggerRepr["teffect"].(map[string]interface{})
		if ! ok { return nil, Newpperror("Could not load trigger effect from json") }
		triggerCondRepr , ok := triggerRepr["tcond"].(map[string]interface{})
		if ! ok { return nil, Newpperror("Could not load trigger cond from json") }
		trigger := new(Trigger)
		var err error
		trigger.effect, err = getTriggerEffectFromType(triggerEffectRepr)
		if err != nil { return nil, err }
		trigger.conds, err = getTriggerCondFromType(triggerCondRepr)
		if err != nil { return nil, err }
		triggerList = append(triggerList,trigger)
	}
	return triggerList, nil
}

func getTriggerEffectFromType(triggerEffectRepr map[string]interface{}) ([]TriggerEffect, error) {
	effectType, ok := triggerEffectRepr["type"].(string)
	if ! ok { return nil, Newpperror("Could not load trigger effect type from json") }
	switch effectType {
		case "DamageEnhance" : return getDamageEnhancerHelper(triggerEffectRepr)
		case "NoTrigger" : return getDoNothingTrigger()
		default : return nil, Newpperror("Invalid trigger Effect Type found : " + effectType)
	}
	return nil, Newpperror("Invalid trigger Effect Type found : " + effectType)
}

func getTriggerCondFromType(triggerCondRepr map[string]interface{}) ([]TriggerCond, error) {
	effectType, ok := triggerCondRepr["type"].(string)
	if ! ok { return nil, Newpperror("Could not load trigger effect type from json") }
	switch effectType {
		case "AlwaysValid" : return getAlwaysValidTrigger()
		default : return nil, Newpperror("Invalid trigger Effect Type found : " + effectType)
	}
	return nil, Newpperror("Invalid trigger Effect Type found : " + effectType)
}

func getDamageEnhancerHelper(triggerEffectRepr map[string]interface{}) ([]TriggerEffect, error) {
	/*
	elementString, ok := triggerEffectRepr["element"].(string)
	if ! ok { return nil, Newpperror("element in trigger effect was not a string") }
	elementType, err := getElementTypeFromString(elementString)
	if err != nil { return nil, err }
	*/
	params, ok := triggerEffectRepr["params"].(map[string]interface{})
	if ! ok { return nil, Newpperror("Could not load trigger effect params from json") }
	amountFloat, ok := params["amount"].(float64)
	if ! ok { return nil, Newpperror("Could not load trigger effect amount from json") }
	amount := int(amountFloat)
	if ! ok { return nil, Newpperror("Could not load trigger effect param amount from json") }
	return []TriggerEffect{&directDamageTriggerEffect{amount}}, nil
}

func getDoNothingTrigger() ([]TriggerEffect, error) {
	return []TriggerEffect{new(doNothingTrigger)}, nil
}

func getAlwaysValidTrigger() ([]TriggerCond, error) {
	return []TriggerCond{new(validTrigger)}, nil
}

/* Direct Damage Instant Effect */

type directDamageTriggerEffect struct {
	amount int
}
func (dd *directDamageTriggerEffect) applyTo(subAction *SubAction, uid int) {
	subAction.IncreaseDamage(dd.amount)
}

/* Do Nothing Instant Effect */

type doNothingTrigger struct { }
func (dnt *doNothingTrigger) applyTo(subAction *SubAction, uid int) { }


/* Always valid Trigger */

type validTrigger struct { }
func (vi *validTrigger) isValid(subAction *SubAction, action *Action, game *Game, uid int) bool {
	return true;
}

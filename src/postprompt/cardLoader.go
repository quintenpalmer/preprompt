package postprompt

import "fmt"

func GetEffectFromString(effectString string) (*Effect, error) {
	effectRepr, err := loadJson([]byte(effectString))
	if err != nil { return nil, err }
	effect := new(Effect)
	effect.instants, err = getInstants(effectRepr["instants"])
	if err != nil { return nil, err }
	effect.persists, err = getPersists(effectRepr["persists"])
	if err != nil { return nil, err }
	effect.triggers, err = getTriggers(effectRepr["triggers"])
	if err != nil { return nil, err }
	return effect, nil
}

func getInstants(instantRepr interface{}) (InstantList, error) {
	//instantList := make(InstantList,0)
	instant := new(Instant)
	instant.effect = []InstantEffect{
		&directDamageInstantEffect{4,Fire}}
	instant.conds = []InstantCond{
		new(validInstant)}
	return []*Instant{instant}, nil
}

func getPersists(persistRepr interface{}) (PersistList, error) {
	persistList := make(PersistList,0)
	fmt.Println(persistRepr)
	return persistList, nil
}

func getTriggers(triggerRepr interface{}) (TriggerList, error) {
	triggerList := make(TriggerList,0)
	fmt.Println(triggerRepr)
	return triggerList, nil
}

package postprompt

type Effect struct {
	instants InstantList
	persists PersistList
	triggers TriggerList
}

func NewEffect(effectString string) *Effect {
	effect := new(Effect)
	return effect
}

package postprompt

type Effect struct {
	instants InstantList
	persists []*Persist
	triggers []*Trigger
}

func NewEffect(effectString string) *Effect {
	effect := new(Effect)
	return effect
}

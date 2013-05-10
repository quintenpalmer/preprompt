package postprompt

func GetDirectDamage(amount int, elementType ElementType) *InstantList {
	instantList := new(InstantList)
	instantList.instants = []*Instant{NewDirectDamageInstant(amount,elementType)}
	return instantList
}

func NewDirectDamageInstant(amount int, elementType ElementType) *Instant {
	instant := new(Instant)
	dd := new(directDamageInstantEffect)
	dd.amount = amount
	dd.elementType = elementType
	instant.effect = dd
	instant.conds = []InstantCond{new(validInstant)}
	return instant
}

type directDamageInstantEffect struct {
	amount int
	elementType ElementType
}

func (dd *directDamageInstantEffect) applyTo(action *Action) {
	action.SetDamage(dd.amount)
}

type validInstant struct { }

func (vi *validInstant) isValid(game *Game, action *Action) bool {
		return true;
}

/*
func GetDestroyInstant(srcCard playerNum, int) *instant {
	i := new(instant)
	i.ieffect = NewDestroyInstantEffect(srcCard,playerNum)
	i.iconds = []instantCond{NewValidInstant()}
		NewDestroyEffect(srcCard,playerNum),
		NewInstantCond[]{
			NewValidInstant()})
}

type NewDestroyInstantEffect struct {
	srcCard, playerNum int
}

func (destroy *NewDestroyInstantEffect) applyTo(sub *subAction) {
	sub.setMovement(destroy.playerNum,Active,destroy.srcCard,destroy.playerNum,Grave,-1)
}

func GetPhaseInstantList() *instantList {
	i := new(instantList)
	i.instants = []*instant{NewInstant()}
	return i
}
*/

package postprompt

func GetDirectDamage(amount int, elementType ElementType) *InstantList {
	instantList := new(InstantList)
	instantList.instants = []*Instant{NewDirectDamageInstant(amount,elementType)}
	return instantList
}

func GetDrawEffect() *InstantList {
	instantList := new(InstantList)
	instantList.instants = []*Instant{NewCardMoveInstant(PlayerTypeMe,Deck,-1,PlayerTypeMe,Hand,-1)}
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

func NewCardMoveInstant(
		srcPlayerType PlayerType,
		srcList CLType,
		srcIndex int,
		dstPlayerType PlayerType,
		dstList CLType,
		dstIndex int,) *Instant {
	instant := new(Instant)
	cm := new(cardMoveInstantEffect)
	cm.srcPlayerType = srcPlayerType
	cm.srcList = srcList
	cm.srcIndex = srcIndex
	cm.dstPlayerType = dstPlayerType
	cm.dstList = dstList
	cm.dstIndex = dstIndex
	instant.effect = cm
	instant.conds = []InstantCond{new(validInstant)}
	return instant
}

type cardMoveInstantEffect struct {
		srcPlayerType PlayerType
		srcList CLType
		srcIndex int
		dstPlayerType PlayerType
		dstList CLType
		dstIndex int
}

func (cm *cardMoveInstantEffect) applyTo(action *Action) {
	movement := new(Movement)
	movement.srcPlayerType = cm.srcPlayerType
	movement.srcList = cm.srcList
	movement.srcIndex = cm.srcIndex
	movement.dstPlayerType = cm.dstPlayerType
	movement.dstList = cm.dstList
	movement.dstIndex = cm.dstIndex
	action.movement = movement
}

type directDamageInstantEffect struct {
	amount int
	elementType ElementType
}

func (dd *directDamageInstantEffect) applyTo(action *Action) {
	action.SetDamage(dd.amount)
	action.SetElementType(dd.elementType)
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

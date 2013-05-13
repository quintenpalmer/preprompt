package postprompt

func GetDirectDamageIL(amount int, elementType ElementType) *InstantList {
	instantList := new(InstantList)
	instantList.instants = []*Instant{newDirectDamageInstant(amount,elementType)}
	return instantList
}

func GetPhaseStepIL() *InstantList {
	instantList := new(InstantList)
	instant := new(Instant)
	instant.effect = new(stepPhase)
	instant.conds = []InstantCond{&validSuperPhase{MainSuperPhase}}
	instantList.instants = []*Instant{instant}
	return instantList
}
func GetDrawIL() *InstantList {
	instantList := new(InstantList)
	instant := new(Instant)
	instant.effect = newCardMoveInstantEffect(PlayerTypeMe,Deck,-1,PlayerTypeMe,Hand,-1)
	instant.conds = []InstantCond{&validPhase{DrawPhase},&validSuperPhase{MainSuperPhase}}
	instantList.instants = []*Instant{instant}
	return instantList
}

func GetTurnStepIL() *InstantList {
	instantList := new(InstantList)
	instant := new(Instant)
	instant.effect = new(stepTurn)
	instant.conds = []InstantCond{&validSuperPhase{MainSuperPhase},&validPhase{EndPhase}}
	instantList.instants = []*Instant{instant}
	return instantList
}

func GetSetupIL() *InstantList {
	instantList := new(InstantList)
	instant := new(Instant)
	instant.effect = new(stepSuperPhase)
	instant.conds = []InstantCond{&validSuperPhase{PreSuperPhase}}
	instantList.instants = []*Instant{instant}
	return instantList
}

func newDirectDamageInstant(amount int, elementType ElementType) *Instant {
	instant := new(Instant)
	dd := new(directDamageInstantEffect)
	dd.amount = amount
	dd.elementType = elementType
	instant.effect = dd
	instant.conds = []InstantCond{new(validInstant)}
	return instant
}

func newCardMoveInstantEffect(
		srcPlayerType PlayerType,
		srcList CLType,
		srcIndex int,
		dstPlayerType PlayerType,
		dstList CLType,
		dstIndex int,) InstantEffect {
	cm := new(cardMoveInstantEffect)
	cm.srcPlayerType = srcPlayerType
	cm.srcList = srcList
	cm.srcIndex = srcIndex
	cm.dstPlayerType = dstPlayerType
	cm.dstList = dstList
	cm.dstIndex = dstIndex
	return cm
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

type stepTurn struct { }

func (st *stepTurn) applyTo(action *Action) {
	action.SetTurnStep(true)
}

type stepPhase struct { }

func (sp *stepPhase) applyTo(action *Action) {
	action.SetPhaseStep(StepOnePhase)
}

type stepSuperPhase struct { }

func (ssp *stepSuperPhase) applyTo(action *Action) {
	action.SetSuperPhaseStep(StepOneSuperPhase)
}

type directDamageInstantEffect struct {
	amount int
	elementType ElementType
}

func (dd *directDamageInstantEffect) applyTo(action *Action) {
	action.SetDamage(dd.amount)
	action.SetElementType(dd.elementType)
}

type validPhase struct {
	phase Phase
}

func (vp *validPhase) isValid(game *Game, action *Action) bool {
	if game.phase == vp.phase {
		return true
	}
	return false
}

type validSuperPhase struct {
	superPhase SuperPhase
}

func (vp *validSuperPhase) isValid(game *Game, action *Action) bool {
	if game.superPhase == vp.superPhase {
		return true
	}
	return false
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

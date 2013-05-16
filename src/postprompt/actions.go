package postprompt

/* Public InstantList constructors */

func GetDirectDamageIL(amount int, elementType ElementType) *InstantList {
	instantList := new(InstantList)
	instant := new(Instant)
	instant.effect = &directDamageInstantEffect{amount,elementType}
	instant.conds = []InstantCond{new(validInstant)}
	instantList.instants = []*Instant{instant}
	return instantList
}

func GetPhaseStepIL() *InstantList {
	instantList := new(InstantList)
	instant := new(Instant)
	instant.effect = new(stepPhase)
	instant.conds = []InstantCond{&validSuperPhase{MainSuperPhase},new(validTurnOwner)}
	instantList.instants = []*Instant{instant}
	return instantList
}
func GetDrawIL() *InstantList {
	instantList := new(InstantList)
	instant := new(Instant)
	instant.effect = newCardMoveInstantEffect(PlayerTypeMe,Deck,-1,PlayerTypeMe,Hand,-1)
	instant.conds = []InstantCond{&validPhase{DrawPhase},&validSuperPhase{MainSuperPhase},new(validTurnOwner)}
	instantList.instants = []*Instant{instant}
	return instantList
}

func GetTurnStepIL() *InstantList {
	instantList := new(InstantList)
	instant := new(Instant)
	instant.effect = new(stepTurn)
	instant.conds = []InstantCond{&validSuperPhase{MainSuperPhase},&validPhase{EndPhase},new(validTurnOwner)}
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

func GetEmptyIL() *InstantList {
	instantList := new(InstantList)
	instant := new(Instant)
	instant.effect = new(doNothing)
	instant.conds = []InstantCond{new(validInstant)}
	instantList.instants = []*Instant{instant}
	return instantList
}

func GetDestroyIL(srcIndex int) *InstantList {
	instantList := new(InstantList)
	instant := new(Instant)
	instant.effect = newCardMoveInstantEffect(PlayerTypeMe,Hand,srcIndex,PlayerTypeMe,Grave,-1)
	instant.conds = []InstantCond{&validPhase{MainPhase},&validSuperPhase{MainSuperPhase}}
	instantList.instants = []*Instant{instant}
	return instantList
}

/* Instant Effects */

/* Card Move Instant Effect */

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

/* Turn Swap Instant Effect */

type stepTurn struct { }

func (st *stepTurn) applyTo(action *Action) {
	action.SetTurnStep(true)
}

/* Phase Step Instant Effect */

type stepPhase struct { }

func (sp *stepPhase) applyTo(action *Action) {
	action.SetPhaseStep(StepOnePhase)
}

/* Super Phase Step Instant Effect */

type stepSuperPhase struct { }

func (ssp *stepSuperPhase) applyTo(action *Action) {
	action.SetSuperPhaseStep(StepOneSuperPhase)
}

/* Do Nothing Instant Effect */

type doNothing struct { }

func (dn *doNothing) applyTo(action *Action) { }

/* Direct Damage Instant Effect */

type directDamageInstantEffect struct {
	amount int
	elementType ElementType
}

func (dd *directDamageInstantEffect) applyTo(action *Action) {
	action.SetDamage(dd.amount)
	action.SetElementType(dd.elementType)
}

/* Instant Conds */

/* Valid only on given phase */

type validPhase struct {
	phase Phase
}

func (vp *validPhase) isValid(game *Game, uid int, action *Action) bool {
	return game.phase == vp.phase
}

/* Valid only on given super phase */

type validSuperPhase struct {
	superPhase SuperPhase
}

func (vp *validSuperPhase) isValid(game *Game, uid int, action *Action) bool {
	return game.superPhase == vp.superPhase
}

/* Always valid */

type validInstant struct { }

func (vi *validInstant) isValid(game *Game, uid int, action *Action) bool {
	return true;
}

/* Only valid on your turn */

type validTurnOwner struct { }

func (vto *validTurnOwner) isValid(game *Game, uid int, action *Action) bool {
	return uid == game.turnOwner
}

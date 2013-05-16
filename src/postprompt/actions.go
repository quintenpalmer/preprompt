package postprompt

/* Public InstantList constructors */

func GetDirectDamageIL(amount int, elementType ElementType) *InstantList {
	instantList := new(InstantList)
	instant := new(Instant)
	instant.effect = []InstantEffect{&directDamageInstantEffect{amount,elementType}}
	instant.conds = []InstantCond{new(validInstant)}
	instantList.instants = []*Instant{instant}
	return instantList
}

func GetPhaseStepIL() *InstantList {
	instantList := new(InstantList)
	instant := new(Instant)
	instant.effect = []InstantEffect{new(stepPhase)}
	instant.conds = []InstantCond{&validSuperPhase{MainSuperPhase},new(validTurnOwner)}
	instantList.instants = []*Instant{instant}
	return instantList
}
func GetDrawIL() *InstantList {
	instantList := new(InstantList)
	instant := new(Instant)
	instant.effect = []InstantEffect{newCardMoveInstantEffect(PlayerTypeMe,Deck,-1,PlayerTypeMe,Hand,-1),new(setDidDraw)}
	instant.conds = []InstantCond{&validPhase{DrawPhase},&validSuperPhase{MainSuperPhase},new(validTurnOwner),new(validHaveNotDrawn)}
	instantList.instants = []*Instant{instant}
	return instantList
}

func GetTurnStepIL() *InstantList {
	instantList := new(InstantList)
	instant := new(Instant)
	instant.effect = []InstantEffect{new(stepTurn)}
	instant.conds = []InstantCond{&validSuperPhase{MainSuperPhase},&validPhase{EndPhase},new(validTurnOwner)}
	instantList.instants = []*Instant{instant}
	return instantList
}

func GetSetupIL() *InstantList {
	instantList := new(InstantList)
	instant := new(Instant)
	instant.effect = []InstantEffect{
		new(stepSuperPhase),
		newCardMoveInstantEffect(PlayerTypeMe,Deck,-1,PlayerTypeMe,Hand,-1),
		newCardMoveInstantEffect(PlayerTypeMe,Deck,-1,PlayerTypeMe,Hand,-1),
		newCardMoveInstantEffect(PlayerTypeMe,Deck,-1,PlayerTypeMe,Hand,-1),
		newCardMoveInstantEffect(PlayerTypeMe,Deck,-1,PlayerTypeMe,Hand,-1),
		newCardMoveInstantEffect(PlayerTypeMe,Deck,-1,PlayerTypeMe,Hand,-1)}
	instant.conds = []InstantCond{&validSuperPhase{PreSuperPhase}}
	instantList.instants = []*Instant{instant}
	return instantList
}

func GetEmptyIL() *InstantList {
	instantList := new(InstantList)
	instant := new(Instant)
	instant.effect = []InstantEffect{new(doNothing)}
	instant.conds = []InstantCond{new(validInstant)}
	instantList.instants = []*Instant{instant}
	return instantList
}

func GetDestroyIL(srcIndex int) *InstantList {
	instantList := new(InstantList)
	instant := new(Instant)
	instant.effect = []InstantEffect{newCardMoveInstantEffect(PlayerTypeMe,Hand,srcIndex,PlayerTypeMe,Grave,-1)}
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
func (cm *cardMoveInstantEffect) applyTo(uid int, subAction *SubAction) {
	movement := new(Movement)
	movement.srcPlayerType = cm.srcPlayerType
	movement.srcList = cm.srcList
	movement.srcIndex = cm.srcIndex
	movement.dstPlayerType = cm.dstPlayerType
	movement.dstList = cm.dstList
	movement.dstIndex = cm.dstIndex
	subAction.movement = movement
}

/* Turn Swap Instant Effect */

type stepTurn struct { }
func (st *stepTurn) applyTo(uid int, subAction *SubAction) {
	subAction.SetTurnStep(true)
}

/* Phase Step Instant Effect */

type stepPhase struct { }
func (sp *stepPhase) applyTo(uid int, subAction *SubAction) {
	subAction.SetPhaseStep(StepOnePhase)
}

/* Super Phase Step Instant Effect */

type stepSuperPhase struct { }
func (ssp *stepSuperPhase) applyTo(uid int, subAction *SubAction) {
	subAction.SetSuperPhaseStep(StepOneSuperPhase)
}

/* Set Draw to True Instant Effect */

type setDidDraw struct { }
func (sdd *setDidDraw) applyTo(uid int, subAction *SubAction) {
	subAction.SetDidDraw(true)
}

/* Do Nothing Instant Effect */

type doNothing struct { }
func (dn *doNothing) applyTo(uid int, subAction *SubAction) { }

/* Direct Damage Instant Effect */

type directDamageInstantEffect struct {
	amount int
	elementType ElementType
}
func (dd *directDamageInstantEffect) applyTo(uid int, subAction *SubAction) {
	subAction.SetDamage(dd.amount)
	subAction.SetElementType(dd.elementType)
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

/* Only valid when haven't drawn */

type validHaveNotDrawn struct { }
func (vhnd *validHaveNotDrawn) isValid(game *Game, uid int, action *Action) bool {
	return !game.hasDrawn
}

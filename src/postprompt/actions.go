package postprompt

/* Public InstantList constructors */

func GetDirectDamageIL(amount int, elementType ElementType) InstantList {
	//instantList := make(InstantList,0)
	instant := new(Instant)
	instant.effect = []InstantEffect{
		&directDamageInstantEffect{amount, elementType}}
	instant.conds = []InstantCond{
		new(validInstant)}
	return []*Instant{instant}
}

func GetPhaseStepIL() InstantList {
	instant := new(Instant)
	instant.effect = []InstantEffect{new(stepPhase)}
	instant.conds = []InstantCond{
		&validSuperPhase{MainSuperPhase},
		new(validTurnOwner)}
	return []*Instant{instant}
}
func GetDrawIL() InstantList {
	instant := new(Instant)
	instant.effect = []InstantEffect{
		newCardMoveInstantEffect(PlayerTypeMe, Deck, -1, PlayerTypeMe, Hand, -1,false),
		&setDidDraw{true}}
	instant.conds = []InstantCond{
		&validPhase{DrawPhase},
		&validSuperPhase{MainSuperPhase},
		new(validTurnOwner),
		new(validHaveNotDrawn)}
	return []*Instant{instant}
}

func GetTurnStepIL() InstantList {
	instant := new(Instant)
	instant.effect = []InstantEffect{
		new(stepTurn),
		&setDidDraw{false}}
	instant.conds = []InstantCond{
		&validSuperPhase{MainSuperPhase},
		&validPhase{EndPhase},
		new(validTurnOwner)}
	return []*Instant{instant}
}

func GetSetupIL() InstantList {
	instant := new(Instant)
	instant.effect = []InstantEffect{
		new(stepSuperPhase),
		&shuffler{PlayerTypeMe},
		&shuffler{PlayerTypeThem},
		newCardMoveInstantEffect(PlayerTypeMe, Deck, -1, PlayerTypeMe, Hand, -1,false),
		newCardMoveInstantEffect(PlayerTypeMe, Deck, -1, PlayerTypeMe, Hand, -1,false),
		newCardMoveInstantEffect(PlayerTypeMe, Deck, -1, PlayerTypeMe, Hand, -1,false),
		newCardMoveInstantEffect(PlayerTypeMe, Deck, -1, PlayerTypeMe, Hand, -1,false),
		newCardMoveInstantEffect(PlayerTypeMe, Deck, -1, PlayerTypeMe, Hand, -1,false),
		newCardMoveInstantEffect(PlayerTypeThem, Deck, -1, PlayerTypeThem, Hand, -1,false),
		newCardMoveInstantEffect(PlayerTypeThem, Deck, -1, PlayerTypeThem, Hand, -1,false),
		newCardMoveInstantEffect(PlayerTypeThem, Deck, -1, PlayerTypeThem, Hand, -1,false),
		newCardMoveInstantEffect(PlayerTypeThem, Deck, -1, PlayerTypeThem, Hand, -1,false),
		newCardMoveInstantEffect(PlayerTypeThem, Deck, -1, PlayerTypeThem, Hand, -1,false)}
	instant.conds = []InstantCond{
		&validSuperPhase{PreSuperPhase}}
	return []*Instant{instant}
}

func GetEmptyIL() InstantList {
	instant := new(Instant)
	instant.effect = []InstantEffect{
		new(doNothing)}
	instant.conds = []InstantCond{
		new(validInstant)}
	return []*Instant{instant}
}

func GetPlayMoveCardIL(srcIndex int) InstantList {
	instant := new(Instant)
	instant.effect = []InstantEffect{
		newCardMoveInstantEffect(PlayerTypeMe, Hand, srcIndex, PlayerTypeMe, Active, -1,false)}
	instant.conds = []InstantCond{
		&validPhase{MainPhase},
		&validSuperPhase{MainSuperPhase}}
	return []*Instant{instant}
}

func GetCardDestroyFromHand(srcIndex int) *Instant {
	instant := new(Instant)
	instant.effect = []InstantEffect{
		newCardMoveInstantEffect(PlayerTypeThem, Hand, srcIndex, PlayerTypeThem, Grave, -1,true)}
	instant.conds = []InstantCond{
		new(validInstant)}
	return instant
}

func GetCardExpire(givenPlayerType PlayerType, srcIndex int) *Instant {
	instant := new(Instant)
	instant.effect = []InstantEffect{
		newCardMoveInstantEffect(givenPlayerType, Active, srcIndex, givenPlayerType, Grave, -1,false)}
	instant.conds = []InstantCond{
		new(validInstant)}
	return instant
}

/* Instant Effects */

/* Shuffle the player's deck */

type shuffler struct {
	playerType PlayerType
}

func (sh *shuffler) applyTo(uid int, subAction *SubAction) {
	subAction.SetDoShuffle(true, sh.playerType)
}

/* Card Move Instant Effect */

func newCardMoveInstantEffect(
		srcPlayerType PlayerType,
		srcList CLType,
		srcIndex int,
		dstPlayerType PlayerType,
		dstList CLType,
		dstIndex int,
		safe bool) InstantEffect {
	cm := new(cardMoveInstantEffect)
	cm.srcPlayerType = srcPlayerType
	cm.srcList = srcList
	cm.srcIndex = srcIndex
	cm.dstPlayerType = dstPlayerType
	cm.dstList = dstList
	cm.dstIndex = dstIndex
	cm.safe = safe
	return cm
}

type cardMoveInstantEffect struct {
	srcPlayerType PlayerType
	srcList       CLType
	srcIndex      int
	dstPlayerType PlayerType
	dstList       CLType
	dstIndex      int
	safe          bool
}

func (cm *cardMoveInstantEffect) applyTo(uid int, subAction *SubAction) {
	subAction.SetMovement(cm.srcPlayerType,
		cm.srcList,
		cm.srcIndex,
		cm.dstPlayerType,
		cm.dstList,
		cm.dstIndex,
		cm.safe)
}

/* Turn Swap Instant Effect */

type stepTurn struct{}

func (st *stepTurn) applyTo(uid int, subAction *SubAction) {
	subAction.SetTurnStep(true)
}

/* Phase Step Instant Effect */

type stepPhase struct{}

func (sp *stepPhase) applyTo(uid int, subAction *SubAction) {
	subAction.SetPhaseStep(StepOnePhase)
}

/* Super Phase Step Instant Effect */

type stepSuperPhase struct{}

func (ssp *stepSuperPhase) applyTo(uid int, subAction *SubAction) {
	subAction.SetSuperPhaseStep(StepOneSuperPhase)
}

/* Set Draw to True Instant Effect */

type setDidDraw struct {
	didDraw bool
}

func (sdd *setDidDraw) applyTo(uid int, subAction *SubAction) {
	subAction.SetDidDraw(sdd.didDraw)
}

/* Do Nothing Instant Effect */

type doNothing struct{}

func (dn *doNothing) applyTo(uid int, subAction *SubAction) {}

/* Direct Damage Instant Effect */

type directDamageInstantEffect struct {
	amount      int
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

type validInstant struct{}

func (vi *validInstant) isValid(game *Game, uid int, action *Action) bool {
	return true
}

/* Only valid on your turn */

type validTurnOwner struct{}

func (vto *validTurnOwner) isValid(game *Game, uid int, action *Action) bool {
	return uid == game.turnOwner
}

/* Only valid when haven't drawn */

type validHaveNotDrawn struct{}

func (vhnd *validHaveNotDrawn) isValid(game *Game, uid int, action *Action) bool {
	return !game.hasDrawn
}

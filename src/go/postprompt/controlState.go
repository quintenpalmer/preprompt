package postprompt

type Phase int
type SuperPhase int

const (
	DrawPhase Phase = iota
	PrePhase
	MainPhase
	EndPhase
	StepOnePhase = 1
)

const (
	PreSuperPhase SuperPhase = iota
	MainSuperPhase
	DoneSuperPhase
	StepOneSuperPhase = 1
)

type ControlState struct {
	uids [2]int
	phase Phase
	superPhase SuperPhase
	turnOwner int
	hasDrawn bool
}

func NewControlState(uid1, uid2 int) *ControlState {
	controlState := new(ControlState)
	controlState.uids = [2]int{uid1,uid2}
	controlState.phase = 0
	controlState.superPhase = 0
	controlState.turnOwner = uid1
	controlState.hasDrawn = false
	return controlState
}

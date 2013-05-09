package postprompt

type phase int
type superPhase int

type controlState struct {
	uids [2]int
	currentPhase phase
	currentSuperPhase superPhase
	turnOwner int
	hasDrawn bool
}

func NewControlState(uid1, uid2 int) *controlState {
	c := new(controlState)
	c.uids = [2]int{uid1,uid2}
	c.currentPhase = 0
	c.currentSuperPhase = 0
	c.turnOwner = uid1
	c.hasDrawn = false
	return c
}

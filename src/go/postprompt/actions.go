package postprompt

import "fmt"

func GetDirectDamage(amount int) *instantList {
	fmt.Println("Making a direct damage")
	il := new(instantList)
	il.instants  = []*instant{NewDirectDamageInstant(amount)}
	return il
}

func NewDirectDamageInstant(amount int) *instant {
	fmt.Println("Making a dd instant")
	i := new(instant)
	e := new(directDamageInstantEffect)
	e.amount = amount
	i.ieffect = e
	i.iconds = []instantCond{new(validInstant)}
	return i
}

type directDamageInstantEffect struct {
	amount int
}

func (dd *directDamageInstantEffect) applyTo(sub *subAction) {
	fmt.Println("applying")
	sub.SetDamage(dd.amount)
}

type validInstant struct {
}

func (vi *validInstant) isValid(g *game, sub *subAction) bool {
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
	sub.setMovement(destroy.playerNum,GetIndexFromName("active"),destroy.srcCard,destroy.playerNum,GetIndexFromName("grave"),-1)
}

func GetPhaseInstantList() *instantList {
	i := new(instantList)
	i.instants = []*instant{NewInstant()}
	return i
}
*/

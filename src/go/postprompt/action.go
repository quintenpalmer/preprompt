package postprompt

import (
	queue "container/list"
	"fmt"
)

type action struct {
	subActions *queue.List
}

type subAction struct {
	g *game
	uid int
	inst *instant
	damage int
	heal int
	/*
	eType elementType = elementType.neutral
	moving boolean = false
	srcPlayerType int = 0
	srcList int = 0
	srcIndex int = 0
	dstPlayerType int = 0
	dstList int = 0
	dstIndex int = 0
	phase boolean = false
	turn boolean = false
	*/
}

func Act(g *game, uid int, iList *instantList) error {
	a := new(action)
	a.subActions = new(queue.List)
	for _,inst := range iList.instants {
		a.subActions.PushBack(NewSubAction(g,uid,inst))
	}
	// sort?
	for {
		front := a.subActions.Front()
		if front == nil { break }
		sub := a.subActions.Remove(front)
		if sub == nil { break }
		s, ok := sub.(*subAction)
		if !ok { return Newpperror("Element was not SubAction somehow?") }
        if err := s.act(); err != nil { return err }
		fmt.Println(ok)
		// destroy cards that don't exist for both players
	}
	return nil
}

func NewSubAction(g *game, uid int, inst *instant) *subAction {
	s := new(subAction)
	s.uid = uid
	s.g = g
	s.inst = inst
	return s
}

func (s *subAction) act() error {
	s.inst.applyTo(s,s.g)
    // Apply others to this
    me, err := s.g.GetMeFromUid(s.uid)
    if err != nil { return err }
    me.health -= s.damage
    them, err := s.g.GetThemFromUid(s.uid)
    if err != nil { return err }
    them.health += s.heal
	return nil
}

func (s *subAction) SetDamage(amount int) {
	s.damage = amount
}

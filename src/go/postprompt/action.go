package postprompt

import (
	"container/list"
)

type ActionList list.List

type Action struct {
	game *Game
	uid int
	instant *Instant

	damage int
	heal int
	elementType ElementType
	/*
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

func NewAction(game *Game, uid int, instant *Instant) *Action {
	action := new(Action)
	action.uid = uid
	action.game = game
	action.instant = instant
	action.elementType = neutral
	return action
}

func Act(game *Game, uid int, instantList *InstantList) error {
	action := new(list.List)
	for _,instant := range instantList.instants {
		action.PushBack(NewAction(game,uid,instant))
	}
	// sort?
	for {
		front := action.Front()
		if front == nil {
			break
		}
		sub := action.Remove(front)
		s, ok := sub.(*Action)
		if !ok {
			return Newpperror("Element was not Action somehow?")
		}
		if err := s.act(); err != nil {
			return err
		}
		// destroy cards that don't exist for both players
	}
	return nil
}

func (action *Action) act() error {
	action.instant.applyTo(action,action.game)
	// Apply others to this

	me, err := action.game.GetMeFromUid(action.uid)
	if err != nil {
		return err
	}
	me.health += action.heal

	them, err := action.game.GetThemFromUid(action.uid)
	if err != nil {
		return err
	}
	them.health -= action.damage

	return nil
}

func (action *Action) SetDamage(amount int) {
	action.damage = amount
}

func (action *Action) SetHeal(amount int) {
	action.heal = amount
}

/*
func (s *Action) SetMovement(srcPlayer, srcList, srcCardLoc, dstPlayer, dstList, dstCardLoc, int) {
	
}
*/

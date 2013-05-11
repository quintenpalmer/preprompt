package postprompt

import "container/list"

type ActionList list.List

type Action struct {
	game *Game
	uid int
	instant *Instant

	damage int
	heal int
	elementType ElementType
	movement *Movement
	phase bool
	turn bool
}

type Movement struct {
	srcPlayerType PlayerType
	srcList CLType
	srcIndex int
	dstPlayerType PlayerType
	dstList CLType
	dstIndex int
}

func NewAction(game *Game, uid int, instant *Instant) *Action {
	action := new(Action)
	action.uid = uid
	action.game = game
	action.instant = instant
	action.elementType = neutral
	action.movement = nil
	action.phase = false
	action.turn = false
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
	them, err := action.game.GetThemFromUid(action.uid)
	if err != nil {
		return err
	}
	me.health += action.heal
	them.health -= action.damage

	var player *Player
	if action.movement != nil {
		if action.movement.srcPlayerType == 0 {
			player = me
		} else {
			player = them
		}
		card := player.collection.cardList[action.movement.srcList].cards[action.movement.srcIndex]
		if action.movement.dstPlayerType == 0 {
			player = me
		} else {
			player = them
		}
		player.collection.cardList[action.movement.dstList].push(card,action.movement.dstIndex)
	}

	return nil
}

func (action *Action) SetDamage(amount int) {
	action.damage = amount
}

func (action *Action) SetHeal(amount int) {
	action.heal = amount
}

func (action *Action) SetElementType(elementType ElementType){
	action.elementType = elementType
}

func (action *Action) SetMovement(
		srcPlayerType PlayerType,
		srcList CLType,
		srcIndex int,
		dstPlayerType PlayerType,
		dstList CLType,
		dstIndex int) {
	action.movement = new(Movement)
	action.movement.srcPlayerType = srcPlayerType
	action.movement.srcList = srcList
	action.movement.srcIndex = srcIndex
	action.movement.dstPlayerType = dstPlayerType
	action.movement.dstList = dstList
	action.movement.dstIndex = dstIndex
}

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
	superPhaseStep SuperPhase
	phaseStep Phase
	turnStep bool
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
	action.superPhaseStep = 0
	action.phaseStep = 0
	action.turnStep = false
	return action
}

func Act(game *Game, uid int, instantList *InstantList) (string, error) {
	action := new(list.List)
	for _,instant := range instantList.instants {
		action.PushBack(NewAction(game,uid,instant))
	}
	// sort?
	fullMessage := ""
	for {
		front := action.Front()
		if front == nil {
			break
		}
		sub := action.Remove(front)
		s, ok := sub.(*Action)
		if !ok { return fullMessage, Newpperror("Element was not Action somehow?") }
		message, err := s.act()
		if err != nil { return fullMessage, err }
		if message != "ok" { fullMessage = fullMessage + message }
		// destroy cards that don't exist for both players
	}
	if fullMessage == "" { fullMessage = "ok" }
	return fullMessage, nil
}

func (action *Action) act() (string, error) {
	statusString := action.instant.applyTo(action,action.game)
	if statusString != "ok" { return statusString, nil }
	// Apply others to this

	me, err := action.game.GetMeFromUid(action.uid)
	if err != nil {
		return "error", err
	}
	them, err := action.game.GetThemFromUid(action.uid)
	if err != nil {
		return "error", err
	}
	me.health += action.heal
	them.health -= action.damage

	if action.game.controlState.superPhase + action.superPhaseStep <= DoneSuperPhase {
		action.game.controlState.superPhase += action.superPhaseStep
	} else { return "reached end super phase", nil }
	if action.game.controlState.phase + action.phaseStep <= EndPhase {
		action.game.controlState.phase += action.phaseStep
	} else { return "reached end phase", nil }

	if action.turnStep {
		if action.game.controlState.turnOwner == action.game.controlState.uids[0] {
			action.game.controlState.turnOwner = action.game.controlState.uids[1]
		} else {
			action.game.controlState.turnOwner = action.game.controlState.uids[0]
		}
		action.game.controlState.phase = DrawPhase
	}

	var player *Player
	if action.movement != nil {
		if action.movement.srcPlayerType == 0 {
			player = me
		} else {
			player = them
		}
		card, err := player.collection.cardList[action.movement.srcList].pop(action.movement.srcIndex)
		if err != nil { return "error", err }
		if action.movement.dstPlayerType == 0 {
			player = me
		} else {
			player = them
		}
		err = player.collection.cardList[action.movement.dstList].push(card,action.movement.dstIndex)
		if err != nil { return "problem", err }
	}

	return "ok", nil
}

func (action *Action) SetDamage(amount int) {
	action.damage = amount
}

func (action *Action) SetHeal(amount int) {
	action.heal = amount
}

func (action *Action) SetElementType(elementType ElementType) {
	action.elementType = elementType
}

func (action *Action) SetPhaseStep(amount Phase) {
	action.phaseStep += amount
}

func (action *Action) SetSuperPhaseStep(amount SuperPhase) {
	action.superPhaseStep += amount
}

func (action *Action) SetTurnStep(turnStep bool) {
	action.turnStep = turnStep
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

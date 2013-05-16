package postprompt

import "container/list"

type ActionList list.List

type Action struct {
	game *Game
	uid int
	instant *Instant
	subActions []*SubAction
}

type SubAction struct {
	damage int
	heal int
	elementType ElementType
	movement *Movement
	superPhaseStep SuperPhase
	phaseStep Phase
	turnStep bool
	hasSetDidDraw bool
	didDraw bool
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
	return action
}

func NewSubAction() *SubAction {
	subAction := new(SubAction)
	subAction.elementType = Neutral
	subAction.movement = nil
	subAction.superPhaseStep = 0
	subAction.phaseStep = 0
	subAction.turnStep = false
	subAction.hasSetDidDraw = false
	subAction.didDraw = false
	return subAction
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
		subActions, err := s.instant.applyTo(s,s.game,s.uid)
		if err != nil { return "", err }
		for _,subAction := range subActions {
			message, err := subAction.act(s)
			if err != nil { return fullMessage, err }
			if message != "ok" { fullMessage = fullMessage + message }
		}
		// destroy cards that don't exist for both players
	}
	if fullMessage == "" { fullMessage = "ok" }
	return fullMessage, nil
}

func (subAction *SubAction) act(action *Action) (string, error) {
	// Apply others to this

	me, err := action.game.GetMeFromUid(action.uid)
	if err != nil {
		return "error", err
	}
	them, err := action.game.GetThemFromUid(action.uid)
	if err != nil {
		return "error", err
	}
	me.health += subAction.heal
	them.health -= subAction.damage

	if action.game.superPhase + subAction.superPhaseStep <= DoneSuperPhase {
		action.game.superPhase += subAction.superPhaseStep
	} else { return "reached end super phase", nil }
	if action.game.phase + subAction.phaseStep <= EndPhase {
		action.game.phase += subAction.phaseStep
	} else { return "reached end phase", nil }

	if subAction.turnStep {
		if action.game.turnOwner == action.game.uids[0] {
			action.game.turnOwner = action.game.uids[1]
		} else {
			action.game.turnOwner = action.game.uids[0]
		}
		action.game.phase = DrawPhase
	}

	var player *Player
	if subAction.movement != nil {
		if subAction.movement.srcPlayerType == 0 {
			player = me
		} else {
			player = them
		}
		card, err := player.cardList[subAction.movement.srcList].pop(subAction.movement.srcIndex)
		if err != nil { return "error", err }
		if subAction.movement.dstPlayerType == 0 {
			player = me
		} else {
			player = them
		}
		err = player.cardList[subAction.movement.dstList].push(card,subAction.movement.dstIndex)
		if err != nil { return "problem", err }
	}

	if subAction.hasSetDidDraw {
		action.game.hasDrawn = subAction.didDraw
	}

	return "ok", nil
}

func (subAction *SubAction) SetDamage(amount int) {
	subAction.damage = amount
}

func (subAction *SubAction) SetHeal(amount int) {
	subAction.heal = amount
}

func (subAction *SubAction) SetElementType(elementType ElementType) {
	subAction.elementType = elementType
}

func (subAction *SubAction) SetPhaseStep(amount Phase) {
	subAction.phaseStep += amount
}

func (subAction *SubAction) SetSuperPhaseStep(amount SuperPhase) {
	subAction.superPhaseStep += amount
}

func (subAction *SubAction) SetTurnStep(turnStep bool) {
	subAction.turnStep = turnStep
}

func (subAction *SubAction) SetMovement(
		srcPlayerType PlayerType,
		srcList CLType,
		srcIndex int,
		dstPlayerType PlayerType,
		dstList CLType,
		dstIndex int) {
	subAction.movement = new(Movement)
	subAction.movement.srcPlayerType = srcPlayerType
	subAction.movement.srcList = srcList
	subAction.movement.srcIndex = srcIndex
	subAction.movement.dstPlayerType = dstPlayerType
	subAction.movement.dstList = dstList
	subAction.movement.dstIndex = dstIndex
}

func (subAction *SubAction) SetDidDraw(didDraw bool) {
	subAction.hasSetDidDraw = true
	subAction.didDraw = didDraw
}

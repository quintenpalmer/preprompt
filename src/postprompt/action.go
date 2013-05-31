package postprompt

import "math/rand"

type FullAction struct {
	actions ActionList
}

type ActionList []*Action

type Action struct {
	instant *Instant
}

type SubAction struct {
	damage         int
	doesDamage     bool
	heal           int
	doesHeal       bool
	elementType    ElementType
	movement       *Movement
	superPhaseStep SuperPhase
	phaseStep      Phase
	turnStep       bool
	hasSetDidDraw  bool
	didDraw        bool
	doShuffle      bool
	whoShuffle     PlayerType
}

type Movement struct {
	srcPlayerType PlayerType
	srcList       CLType
	srcIndex      int
	dstPlayerType PlayerType
	dstList       CLType
	dstIndex      int
}

func NewAction(instant *Instant) *Action {
	action := new(Action)
	action.instant = instant
	return action
}

func NewSubAction() *SubAction {
	subAction := new(SubAction)
	subAction.elementType = Neutral
	subAction.damage = 0
	subAction.doesDamage = false
	subAction.heal = 0
	subAction.doesHeal = false
	subAction.movement = nil
	subAction.superPhaseStep = 0
	subAction.phaseStep = 0
	subAction.turnStep = false
	subAction.hasSetDidDraw = false
	subAction.didDraw = false
	subAction.doShuffle = false
	return subAction
}

func Act(game *Game, uid int, instantList InstantList) (string, error) {
	fullAction := new(FullAction)
	fullAction.actions = make([]*Action, 0)
	for _, instant := range instantList {
		fullAction.actions = append(fullAction.actions, NewAction(instant))
	}

	// TODO sort all of the actions on to-exist field

	me, err := game.GetMeFromUid(uid)
	if err != nil {
		return "", err
	}
	them, err := game.GetThemFromUid(uid)
	if err != nil {
		return "", err
	}
	enemyuid := them.uid

	fullMessage := ""
	for len(fullAction.actions) > 0 {
		var action *Action
		action, fullAction.actions = fullAction.actions[len(fullAction.actions)-1], fullAction.actions[:len(fullAction.actions)-1]
		subActions, err := action.instant.applyTo(action, game, uid)
		if err != nil {
			return "", err
		}

		for _, subAction := range subActions {
			// Activate all triggers
			for _, card := range me.cardList[Active] {
				for _, trigger := range card.triggers {
					trigger.applyTo(subAction, action, fullAction, game, uid)
				}
			}
			for _, card := range them.cardList[Active] {
				for _, trigger := range card.triggers {
					trigger.applyTo(subAction, action, fullAction, game, enemyuid)
				}
			}
			// Do the deed
			message, err := subAction.act(game, uid)
			if err != nil {
				return fullMessage, err
			}
			if message != "ok" {
				fullMessage = fullMessage + message
			}
		}
		// Destroy cards that don't exist for both players
		for index, card := range me.cardList[Active] {
			if !card.persists.doesPersist(game) {
				fullAction.actions = append(fullAction.actions, NewAction(GetCardExpire(PlayerTypeMe, index)))
				break
			}
		}
		for index, card := range them.cardList[Active] {
			if !card.persists.doesPersist(game) {
				fullAction.actions = append(fullAction.actions, NewAction(GetCardExpire(PlayerTypeThem, index)))
				break
			}
		}
	}
	if fullMessage == "" {
		fullMessage = "ok"
	}
	return fullMessage, nil
}

func (subAction *SubAction) act(game *Game, uid int) (string, error) {
	// TODO Apply triggers to this

	me, err := game.GetMeFromUid(uid)
	if err != nil {
		return "error", err
	}
	them, err := game.GetThemFromUid(uid)
	if err != nil {
		return "error", err
	}
	me.health += subAction.heal
	them.health -= subAction.damage

	if subAction.doShuffle {
		var player *Player
		if subAction.whoShuffle == PlayerTypeMe {
			player = me
		} else if subAction.whoShuffle == PlayerTypeThem {
			player = them
		} else {
			return "invalid PlayerType given to shuffle", nil
		}
		deck := player.cardList[Deck]
		startSize := len(deck)
		newSlice := make([]*Card, 0)
		for i := startSize; i > 0; i-- {
			r := rand.Intn(i)
			newSlice = append(newSlice, deck[r])
			deck = append(deck[:r], deck[r+1:]...)
		}
		player.cardList[Deck] = newSlice
	}

	if game.superPhase+subAction.superPhaseStep <= DoneSuperPhase {
		game.superPhase += subAction.superPhaseStep
	} else {
		return "reached end super phase", nil
	}
	if game.phase+subAction.phaseStep <= EndPhase {
		game.phase += subAction.phaseStep
	} else {
		return "reached end phase", nil
	}

	if subAction.turnStep {
		if game.turnOwner == game.uids[0] {
			game.turnOwner = game.uids[1]
		} else {
			game.turnOwner = game.uids[0]
		}
		game.phase = DrawPhase
		for _, card := range them.cardList[Active] {
			card.persists.tick()
		}
	}

	var player *Player
	if subAction.movement != nil {
		if subAction.movement.srcPlayerType == 0 {
			player = me
		} else {
			player = them
		}
		card, err := player.pop(subAction.movement.srcList, subAction.movement.srcIndex)
		if err != nil {
			return "error", err
		}
		if subAction.movement.dstPlayerType == 0 {
			player = me
		} else {
			player = them
		}
		err = player.push(subAction.movement.dstList, card, subAction.movement.dstIndex)
		if err != nil {
			return "problem", err
		}
	}

	if subAction.hasSetDidDraw {
		game.hasDrawn = subAction.didDraw
	}

	return "ok", nil
}

func (subAction *SubAction) SetDamage(amount int) {
	subAction.damage = amount
	subAction.doesDamage = true
}

func (subAction *SubAction) IncreaseDamage(amount int) {
	if subAction.doesDamage {
		subAction.damage += amount
	}
}

func (subAction *SubAction) SetHeal(amount int) {
	subAction.heal = amount
	subAction.doesHeal = true
}

func (subAction *SubAction) IncreaseHeal(amount int) {
	if subAction.doesHeal {
		subAction.heal += amount
	}
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

func (subAction *SubAction) SetDoShuffle(doShuffle bool, playerType PlayerType) {
	subAction.doShuffle = doShuffle
	subAction.whoShuffle = playerType
}

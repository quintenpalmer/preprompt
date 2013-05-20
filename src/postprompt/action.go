package postprompt

type ActionList []*Action

type Action struct {
	instant *Instant
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

func NewAction(instant *Instant) *Action {
	action := new(Action)
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

func Act(game *Game, uid int, instantList InstantList) (string, error) {
	actions := make([]*Action,0)
	for _,instant := range instantList {
		actions = append(actions,NewAction(instant))
	}
	// TODO sort all of the actions on to-exist field
	fullMessage := ""
	for len(actions) > 0{
		var action *Action
		action, actions = actions[len(actions)-1], actions[:len(actions)-1]
		subActions, err := action.instant.applyTo(action,game,uid)
		if err != nil { return "", err }
		for _,subAction := range subActions {
			message, err := subAction.act(game,uid)
			if err != nil { return fullMessage, err }
			if message != "ok" { fullMessage = fullMessage + message }
		}
		// TODO Destroy cards that don't exist for both players
		var index int = 0
		me, err := game.GetMeFromUid(uid)
		if err != nil { return "", err }
		for _, card := range me.cardList[Active] {
			if ! card.persists.doesPersist(game) {
				actions = append(actions, NewAction(GetCardExpire(index)))
				break
			}
			index++
		}
		them, err := game.GetThemFromUid(uid)
		if err != nil { return "", err }
		index = 0
		for _, card := range them.cardList[Active] {
			if ! card.persists.doesPersist(game) {
				actions = append(actions, NewAction(GetCardExpire(index)))
				break
			}
			index++
		}
	}
	if fullMessage == "" { fullMessage = "ok" }
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

	if game.superPhase + subAction.superPhaseStep <= DoneSuperPhase {
		game.superPhase += subAction.superPhaseStep
	} else { return "reached end super phase", nil }
	if game.phase + subAction.phaseStep <= EndPhase {
		game.phase += subAction.phaseStep
	} else { return "reached end phase", nil }

	if subAction.turnStep {
		if game.turnOwner == game.uids[0] {
			game.turnOwner = game.uids[1]
		} else {
			game.turnOwner = game.uids[0]
		}
		game.phase = DrawPhase
	}

	var player *Player
	if subAction.movement != nil {
		if subAction.movement.srcPlayerType == 0 {
			player = me
		} else {
			player = them
		}
		card, err := player.pop(subAction.movement.srcList,subAction.movement.srcIndex)
		if err != nil { return "error", err }
		if subAction.movement.dstPlayerType == 0 {
			player = me
		} else {
			player = them
		}
		err = player.push(subAction.movement.dstList,card,subAction.movement.dstIndex)
		if err != nil { return "problem", err }
	}

	if subAction.hasSetDidDraw {
		game.hasDrawn = subAction.didDraw
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

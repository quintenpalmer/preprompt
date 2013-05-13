package postprompt

func handleCommand(buf []byte, model *Model) string {
	jsonRequest, err := loadJson(buf)
	if  err != nil {
		respondError(err)
	}
	request, err := jsonRequest.getMap("request")
	if err != nil {
		return respondError(err)
	}
	command, err := request.getString("command")
	if err != nil {
		respondError(err)
	}
	switch command {
		case "new" : return handleNewGame(request,model)
		case "setup" : return handleSetup(request,model)
		case "draw" : return handleDraw(request,model)
		case "phase" : return handlePhase(request,model)
		case "turn" : return handleTurn(request,model)
	}
	return respondOther(command)
}

func getStandardInfo(r jsonMap, m *Model) (int, int, *Game, error) {
	gameId, err := r.getInt("gameId")
	if err != nil { return 0, 0, nil, err }
	playerId, err := r.getInt("playerId")
	if err != nil { return 0, 0, nil, err }
	game, err := m.GetGameFromGameId(gameId)
	if err != nil { return 0, 0, nil, err }
	return gameId, playerId, game, nil
}

func handleNewGame(r jsonMap, m *Model) string {
	p1_uid, err := r.getInt("p1_uid")
	if err != nil { return respondError(err) }
	p1_did, err := r.getInt("p1_did")
	if err != nil { return respondError(err) }
	p2_uid, err := r.getInt("p2_uid")
	if err != nil { return respondError(err) }
	p2_did, err := r.getInt("p2_did")
	if err != nil { return respondError(err) }
	g,i,err := m.AddGame(p1_uid,p1_did,p2_uid,p2_did)
	gameRepr, err := getGameJsonMap(g,p1_uid)
	if err != nil { return respondError(err) }
	return respondNew(i,gameRepr)
}

func handleDraw(r jsonMap, m *Model) string {
	gameId, playerId, game, err := getStandardInfo(r,m)
	if err != nil { return respondError(err) }
	message, err := Act(game,playerId,GetDrawIL())
	if err != nil { return respondError(err) }
	gameRepr, err := getGameJsonMap(game,playerId)
	if err != nil { return respondError(err) }
	return respondAction("draw",gameId,gameRepr,message)
	//Act(g,playerId,GetDirectDamageIL(5,fire))
}

func handleSetup(r jsonMap, m *Model) string {
	gameId, playerId, game, err := getStandardInfo(r,m)
	if err != nil { return respondError(err) }
	message, err := Act(game,playerId,GetSetupIL())
	if err != nil { return respondError(err) }
	gameRepr, err := getGameJsonMap(game,playerId)
	if err != nil { return respondError(err) }
	return respondAction("setup",gameId,gameRepr,message)
}

func handlePhase(r jsonMap, m *Model) string {
	gameId, playerId, game, err := getStandardInfo(r,m)
	if err != nil { return respondError(err) }
	message, err := Act(game,playerId,GetPhaseStepIL())
	if err != nil { return respondError(err) }
	gameRepr, err := getGameJsonMap(game,playerId)
	if err != nil { return respondError(err) }
	return respondAction("setup",gameId,gameRepr,message)
}

func handleTurn(r jsonMap, m *Model) string {
	gameId, playerId, game, err := getStandardInfo(r,m)
	if err != nil { return respondError(err) }
	message, err := Act(game,playerId,GetTurnStepIL())
	if err != nil { return respondError(err) }
	gameRepr, err := getGameJsonMap(game,playerId)
	if err != nil { return respondError(err) }
	return respondAction("turn",gameId,gameRepr,message)
}

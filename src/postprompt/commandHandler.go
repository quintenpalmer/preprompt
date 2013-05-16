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
		case "setup" : return handleBuiltinAction(request,model,GetSetupIL(),command)
		case "draw" : return handleBuiltinAction(request,model,GetDrawIL(),command)
		case "phase" : return handleBuiltinAction(request,model,GetPhaseStepIL(),command)
		case "turn" : return handleBuiltinAction(request,model,GetTurnStepIL(),command)
		case "out" : return handleBuiltinAction(request,model,GetEmptyIL(),command)
		case "play" : return handleCardPlay(request,model)
		case "list" : return handleList(request,model)
	}
	return respondOther(command)
}

func handleNewGame(request jsonMap, m *Model) string {
	p1_uid, err := request.getInt("p1_uid")
	if err != nil { return respondError(err) }
	p1_did, err := request.getInt("p1_did")
	if err != nil { return respondError(err) }
	p2_uid, err := request.getInt("p2_uid")
	if err != nil { return respondError(err) }
	p2_did, err := request.getInt("p2_did")
	if err != nil { return respondError(err) }
	g,i,err := m.AddGame(p1_uid,p1_did,p2_uid,p2_did)
	if err != nil { return respondError(err) }
	gameRepr, err := GetGameJsonMap(g,p1_uid)
	if err != nil { return respondError(err) }
	return respondNew(i,gameRepr)
}

func handleCardPlay(request jsonMap, m *Model) string {
	gameId, err := request.getInt("gameId")
	if err != nil { return respondError(err) }
	playerId, err := request.getInt("playerId")
	if err != nil { return respondError(err) }
	/*
	srcList, err := request.getInt("srcList")
	if err != nil { return respondError(err) }
	*/
	srcCard, err := request.getInt("srcCard")
	if err != nil { return respondError(err) }
	/*
	targetUid, err := request.getInt("targetUid")
	if err != nil { return respondError(err) }
	targetList, err := request.getInt("targetList")
	if err != nil { return respondError(err) }
	targetCard, err := request.getInt("targetCard")
	if err != nil { return respondError(err) }
	*/
	game, err := m.GetGameFromGameId(gameId)
	if err != nil { return respondError(err) }
	message, err := Act(game,playerId,GetDestroyIL(srcCard))
	if err != nil { return respondError(err) }
	gameRepr, err := GetGameJsonMap(game,playerId)
	if err != nil { return respondError(err) }
	return respondAction("play",gameId,gameRepr,message)
}

func handleBuiltinAction(request jsonMap,m *Model, myInstantList InstantList, command string) string {
	gameId, err := request.getInt("gameId")
	if err != nil { return respondError(err) }
	playerId, err := request.getInt("playerId")
	if err != nil { return respondError(err) }
	game, err := m.GetGameFromGameId(gameId)
	if err != nil { return respondError(err) }
	message, err := Act(game,playerId,myInstantList)
	if err != nil { return respondError(err) }
	gameRepr, err := GetGameJsonMap(game,playerId)
	if err != nil { return respondError(err) }
	return respondAction(command,gameId,gameRepr,message)
}

func handleList(request jsonMap,m *Model) string {
	// TODO Only return the games that this player is playing
	gameIds := make([]int,len(m.games))
	i := 0
	for k,_ := range m.games {
		gameIds[i] = k
		i++
	}
	return respondList(gameIds)
}
//Act(g,playerId,GetDirectDamageIL(5,Fire))

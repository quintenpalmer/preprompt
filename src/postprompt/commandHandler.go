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
	}
	return respondOther(command)
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

func handleBuiltinAction(r jsonMap, m*Model, myInstantList *InstantList, command string) string{
	gameId, err := r.getInt("gameId")
	if err != nil { return respondError(err) }
	playerId, err := r.getInt("playerId")
	if err != nil { return respondError(err) }
	game, err := m.GetGameFromGameId(gameId)
	if err != nil { return respondError(err) }
	message, err := Act(game,playerId,myInstantList)
	if err != nil { return respondError(err) }
	gameRepr, err := getGameJsonMap(game,playerId)
	if err != nil { return respondError(err) }
	return respondAction(command,gameId,gameRepr,message)
}

//Act(g,playerId,GetDirectDamageIL(5,Fire))

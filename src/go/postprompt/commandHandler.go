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
		case "draw" : return handleDraw(request,model)
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

func handleDraw(r jsonMap, m *Model) string {
	gameId, err := r.getInt("gameId")
	if err != nil { return respondError(err) }
	playerId, err := r.getInt("playerId")
	if err != nil { return respondError(err) }
	g, err := m.GetGameFromGameId(gameId)
	if err != nil { return respondError(err) }
	Act(g,playerId,GetDraw())
	//Act(g,playerId,GetDirectDamage(5,fire))
	gameRepr, err := getGameJsonMap(g,playerId)
	if err != nil { return respondError(err) }
	return respondAction("draw",gameId,gameRepr)
}

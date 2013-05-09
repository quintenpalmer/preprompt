package postprompt

import (
	"encoding/json"
)

func handleCommand(buf []byte, m *model) string {
	var jsonRequest jsonMap
	err := json.Unmarshal(buf, &jsonRequest)
	if err != nil {
		return respondError(err)
	}
	r, ok := jsonRequest["request"].(map[string]interface{})
	if !ok { return respondError(Newpperror("Not a map inside the map")) }
	c, ok := r["command"].(string)
	if !ok { return respondError(Newpperror("Not a string inside the map")) }

	switch c {
		case "new" : return handleNewGame(r,m)
		case "draw" : return handleDraw(r,m)
	}
	return respondOther(c)
}

func handleNewGame(r jsonMap, m *model) string {
	p1_uid, err := r.getInt("p1_uid")
	if err !=nil { return respondError(err) }
	p1_did, err := r.getInt("p1_did")
	if err !=nil { return respondError(err) }
	p2_uid, err := r.getInt("p2_uid")
	if err !=nil { return respondError(err) }
	p2_did, err := r.getInt("p2_did")
	if err !=nil { return respondError(err) }
	g,i,err := m.AddGame(p1_uid,p1_did,p2_uid,p2_did)
	gameRepr, err := getGameJsonMap(g,p1_uid)
	if err != nil { return respondError(err) }
	return respondNew(i,gameRepr)
}

func handleDraw(r jsonMap, m *model) string {
	gameId, err := r.getInt("gameId")
	if err !=nil { return respondError(err) }
	playerId, err := r.getInt("playerId")
	if err !=nil { return respondError(err) }
	g, err := m.GetGameFromGameId(gameId)
	if err != nil { return respondError(err) }
	Act(g,playerId,GetDirectDamage(5))
	gameRepr, err := getGameJsonMap(g,playerId)
	if err != nil { return respondError(err) }
	return respondAction("draw",gameId,gameRepr)
}

package postprompt

import (
	"encoding/json"
	"strconv"
)

type jsonMap map[string]interface{}

func getGameJsonMap(g *game, uid int) (jsonMap, error) {
	containerJson := make(jsonMap)
	gJson := make(jsonMap)
	player, err := g.GetMeFromUid(uid)
	if err != nil { return make(jsonMap), err }
	gJson["me"] = serializePlayer(player,0)
	player, err = g.GetThemFromUid(uid)
	if err != nil { return make(jsonMap), err }
	gJson["them"] = serializePlayer(player,0)
	gJson["controlState"] = serializeControlState(g.controlState)
	containerJson["game"] = gJson
	return containerJson, nil
}

func SerializeGame(g *game, uid int) (string, error) {
	containerJson := make(jsonMap)
	gJson := make(jsonMap)
	player, err := g.GetMeFromUid(uid)
	if err != nil { return "", err }
	gJson["me"] = serializePlayer(player,0)
	player, err = g.GetThemFromUid(uid)
	if err != nil { return "", err }
	gJson["them"] = serializePlayer(player,0)
	gJson["controlState"] = serializeControlState(g.controlState)
	containerJson["game"] = gJson
	ret, err := containerJson.toString()
	if err != nil { return "", err }
	return ret, nil
}

func serializePlayer(p *player, pt PlayerType) jsonMap {
	pJson := make(jsonMap)
	pJson["uid"] = p.uid
	pJson["health"] = p.health
	pJson["name"] = p.name
	pJson["deck"] = serializeDeck(p.d,pt)
	return pJson
}

func serializeControlState(c *controlState) jsonMap {
	cJson := make(jsonMap)
	cJson["uids"] = c.uids
	cJson["currentPhase"] = c.currentPhase
	cJson["currentSuperPhase"] = c.currentSuperPhase
	cJson["turnOwner"] = c.turnOwner
	cJson["hasDrawn"] = c.hasDrawn
	return cJson
}

func serializeDeck(d *deck, pt PlayerType) jsonMap {
	dJson := make(jsonMap)
	for i,cardList := range d.cl{
		index, err := GetNameFromIndex(i)
		if err != nil { }
		dJson[index] = serializeCardList(cardList, true)
	}
	return dJson
}

func serializeCardList(cl *cardList, full bool) jsonMap {
	clJson := make(jsonMap)
	array := []jsonMap{}
	for _,c := range cl.cards {
		cJson := make(jsonMap)
		cJson["card"] = serializeCard(c)
		array = append(array,cJson)
	}
	clJson["cards"] = array
	return clJson
}

func serializeCard(c *card) jsonMap {
	cJson := make(jsonMap)
	cJson["name"] = c.name
	cJson["effect"] = c.effect
	return cJson
}

func (repr jsonMap) toString() (string, error) {
	str, err := json.Marshal(repr)
	if err != nil { return "", err }
	return string(str), nil
}

func (repr jsonMap) getInt(key string) (int, error) {
	tmpString, ok := repr[key].(string)
	if !ok { return 0,Newpperror("Not an string inside the map") }
	retInt, err := strconv.Atoi(tmpString)
	if err != nil { return 0,Newpperror("Cound not conver to to") }
	return retInt, nil
}

func (repr jsonMap) getString(key string) (string, error) {
	retString, ok := repr[key].(string)
	if !ok { return "",Newpperror("Not an string inside the map") }
	return retString, nil
}

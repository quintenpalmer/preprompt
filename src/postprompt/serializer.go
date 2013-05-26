package postprompt

import (
	"encoding/json"
	"io/ioutil"
	"strconv"
)

type jsonMap map[string]interface{}

func GetGameJsonMap(g *Game, uid int) (jsonMap, error) {
	containerJson := make(jsonMap)
	gJson := make(jsonMap)
	player, err := g.GetMeFromUid(uid)
	if err != nil {
		return make(jsonMap), err
	}
	gJson["me"] = serializePlayer(player, 0)
	player, err = g.GetThemFromUid(uid)
	if err != nil {
		return make(jsonMap), err
	}
	gJson["them"] = serializePlayer(player, 0)
	gJson["uids"] = g.uids
	gJson["phase"] = g.phase
	gJson["superPhase"] = g.superPhase
	gJson["turnOwner"] = g.turnOwner
	gJson["hasDrawn"] = g.hasDrawn
	containerJson["game"] = gJson
	return containerJson, nil
}

func PrintGame(g *Game, uid int) error {
	gameRepr, err := SerializeGame(g, uid)
	if err != nil {
		return err
	}
	err = ioutil.WriteFile("out.json", []byte(gameRepr), 0644)
	if err != nil {
		return err
	}
	return nil
}

func SerializeGame(g *Game, uid int) (string, error) {
	containerJson, err := GetGameJsonMap(g, uid)
	if err != nil {
		return "", err
	}
	ret, err := containerJson.toString()
	if err != nil {
		return "", err
	}
	return ret, nil
}

func serializePlayer(p *Player, pt PlayerType) jsonMap {
	pJson := make(jsonMap)
	pJson["uid"] = p.uid
	pJson["health"] = p.health
	pJson["name"] = p.name
	for i, cardList := range p.cardList {
		index, err := GetNameFromIndex(i)
		if err != nil {
		}
		pJson[index] = serializeCardList(cardList, true)
	}
	return pJson
}

func serializeCardList(cl CardList, full bool) jsonMap {
	clJson := make(jsonMap)
	array := []jsonMap{}
	for _, c := range cl {
		cJson := make(jsonMap)
		cJson["card"] = serializeCard(c)
		array = append(array, cJson)
	}
	clJson["cards"] = array
	return clJson
}

func serializeCard(c *Card) jsonMap {
	cJson := make(jsonMap)
	cJson["name"] = c.name
	cJson["effect"] = "effect"
	return cJson
}

func (repr jsonMap) toString() (string, error) {
	str, err := json.Marshal(repr)
	if err != nil {
		return "", err
	}
	return string(str), nil
}

func (repr jsonMap) getInt(key string) (int, error) {
	tmpString, ok := repr[key].(string)
	if !ok {
		return 0, Newpperror("Not an int inside the map")
	}
	retInt, err := strconv.Atoi(tmpString)
	if err != nil {
		return 0, Newpperror("Cound not conver to to")
	}
	return retInt, nil
}

func (repr jsonMap) getString(key string) (string, error) {
	retString, ok := repr[key].(string)
	if !ok {
		return "", Newpperror("Not an string inside the map")
	}
	return retString, nil
}

func (repr jsonMap) getMap(key string) (jsonMap, error) {
	retMap, ok := repr[key].(map[string]interface{})
	if !ok {
		return nil, Newpperror("Not a map inside the map")
	}
	return retMap, nil
}

func loadJson(buf []byte) (jsonMap, error) {
	jsonRepr := make(jsonMap)
	err := json.Unmarshal(buf, &jsonRepr)
	if err != nil {
		return nil, err
	}
	return jsonRepr, nil
}

package postprompt

import (
	"encoding/json"
	"strconv"
	"fmt"
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

	if c == "new" {
		sp1_uid, ok := r["p1_uid"].(string)
		if !ok { return respondError(Newpperror("Not an string inside the map")) }
		p1_uid,err := strconv.Atoi(sp1_uid)
		if err != nil { return respondError(Newpperror("Cound not conver to to")) }
		sp1_did, ok := r["p1_did"].(string)
		if !ok { return respondError(Newpperror("Not an string inside the map")) }
		p1_did,err := strconv.Atoi(sp1_did)
		if err != nil { return respondError(Newpperror("Cound not conver to to")) }
		sp2_uid, ok := r["p2_uid"].(string)
		if !ok { return respondError(Newpperror("Not an string inside the map")) }
		p2_uid,err := strconv.Atoi(sp2_uid)
		if err != nil { return respondError(Newpperror("Cound not conver to to")) }
		sp2_did, ok := r["p2_did"].(string)
		if !ok { return respondError(Newpperror("Not an string inside the map")) }
		p2_did,err := strconv.Atoi(sp2_did)
		if err != nil { return respondError(Newpperror("Cound not conver to to")) }
		g,i,err := m.AddGame(p1_uid,p1_did,p2_uid,p2_did)
		gameRepr, err := getGameJsonMap(g,p1_uid)
		if err != nil { return respondError(err) }
		fmt.Println("---------------")
		fmt.Println(c=="new")
		fmt.Println("---------------")
		return respondNew(i,gameRepr)
	}
	return respondOther(c)
}

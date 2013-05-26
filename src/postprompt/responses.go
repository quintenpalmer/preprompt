package postprompt

import "fmt"

func respondOther(command string) string {
	fmt.Println(command)
	resp := make(jsonMap)
	resp["respType"] = "unsupported"
	resp["command"] = command
	ret, err := resp.toString()
	if err != nil {
		return respondError(err)
	}
	return ret
}

func respondAction(command string, gameId int, gameRepr jsonMap, message string) string {
	fmt.Println(command, " : ", gameId)
	resp := make(jsonMap)
	resp["respType"] = "ok"
	resp["command"] = command
	resp["gameId"] = gameId
	resp["gameRepr"] = gameRepr
	resp["message"] = message
	ret, err := resp.toString()
	if err != nil {
		return respondError(err)
	}
	return ret
}

func respondNew(gameId int, gameRepr jsonMap) string {
	fmt.Println("new : ", gameId)
	resp := make(jsonMap)
	resp["respType"] = "ok"
	resp["command"] = "new"
	resp["gameId"] = gameId
	resp["gameRepr"] = gameRepr
	resp["message"] = "ok"
	ret, err := resp.toString()
	if err != nil {
		return respondError(err)
	}
	return ret
}

func respondError(err error) string {
	fmt.Println(err)
	resp := make(jsonMap)
	resp["respType"] = "error"
	ret, err2 := resp.toString()
	if err2 != nil {
	}
	return ret
}

func respondList(gameIds []int) string {
	resp := make(jsonMap)
	resp["respType"] = "ok"
	resp["command"] = "list"
	resp["gameId"] = gameIds
	ret, err := resp.toString()
	if err != nil {
		return respondError(err)
	}
	return ret
}

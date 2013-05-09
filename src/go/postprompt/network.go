package postprompt

import (
	"net"
	"fmt"
)

const (
	RECV_BUF_LEN = 1024
)

func Listen(port string, m *model) {
	ln, err := net.Listen("tcp", ":"+port)
	if err != nil { fmt.Println("Could not listen on port") }

	for {
		conn, err := ln.Accept()
		if err != nil {
			fmt.Println("Error accepting connection")
			continue
		}
		go handleConnection(conn,m)
	}
}

func handleConnection(conn net.Conn, m *model) {
	fmt.Println("handling a connection")
	buf := make([]byte,RECV_BUF_LEN)
	n, err := conn.Read(buf)
	if err != nil {
		conn.Write([]byte(respondError(err)))
		return
	}
	buf = buf[0:n]
	conn.Write([]byte(handleCommand(buf,m)+"\n"))
}

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

func respondNew(gameId int, gameRepr jsonMap) string {
	fmt.Println("new : ",gameId)
	resp := make(jsonMap)
	resp["respType"] = "ok"
	resp["command"] = "new"
	resp["gameId"] = gameId
	resp["gameRepr"] = gameRepr
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
	if err2 != nil { }
	return ret
}

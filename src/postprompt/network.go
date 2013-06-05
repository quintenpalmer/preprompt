package postprompt

import (
	"fmt"
	"net"
)

const (
	RECV_BUF_LEN = 1024
)

func Listen(port string, m *Model) {
	ln, err := net.Listen("tcp", ":"+port)
	if err != nil {
		fmt.Println("Could not listen on port : " + port)
		return
	}
	fmt.Println("Listening on port : " + port)
	running := true
	for running {
		conn, err := ln.Accept()
		if err != nil {
			fmt.Println("Error accepting connection")
			continue
		}
		running = handleConnection(conn, m)
	}
}

func handleConnection(conn net.Conn, m *Model) bool {
	fmt.Println("Handling a connection")
	buf := make([]byte, RECV_BUF_LEN)
	n, err := conn.Read(buf)
	if err != nil {
		conn.Write([]byte(respondError(err)))
		return false
	}
	buf = buf[0:n]
	response := handleCommand(buf, m)
	if response == "exit" {
		return false
	} else {
		conn.Write([]byte(response + "\n"))
		return true
	}
}

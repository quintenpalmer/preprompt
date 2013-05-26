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

	for {
		conn, err := ln.Accept()
		if err != nil {
			fmt.Println("Error accepting connection")
			continue
		}
		go handleConnection(conn, m)
	}
}

func handleConnection(conn net.Conn, m *Model) {
	fmt.Println("Handling a connection")
	buf := make([]byte, RECV_BUF_LEN)
	n, err := conn.Read(buf)
	if err != nil {
		conn.Write([]byte(respondError(err)))
		return
	}
	buf = buf[0:n]
	conn.Write([]byte(handleCommand(buf, m) + "\n"))
}

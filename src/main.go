package main

import (
	"fmt"
	"os"
	"postprompt"
)

func main(){
	port := "52690"
	if len(os.Args) == 2 {
		port = os.Args[1]
	}
	model := postprompt.NewModel()
	fmt.Println("Starting PostPrompt!")
	postprompt.Listen(port,model)
}

package main

import (
	"fmt"
	"go/postprompt"
)

func main(){
	m := postprompt.NewModel()
	fmt.Println("Starting PostPrompt")
	fmt.Println(m)
	postprompt.AddGame(m,1,1,2,1)
}

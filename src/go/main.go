package main

import (
	"fmt"
	"go/postprompt"
	//"io/ioutil"
)

func main(){
	m := postprompt.NewModel()
	fmt.Println("Starting PostPrompt")
	postprompt.Listen("52690",m)
	/*
	g := m.AddGame(1,0,2,0)
	err := ioutil.WriteFile("out.json",[]byte(postprompt.SerializeGame(g,1)),0644)
	if err != nil { panic(err) }
	*/
}

package postprompt

import "testing"

func TestFull(t *testing.T) {
	port := "52690"
	model := NewModel()
	Listen(port,model)
}

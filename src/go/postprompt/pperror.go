package postprompt

type pperror struct {
	message string
}

func Newpperror(message string) pperror {
	p := new(pperror)
	p.message = message
	return *p
}

func (p pperror) Error() string {
	return p.message
}

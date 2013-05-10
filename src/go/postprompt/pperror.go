package postprompt

type PPerror struct {
	message string
}

func Newpperror(message string) PPerror {
	pperror := new(PPerror)
	pperror.message = message
	return *pperror
}

func (pperror PPerror) Error() string {
	return pperror.message
}

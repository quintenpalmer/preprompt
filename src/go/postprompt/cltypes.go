package postprompt

//TODO make a general util file (maybe PlayerTypes as well)

type CLType int

const numcl = 6

const (
	Deck CLType = iota
	Hand
	Active
	Grave
	Special
	Other
)

type CLInfo struct {
	i CLType
	name string
}

var CLTypes [6]CLInfo = [6]CLInfo{
	CLInfo{Deck,"deck"},
	CLInfo{Hand,"hand"},
	CLInfo{Active,"active"},
	CLInfo{Grave,"grave"},
	CLInfo{Special,"special"},
	CLInfo{Other,"other"}}

func GetNameFromIndex(i CLType) (string, error) {
	for _,cli := range CLTypes {
		if i == cli.i {
			return cli.name, nil
		}
	}
	//TODO return error if not found
	return "", Newpperror("Not a valid cardList index")
}

func GetIndexFromName(name string) (CLType, error) {
	for _,cli := range CLTypes {
		if name == cli.name {
			return cli.i, nil
		}
	}
	//TODO return error if not found
	return 0, Newpperror("Not a valid cardList name")
}

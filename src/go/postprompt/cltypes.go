package postprompt

//TODO make a general util file (maybe PlayerTypes as well)

type CLType int

const (
	Deck int = iota
	Hand
	Active
	Grave
	Special
	Other
)

const numcl = 6

type CLInfo struct {
	i int
	name string
}

var CLTypes [6]CLInfo = [6]CLInfo{
	CLInfo{Deck,"deck"},
	CLInfo{Hand,"hand"},
	CLInfo{Active,"active"},
	CLInfo{Grave,"grave"},
	CLInfo{Special,"special"},
	CLInfo{Other,"other"}}

func GetNameFromIndex(i int) (string, error) {
	for _,cli := range CLTypes {
		if i == cli.i {
			return cli.name, nil
		}
	}
	//TODO return error if not found
	return "", Newpperror("Not a valid cardList index")
}

func GetIndexFromName(name string) (int, error) {
	for _,cli := range CLTypes {
		if name == cli.name {
			return cli.i, nil
		}
	}
	//TODO return error if not found
	return 0, Newpperror("Not a valid cardList name")
}

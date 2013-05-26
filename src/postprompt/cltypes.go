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
	index  int
	cltype CLType
	name   string
}

var CLTypes [6]CLInfo = [6]CLInfo{
	CLInfo{0, Deck, "deck"},
	CLInfo{1, Hand, "hand"},
	CLInfo{2, Active, "active"},
	CLInfo{3, Grave, "grave"},
	CLInfo{4, Special, "special"},
	CLInfo{5, Other, "other"}}

func GetNameFromIndex(cltype CLType) (string, error) {
	for _, cli := range CLTypes {
		if cltype == cli.cltype {
			return cli.name, nil
		}
	}
	return "", Newpperror("Not a valid cardList index")
}

func GetIndexFromName(name string) (CLType, error) {
	for _, cli := range CLTypes {
		if name == cli.name {
			return cli.cltype, nil
		}
	}
	return 0, Newpperror("Not a valid cardList name")
}

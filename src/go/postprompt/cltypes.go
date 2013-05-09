package postprompt

//TODO make a general util file (maybe PlayerTypes as well)

type clIndex struct {
	i int
	name string
}

var CLTypes [6]clIndex = [6]clIndex{
	clIndex{0,"deck"},
	clIndex{1,"hand"},
	clIndex{2,"active"},
	clIndex{3,"grave"},
	clIndex{4,"special"},
	clIndex{5,"other"}}

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

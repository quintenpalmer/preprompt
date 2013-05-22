package postprompt

type PersistList []Persist

type Persist interface {
	tick()
	doesPersist(game *Game) bool
	reset()
}

func (persistList PersistList) tick() {
	for _,persist := range persistList {
		persist.tick()
	}
}

func (persistList PersistList) doesPersist(game *Game) bool {
	retDoesPersist := true
	for _,persist := range persistList {
		retDoesPersist = retDoesPersist && persist.doesPersist(game)
	}
	return retDoesPersist
}

func getPersists(persistRepr interface{}) (PersistList, error) {
	persistList := make(PersistList,0)
	persistArray, ok := persistRepr.([]interface{})
	if ! ok { return nil, Newpperror("Could not load persist array from json") }
	for _, persisti := range persistArray {
		persistRepr, ok := persisti.(map[string]interface{})
		if ! ok { return nil, Newpperror("Could not load persist from json") }
		persist, err := getPersistFromType(persistRepr)
		if err != nil { return nil, err }
		persistList = append(persistList,persist)
	}
	//fmt.Println(persistRepr)
	return persistList, nil
}

func getPersistFromType(persistRepr map[string]interface{}) (Persist, error) {
	persistType, ok := persistRepr["type"].(string)
	if ! ok { return nil, Newpperror("Could not load instant effect type from json") }
	switch persistType {
		case "Timer" : return getPersistTimer(persistRepr)
		case "NoPersist" : return getNoPersist(persistRepr)
		default : return nil, Newpperror("Invalid Instant Effect Type found : " + persistType)
	}
	return nil, Newpperror("Invalid Instant Effect Type found : " + persistType)
}

func getPersistTimer(persistRepr map[string]interface{}) (Persist, error) {
	params, ok := persistRepr["params"].(map[string]interface{})
	if ! ok { return nil, Newpperror("Could not load instant persist params from json") }
	amountFloat, ok := params["duration"].(float64)
	amount := int(amountFloat)
	if ! ok { return nil, Newpperror("Could not load instant persist param amount from json") }
	pt := new(persistTimer)
	pt.currDuration = amount
	pt.origDuration = amount
	return pt, nil
}

func getNoPersist(persistRepr map[string]interface{}) (Persist, error) {
	return new(noPersist), nil
}

type noPersist struct { }

func (np *noPersist) tick () { }
func (np *noPersist) reset() { }
func (np *noPersist) doesPersist(game *Game) bool { return false }

type persistTimer struct {
	currDuration int
	origDuration int
}

func (pt *persistTimer) tick() {
	pt.currDuration -= 1
}

func (pt *persistTimer) reset() {
	pt.currDuration = pt.origDuration
}

func (pt *persistTimer) doesPersist(game *Game) bool {
	return pt.currDuration > 0
}

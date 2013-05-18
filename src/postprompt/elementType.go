package postprompt

type ElementType int

const numElementTypes = 7

const (
	Neutral ElementType = iota
	Fire
	Water
	Earch
	Wind
	Dark
	Light
)

type ElementTypeInfo struct {
	elementType ElementType
	name string
}

var ElementTypes [numElementTypes]ElementTypeInfo = [numElementTypes]ElementTypeInfo{
	ElementTypeInfo{Neutral,"Neutral"},
	ElementTypeInfo{Fire,"Fire"},
	ElementTypeInfo{Water,"Water"},
	ElementTypeInfo{Earch,"Earch"},
	ElementTypeInfo{Wind,"Wind"},
	ElementTypeInfo{Dark,"Dark"},
	ElementTypeInfo{Light,"Light"}}

func getElementTypeFromString(elementString string) (ElementType, error) {
	for _,eti := range ElementTypes {
		if elementString == eti.name {
			return eti.elementType , nil
		}
	}
	return 0, Newpperror("Not a valid element string" + elementString)
}

func getStringTypeFromElement(elementType ElementType) (string, error) {
	for _,eti := range ElementTypes {
		if elementType == eti.elementType {
			return eti.name, nil
		}
	}
	return "", Newpperror("Not a valid element type")
}

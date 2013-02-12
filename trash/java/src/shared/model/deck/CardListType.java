package shared.model.deck;

public enum CardListType{
	stack(0,"vStack"),hand(1,"vHand"),active(2,"vField"),grave(3,"vGrave");

	int index;
	String string;

	CardListType(int newIndex, String newString){
		index = newIndex;
		string = newString;
	}

	public int getIndex(){
		return index;
	}

	public String getString(){
		return string;
	}

	/*
	public CardListType getCardListType(int checkIndex){
		switch(checkIndex){
			case 0: return CardListType.stack;
			case 1: return CardListType.hand;
			case 2: return CardListType.field;
			case 3: return CardListType.grave;
			case 4: return CardListType.other;
			default : return CardListType.other;
		}
	}
	*/
}

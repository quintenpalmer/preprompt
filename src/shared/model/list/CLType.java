package shared.model.list;

public enum CLType{
	stack(0,"vStack"),hand(1,"vHand"),active(2,"vField"),grave(3,"vGrave");

	int index;
	String string;

	CLType(int newIndex, String newString){
		index = newIndex;
		string = newString;
	}

	public int i(){
		return index;
	}

	public String str(){
		return string;
	}

	public CLType getCardListType(int checkIndex){
		switch(checkIndex){
			case 0: return CLType.stack;
			case 1: return CLType.hand;
			case 2: return CLType.active;
			case 3: return CLType.grave;
			default : return null;
		}
	}
}

package control;

import model.effect.*;
import model.Effect;
import model.ElementType;
import model.Card;

public class CardLoader{

	public static Card getDirectDamage(String name, ElementType elementType, int amount){
		InstantList ilist = new InstantList();
		//{new Instant(new DirectDamage(elementType,amount),{new ValidActivate()})},Phase.main);
		PersistList plist = new PersistList();
		PersistActivateList palist = new PersistActivateList();
		Effect effect = new Effect(ilist,plist,palist);
		return new Card(name,effect);
	}
}

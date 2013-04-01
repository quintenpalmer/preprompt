package control;

import java.util.ArrayList;

import model.effect.*;
import model.Effect;
import model.ElementType;
import model.Card;

public class CardLoader{

	public static Card getDirectDamage(String name, ElementType[] elementType, int amount){
		int[] validTurns = {2};
		InstantList ilist = new InstantList(new ArrayList<Instant>(),validTurns);
		//{new Instant(new DirectDamage(elementType,amount),{new ValidActivate()})},Phase.main);
		PersistList plist = new PersistList();
		PersistActivateList palist = new PersistActivateList();
		Effect effect = new Effect(ilist,plist,palist,elementType);
		return new Card(name,effect);
	}
}

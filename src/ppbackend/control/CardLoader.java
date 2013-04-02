package ppbackend.control;

import java.util.ArrayList;

import ppbackend.model.*;
import ppbackend.model.Effect;
import ppbackend.model.ElementType;
import ppbackend.model.Card;

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

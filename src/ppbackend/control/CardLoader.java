package ppbackend.control;

import java.util.ArrayList;

import ppbackend.model.*;
import ppbackend.model.Effect;
import ppbackend.model.ElementType;
import ppbackend.model.Card;

public class CardLoader{

	public static Card getDirectDamage(String name, ElementType elementType, int amount){
		Instant instant = new Instant(new DirectDamage(4,elementType), new InstantCond[]{});
		InstantList ilist = new InstantList(new Instant[]{instant},new int[]{2});
		//{new Instant(new DirectDamage(elementType,amount),{new ValidActivate()})},Phase.main);
		PersistList plist = new PersistList();
		PersistActivateList palist = new PersistActivateList();
		Effect effect = new Effect(ilist,plist,palist,elementType);
		return new Card(name,effect);
	}
}

class DirectDamage implements InstantEffect{
	int amount;
	ElementType elementType;

	public DirectDamage(int amount, ElementType elementType){
		this.amount = amount;
		this.elementType = elementType;
	}

	public void applyTo(ActionSub action){
		action.setDamage(this.amount);
		action.setElementType(this.elementType);
	}
}

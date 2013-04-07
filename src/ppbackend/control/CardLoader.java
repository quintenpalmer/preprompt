package ppbackend.control;

import java.util.ArrayList;

import ppbackend.model.mainStruct.*;
import ppbackend.model.effect.*;
import ppbackend.model.shared.ElementType;
import ppbackend.model.action.SubAction;

public class CardLoader{

	public static Card getDirectDamage(String name, ElementType elementType, int amount){
		Instant instant = new Instant(new DirectDamage(4,elementType), new InstantCond[]{new ValidInstant()});
		InstantList ilist = new InstantList(new Instant[]{instant},new int[]{2});
		//{new Instant(new DirectDamage(elementType,amount),{new ValidActivate()})},Phase.main);
		PersistList plist = new PersistList(new Persist[]{new DoesNotPersist()},false);
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

	public void applyTo(SubAction action){
		action.setDamage(this.amount);
		action.setElementType(this.elementType);
	}
}
class ValidInstant implements InstantCond{
	public boolean isValid(Game game, SubAction action){
		return true;
	}
}

class DoesNotPersist implements Persist{
	public boolean doesPersist(){
		return false;
	}
	public void tick(){
	}
	public void reset(){
	}
}

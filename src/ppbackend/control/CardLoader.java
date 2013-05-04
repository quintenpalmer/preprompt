package ppbackend.control;

import java.util.ArrayList;

import ppbackend.model.mainStruct.*;
import ppbackend.model.effect.*;
import ppbackend.model.shared.*;
import ppbackend.model.action.SubAction;

public class CardLoader{

	public static Card getDirectDamage(String name, ElementType elementType, int amount){
		InstantList ilist = new InstantList(
			new Instant[]{
				new Instant(
					new DirectDamage(4,elementType),
					new InstantCond[]{
						new ValidInstant()
					}
				)
			},
			new int[]{Phase.main}
		);
		PersistList plist = new PersistList(
			new Persist[]{
				new DoesNotPersist()
			}
		);
		PersistActivateList palist = new PersistActivateList();
		Effect effect = new Effect(ilist,plist,palist,elementType);
		return new Card(name,effect);
	}

	public static Card getDamangeIncreaser(String name, ElementType elementType, int duration){
		InstantList ilist = new InstantList(
			new Instant[]{
				new Instant(
					new DoNothing(),
					new InstantCond[]{
						new ValidInstant()
					}
				)
			},
			new int[]{Phase.main}
		);
		PersistList plist = new PersistList(
			new Persist[]{
				new StandardCountdown(
					duration
				)
			}
		);
		PersistActivateList palist = new PersistActivateList();
		Effect effect = new Effect(ilist,plist,palist,elementType);
		return new Card(name,effect);
	}

	public static InstantList getDrawEffect(){
		return new InstantList(
			new Instant[]{
				new Instant(
					new DrawEffect(),
					new InstantCond[]{
						new ValidInstant()
					}
				)
			},
			new int[]{Phase.main}
		);
	}

	public static InstantList getPhaseEffect(){
		return new InstantList(
			new Instant[]{
				new Instant(
					new PhaseEffect(),
					new InstantCond[]{
						new ValidInstant()
					}
				)
			},
			new int[]{Phase.main}
		);
	}

	public static InstantList getTurnEffect(){
		return new InstantList(
			new Instant[]{
				new Instant(
					new TurnEffect(),
					new InstantCond[]{
						new ValidInstant()
					}
				)
			},
			new int[]{Phase.main}
		);
	}

	public static InstantList getPlayEffect(int srcCard,int dstList){
		return new InstantList(
			new Instant[]{
				new Instant(
					new PlayEffect(srcCard,dstList),
					new InstantCond[]{
						new ValidInstant()
					}
				)
			},
			new int[]{Phase.main}
		);
	}
}

class TurnEffect implements InstantEffect{
	public void applyTo(SubAction action){
		action.setTurn(true);
	}
}

class PhaseEffect implements InstantEffect{
	public void applyTo(SubAction action){
		action.setPhase(true);
	}
}

class PlayEffect implements InstantEffect{
	int dstList;
	int srcCard;

	public PlayEffect(int srcCard, int dstList){
		this.dstList = dstList;
		this.srcCard = srcCard;
	}

	public void applyTo(SubAction action){
		action.setMovement(0,CLTypes.hand,this.srcCard,0,this.dstList,-1);
	}
}

class DrawEffect implements InstantEffect{
	public void applyTo(SubAction action){
		action.setMovement(0,CLTypes.deck,-1,0,CLTypes.hand,-1);
	}
}

class DoNothing implements InstantEffect{
	public DoNothing(){

	}

	public void applyTo(SubAction action){

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

class StandardCountdown implements Persist{
	int duration;
	int startingDuration;

	public StandardCountdown(int duration){
		this.duration = duration;
		this.startingDuration = duration;
	}
	public boolean doesPersist(){
		System.out.println(this.duration);
		return this.duration > 0;
	}
	public void tick(){
		this.duration -= 1;
	}
	public void reset(){
		this.duration = this.startingDuration;
	}
}

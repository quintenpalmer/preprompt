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
		PersistActivateList palist = new PersistActivateList(
			new PersistActivate[]{
				new NoAlter()
			}
		);
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
		PersistActivateList palist = new PersistActivateList(
			new PersistActivate[]{
				new IncreaseAlter(elementType,3)
			}
		);
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

	public static InstantList getPlayEffect(int srcCard){
		return new InstantList(
			new Instant[]{
				new Instant(
					new PlayEffect(srcCard),
					new InstantCond[]{
						new ValidInstant()
					}
				)
			},
			new int[]{Phase.main}
		);
	}

	public static Instant getDestroyEffect(int srcCard,int playerNum){
		return new Instant(
			new DestroyEffect(srcCard,playerNum),
			new InstantCond[]{
				new ValidInstant()
			}
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

class DestroyEffect implements InstantEffect{
	int srcCard;
	int playerNum;

	public DestroyEffect(int srcCard, int playerNum){
		this.srcCard = srcCard;
		this.playerNum = playerNum;
	}

	public void applyTo(SubAction action){
		action.setMovement(this.playerNum,CLTypes.active,this.srcCard,this.playerNum,CLTypes.grave,-1);
	}
}

class PlayEffect implements InstantEffect{
	int srcCard;

	public PlayEffect(int srcCard){
		this.srcCard = srcCard;
	}

	public void applyTo(SubAction action){
		action.setMovement(0,CLTypes.hand,this.srcCard,0,CLTypes.active,-1);
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
		return this.duration > 0;
	}
	public void tick(){
		this.duration -= 1;
	}
	public void reset(){
		this.duration = this.startingDuration;
	}
}

class NoAlter implements PersistActivate{
	public void applyTo(Game game, SubAction action, int playerType){
	}
}

class IncreaseAlter implements PersistActivate{
	ElementType elementType;
	int amount;

	public IncreaseAlter(ElementType elementType, int amount){
		this.elementType = elementType;
		this.amount = amount;
	}

	public void applyTo(Game game, SubAction action, int playerType){
		if(playerType == 0){
			if(action.getElementType() == this.elementType){
				action.increaseDamage(amount);
			}
		}
	}
}

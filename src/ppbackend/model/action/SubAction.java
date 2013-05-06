package ppbackend.model.action;

import pplib.exceptions.*;
import ppbackend.model.shared.*;
import ppbackend.model.mainStruct.*;
import ppbackend.model.effect.*;
import ppbackend.model.shared.ElementType;

public class SubAction{
	Game game;
	PlayerContainer me;
	PlayerContainer them;
	Instant instant;
	ElementType elementType = ElementType.neutral;
	int damage = 0;
	int heal = 0;
	boolean moving = false;
	int srcPlayerType = 0;
	int srcList = 0;
	int srcIndex = 0;
	int dstPlayerType = 0;
	int dstList = 0;
	int dstIndex = 0;
	boolean phase = false;
	boolean turn = false;

	public SubAction(Game game, int uid, Instant instant) throws PPGameActionException{
		this.me = game.getMeFromUid(uid);
		this.them = game.getThemFromUid(uid);
		this.game = game;
		this.instant = instant;
	}

	public void act() throws PPGameActionException{
		this.instant.applyTo(this.game,this);

		for(Card card : this.me.getDeck().getCardList(CLTypes.active).getCards()){
			for (PersistActivate pactivate : card.getEffect().getPersistActivateList().getPersistActivates()){
				System.out.println(pactivate);
				pactivate.applyTo(this.game,this,0);
			}
		}

		for(Card card : this.them.getDeck().getCardList(CLTypes.active).getCards()){
			for (PersistActivate pactivate : card.getEffect().getPersistActivateList().getPersistActivates()){
				System.out.println(pactivate);
				pactivate.applyTo(this.game,this,1);
			}
		}

		this.them.getPlayer().receiveDamage(this.damage);
		this.me.getPlayer().receiveHeal(this.heal);
		if(this.moving){
			PlayerContainer player;
			if(this.srcPlayerType == 0){
				player = this.me;
			}
			else{
				player = this.them;
			}
			Card card = player.getDeck().getCardList(this.srcList).pop(this.srcIndex);
			if(this.dstPlayerType == 0){
				player = this.me;
			}
			else{
				player = this.them;
			}
			player.getDeck().getCardList(this.dstList).push(card,this.dstIndex);
		}
		if(this.phase){
			this.game.getControlState().stepPhase(this.me.getPlayer().getUid());
		}
		if(this.turn){
			this.game.getControlState().toggleTurn(this.me.getPlayer().getUid());
			for(Card card : this.them.getDeck().getCardList(CLTypes.active).getCards()){
				card.getEffect().getPersistList().tick();
			}
		}
	}

	public void setDamage(int amount){
		this.damage = amount;
	}
	public void increaseDamage(int amount){
		this.damage += amount;
	}
	public void setHeal(int amount){
		this.heal = amount;
	}
	public void setElementType(ElementType elementType){
		this.elementType = elementType;
	}
	public ElementType getElementType(){
		return this.elementType;
	}
	public void setMovement(int srcPlayerType, int srcList, int srcIndex, int dstPlayerType, int dstList, int dstIndex){
		this.moving = true;
		this.srcPlayerType = srcPlayerType;
		this.srcList = srcList;
		this.srcIndex = srcIndex;
		this.dstPlayerType = dstPlayerType;
		this.dstList = dstList;
		this.dstIndex = dstIndex;
	}
	public void setPhase(boolean phase){
		this.phase = phase;
	}
	public void setTurn(boolean turn){
		this.turn = turn;
	}
}

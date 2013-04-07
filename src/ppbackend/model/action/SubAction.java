package ppbackend.model.action;

import pplib.exceptions.*;
import ppbackend.model.mainStruct.*;
import ppbackend.model.effect.Instant;
import ppbackend.model.shared.ElementType;

public class SubAction{
	Game game;
	PlayerContainer me;
	PlayerContainer them;
	Instant instant;
	ElementType elementType = ElementType.neutral;
	int damage = 0;
	int heal = 0;

	public SubAction(Game game, int uid, Instant instant) throws PPGameActionException{
		this.me = game.getMeFromUid(uid);
		this.them = game.getThemFromUid(uid);
		this.game = game;
		this.instant = instant;
	}

	public void act() throws PPGameActionException{
		this.instant.applyTo(this.game,this);
		this.them.getPlayer().receiveDamage(this.damage);
		this.me.getPlayer().receiveHeal(this.heal);
	}

	public void setDamage(int amount){
		this.damage = amount;
	}
	public void setHeal(int amount){
		this.heal = amount;
	}
	public void setElementType(ElementType elementType){
		this.elementType = elementType;
	}
}

package ppbackend.model;

import pplib.exceptions.*;
import ppbackend.model.Game;
import ppbackend.model.Instant;
import ppbackend.model.PlayerContainer;
import ppbackend.model.ElementType;

public class SubAction{
	Game game;
	PlayerContainer me;
	PlayerContainer them;
	Instant instant;
	ElementType elementType = null;
	int damage = 0;
	int heal = 0;

	public SubAction(Game game, int uid, Instant instant) throws PPGameActionException{
		this.me = game.getMeFromUid(uid);
		this.them = game.getThemFromUid(uid);
		this.game = game;
		this.instant = instant;
	}

	public boolean act() throws PPGameActionException{
		this.instant.applyTo(this);
		if(this.instant.isValid(this.game,this)){
			this.them.getPlayer().receiveDamage(this.damage);
			this.me.getPlayer().receiveHeal(this.heal);
			return true;
		}
		else{
			return false;
		}
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

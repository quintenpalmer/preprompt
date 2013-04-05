package ppbackend.model;

import pplib.exceptions.*;
import ppbackend.model.Game;
import ppbackend.model.Instant;
import ppbackend.model.PlayerContainer;
import ppbackend.model.ElementType;

public class ActionSub{
	Game game;
	PlayerContainer me;
	PlayerContainer them;
	ElementType elementType = null;
	int damage = 0;
	int heal = 0;

	public ActionSub(Game game, int uid, Instant instant) throws PPGameActionException{
		this.me = game.getMeFromUid(uid);
		this.them = game.getThemFromUid(uid);
		this.game = game;
		instant.applyTo(this);
	}

	public void act() throws PPGameActionException{
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

package host.control.gameHandle.perform;

import host.control.gameHandle.cardEffect.EffectAspect;
import host.model.game.HostGame;
import shared.model.list.CLType;
import host.model.list.HostCardList;

/** An Action is performed when a card activates an effect
 */
public class Action{
	EffectAspect type;
	int damage;
	int heal;
	int self;

	public EffectAspect getType(){
		return type;
	}
	public void setType(EffectAspect newType){
		type = newType;
	}

	public int getHeal(){
		return heal;
	}
	public void setHeal(int newHeal){
		heal = newHeal;
	}

	public int getDamage(){
		return damage;
	}
	public void setDamage(int newDamage){
		damage = newDamage;
	}

	public int getPlayer(){
		return self;
	}
	public void setPlayer(int newSelf){
		self = newSelf;
	}

	public void act(HostGame game, int self){
		accountForBoard(game,self);
		game.getThemFromUid(self).getPlayer().changeHealth(-damage);
		game.getMeFromUid(self).getPlayer().changeHealth(heal);
	}

	public void accountForBoard(HostGame game, int self){
		
		HostCardList selfField = game.getMeFromUid(self).getDeck().getCL(CLType.active);
		HostCardList enemyField= game.getThemFromUid(self).getDeck().getCL(CLType.active);
		int enemy = game.getThemFromUid(self).getUid();
		/*
		selfField.accountFor(game, self);
		enemyField.accountFor(game, enemy);
		*/
	}

	public void addAction(Action action){
		heal = action.getHeal();
		type = action.getType();
		damage = action.getDamage();
	}
}

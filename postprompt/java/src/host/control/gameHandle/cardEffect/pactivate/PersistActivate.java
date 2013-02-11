package host.control.gameHandle.cardEffect.pactivate;

import host.model.game.HostGame;

public class PersistActivate {
	PersistActivateEffect paEffect;
	PersistActivateCond paCond;
	public void account(HostGame game, int me){
		if(paCond.isValid(game,me)){
			paEffect.account(game,me);
		}
	}
}

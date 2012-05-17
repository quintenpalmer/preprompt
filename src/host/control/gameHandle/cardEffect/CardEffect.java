package host.control.gameHandle.cardEffect;

import host.control.gameHandle.cardEffect.instant.InstantList;
import host.control.gameHandle.cardEffect.pactivate.PersistActivateList;
import host.control.gameHandle.cardEffect.persist.PersistCondList;
import host.model.game.HostGame;

public class CardEffect{
	InstantList instants;
	PersistCondList persistConds;
	PersistActivateList persistActivates;
	
	public CardEffect(String wtdt){
		instants = new InstantList(1);
		persistConds = new PersistCondList(1);
		persistActivates = new PersistActivateList(1);
	}
	
	public boolean dosePersist(HostGame game, int me){
		return persistConds.persists(game, me);
	}
	public void onActivate(HostGame game, int me){
		instants.onAct(game,me);
	}
	public void onPersistActivate(HostGame game, int me){
		persistActivates.onAct(game,me);
	}
	
	public InstantList getInstants(){
		return instants;
	}
	public PersistCondList getPersistConds(){
		return persistConds;
	}
	public PersistActivateList getPersistActivates(){
		return persistActivates;
	}
}
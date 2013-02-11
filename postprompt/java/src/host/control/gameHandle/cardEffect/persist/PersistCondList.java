package host.control.gameHandle.cardEffect.persist;

import host.model.game.HostGame;

public class PersistCondList {
	PersistCond[] persistCs;
	int next;
	
	public PersistCondList(int size){
		persistCs = new PersistCond[size];
		next = 0;
	}
	
	public void tick(HostGame game, int me){
		for(int i=0;i<next;i++){
			persistCs[i].tick(game, me);
		}
	}
	public void reset(HostGame game, int me){
		for(int i=0;i<next;i++){
			persistCs[i].reset(game, me);
		}
	}
	public boolean persists(HostGame game, int me){
		boolean persists = true;
		for(int i=0;i<next;i++){
			persists &= persistCs[i].persists(game,me);
		}
		return persists;
	}
}

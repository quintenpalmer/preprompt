package host.control.gameHandle.cardEffect.pactivate;

import host.model.game.HostGame;

public class PersistActivateList {
	PersistActivate[] persistAs;
	int next;
	
	public PersistActivateList(int size){
		persistAs = new PersistActivate[size];
		next = 0;
	}
	
	public void onAct(HostGame game, int me){
		for(int i=0;i<next;i++){
			persistAs[i].account(game,me);
		}
	}
}

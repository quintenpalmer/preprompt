package host.control.gameHandle.cardEffect.instant;

import host.model.game.HostGame;

public class InstantList {
	Instant[] instants;
	int next;
	
	public InstantList(int size){
		instants = new Instant[size];
		next = 0;
	}
	
	public void onAct(HostGame game, int me){
		for(int i=0;i<next;i++){
			instants[i].onAct(game,me);
		}
	}
}

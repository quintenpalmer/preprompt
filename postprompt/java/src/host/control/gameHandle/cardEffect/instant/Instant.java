package host.control.gameHandle.cardEffect.instant;

import host.model.game.HostGame;

public class Instant {
	InstantEffect iEffect;
	InstantCond iCond;
	
	public void onAct(HostGame game, int me){
		if(iCond.isValid(game,me)){
			iEffect.perform(game,me);
		}
	}
	public void setCond(InstantCond newICond){
		iCond = newICond;
	}
	public InstantCond getCond(){
		return iCond;
	}
	
	public void setEffect(InstantEffect newIEffect){
		iEffect = newIEffect;
	}
	public InstantEffect getEffect(){
		return iEffect;
	}

}

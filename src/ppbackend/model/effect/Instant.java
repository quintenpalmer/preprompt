package ppbackend.model.effect;

import pplib.exceptions.*;

import ppbackend.model.mainStruct.Game;
import ppbackend.model.action.SubAction;

public class Instant{
	InstantEffect effect;
	InstantCond[] conditions;

	public Instant(InstantEffect effect, InstantCond[] conds){
		this.effect = effect;
		this.conditions = conds;
	}

	public void applyTo(Game game, SubAction subAction) throws PPGameActionException{
		if(this.isValid(game,subAction)){
			this.effect.applyTo(subAction);
		}
		else{
			throw new PPGameActionException("That card is not valid to play now");
		}
	}

	private boolean isValid(Game game,SubAction subAction){
		boolean playable = true;
		for(InstantCond cond : this.conditions){
			playable = playable & cond.isValid(game,subAction);
		}
		return playable;
	}
}

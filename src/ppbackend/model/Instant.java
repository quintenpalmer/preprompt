package ppbackend.model;

import java.util.ArrayList;

import ppbackend.model.*;

public class Instant{
	InstantEffect effect;
	InstantCond[] conditions;

	public Instant(InstantEffect effect, InstantCond[] conds){
		this.effect = effect;
		this.conditions = conds;
	}

	public void applyTo(SubAction action){
		this.effect.applyTo(action);
	}

	public boolean isValid(Game game,SubAction action){
		boolean playable = true;
		for(InstantCond cond : this.conditions){
			playable = playable & cond.isValid(game,action);
		}
		return playable;
	}
}

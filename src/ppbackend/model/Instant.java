package ppbackend.model;

import java.util.ArrayList;

import ppbackend.model.InstantEffect;
import ppbackend.model.InstantCond;

import ppbackend.model.ActionSub;

public class Instant{
	InstantEffect effect;
	InstantCond[] conditions;

	public Instant(InstantEffect effect, InstantCond[] conds){
		this.effect = effect;
		this.conditions = conds;
	}

	public void applyTo(ActionSub action){
		this.effect.applyTo(action);
	}
}

package model;

import java.util.ArrayList;

import model.ActionSub;
import model.Game;
import model.Effect;
import model.effect.Instant;
import model.ElementType;

public class Action{
	ArrayList<ActionSub> actions;
	Game game;
	int uid;

	public Action(Game game, int uid){
		this.actions = new ArrayList<ActionSub>();
		this.game = game;
		this.uid = uid;
	}

	public void addAction(Effect effect){
		for(Instant instant : effect.getInstantList().getInstants()){
			this.actions.add(new ActionSub(game,uid,instant));
		}
	}

	public void act(){
	}

}

package model;

import java.util.*;

import pplib.exceptions.*;

import model.ActionSub;
import model.Game;
import model.Effect;
import model.effect.Instant;
import model.ElementType;

public class Action{
	LinkedList<ActionSub> actions;
	Game game;
	int uid;

	public Action(Game game, int uid){
		this.actions = new LinkedList<ActionSub>();
		this.game = game;
		this.uid = uid;
	}

	public void addAction(Effect effect) throws PPGameActionException{
		for(Instant instant : effect.getInstants()){
			this.actions.add(new ActionSub(game,uid,instant));
		}
	}

	public void act(){
		while(!actions.isEmpty()){
			ActionSub action = actions.poll();
		}
	}

}

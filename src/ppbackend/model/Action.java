package ppbackend.model;

import java.util.*;

import pplib.exceptions.*;

import ppbackend.model.SubAction;
import ppbackend.model.Game;
import ppbackend.model.Effect;
import ppbackend.model.Instant;
import ppbackend.model.ElementType;

public class Action{
	LinkedList<SubAction> actions;
	Game game;
	int uid;

	public Action(Game game, int uid, Effect effect) throws PPGameActionException{
		this.actions = new LinkedList<SubAction>();
		this.game = game;
		this.uid = uid;
		for(Instant instant : effect.getInstants()){
			this.actions.add(new SubAction(game,uid,instant));
		}
	}

	public boolean act() throws PPGameActionException{
		boolean success = true;
		while(!actions.isEmpty()){
			SubAction action = actions.poll();
			success = success & action.act();
		}
		return success;
	}
}

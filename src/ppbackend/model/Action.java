package ppbackend.model;

import java.util.*;

import pplib.exceptions.*;

import ppbackend.model.ActionSub;
import ppbackend.model.Game;
import ppbackend.model.Effect;
import ppbackend.model.Instant;
import ppbackend.model.ElementType;

public class Action{
	LinkedList<ActionSub> actions;
	Game game;
	int uid;

	public Action(Game game, int uid, Effect effect) throws PPGameActionException{
		this.actions = new LinkedList<ActionSub>();
		this.game = game;
		this.uid = uid;
		for(Instant instant : effect.getInstants()){
			this.actions.add(new ActionSub(game,uid,instant));
		}
	}

	public void act() throws PPGameActionException{
		while(!actions.isEmpty()){
			ActionSub action = actions.poll();
			action.act();
		}
	}
}

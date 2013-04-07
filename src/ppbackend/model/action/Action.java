package ppbackend.model.action;

import java.util.*;

import pplib.exceptions.*;

import ppbackend.model.mainStruct.Game;
import ppbackend.model.effect.*;

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

	public void act() throws PPGameActionException{
		//boolean success = true;
		while(!actions.isEmpty()){
			SubAction action = actions.poll();
			//success = success & action.act();
			action.act();
		}
		//return success;
	}
}

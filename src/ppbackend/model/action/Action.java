package ppbackend.model.action;

import java.util.*;

import pplib.exceptions.*;

import ppbackend.model.mainStruct.Game;
import ppbackend.model.effect.*;

public class Action{
	LinkedList<SubAction> actions;

	public Action(Game game, int uid, InstantList ilist) throws PPGameActionException{
		this.actions = new LinkedList<SubAction>();
		for(Instant instant : ilist.getInstants()){
			this.actions.add(new SubAction(game,uid,instant));
		}
	}

	public void act() throws PPGameActionException{
		//boolean success = true;
		while(!actions.isEmpty()){
			//success = success & actions.poll().act();
			actions.poll().act();
		}
		//return success;
	}
}

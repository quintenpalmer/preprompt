package ppbackend.model;

import ppbackend.model.ActionSub;

public interface InstantCond{
	public boolean isValid(Game game, ActionSub action);
}

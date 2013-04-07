package ppbackend.model.effect;

import ppbackend.model.action.SubAction;
import ppbackend.model.mainStruct.Game;

public interface InstantCond{
	public boolean isValid(Game game, SubAction action);
}

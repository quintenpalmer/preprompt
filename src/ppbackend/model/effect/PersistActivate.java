package ppbackend.model.effect;

import ppbackend.model.mainStruct.*;
import ppbackend.model.action.*;

public interface PersistActivate{

	public void applyTo(Game game, SubAction action, int playerType);

}

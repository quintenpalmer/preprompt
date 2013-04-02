package ppbackend.model;

import pplib.exceptions.*;
import ppbackend.model.Game;
import ppbackend.model.Instant;
import ppbackend.model.PlayerContainer;
import ppbackend.model.ElementType;

public class ActionSub{
	Game game;
	PlayerContainer me;
	PlayerContainer them;
	ElementType element = null;
	int damage = 0;
	int heal = 0;

	public ActionSub(Game game, int uid, Instant instant) throws PPGameActionException{
		this.game = game;
		this.me = game.getMeFromUid(uid);
		this.them = game.getThemFromUid(uid);
		instant.applyTo(this);
	}
}

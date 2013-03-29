package model;

import pplib.exceptions.*;
import model.Game;
import model.effect.Instant;
import model.PlayerContainer;
import model.ElementType;

public class ActionSub{
	Game game;
	PlayerContainer me;
	PlayerContainer them;
	ElementType element = null;

	public ActionSub(Game game, int uid, Instant instant) throws PPGameActionException{
		this.game = game;
		this.me = game.getMeFromUid(uid);
		this.them = game.getThemFromUid(uid);
		instant.applyTo(this);
	}
}

package host.control.gameHandle.cardEffect.instant;

import host.model.game.HostGame;

public interface InstantCond {
	public boolean isValid(HostGame game, int me);
}

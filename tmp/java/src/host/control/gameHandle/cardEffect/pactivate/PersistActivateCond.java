package host.control.gameHandle.cardEffect.pactivate;

import host.model.game.HostGame;

public interface PersistActivateCond {
	public boolean isValid(HostGame game, int me);
}

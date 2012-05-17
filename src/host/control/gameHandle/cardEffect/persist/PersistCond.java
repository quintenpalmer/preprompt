package host.control.gameHandle.cardEffect.persist;

import host.model.game.HostGame;

public interface PersistCond {
	public void reset(HostGame game, int me);
	public boolean persists(HostGame game, int me);
	public void tick(HostGame game, int me);
}

package host.control.gameHandle.cardEffect.instant;

import host.control.gameHandle.cardEffect.pactivate.PersistActivateEffect;
import host.model.game.HostGame;

public interface InstantEffect extends PersistActivateEffect{
	public void perform(HostGame game, int me);
}
package ppbackend.model.effect;

import ppbackend.model.action.SubAction;

public interface InstantEffect{
	public void applyTo(SubAction action);
}

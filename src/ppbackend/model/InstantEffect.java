package ppbackend.model;

import ppbackend.model.SubAction;

public interface InstantEffect{
	public void applyTo(SubAction action);
}

package ppbackend.model.effect;

public interface Persist{
	public boolean doesPersist();
	public void tick();
	public void reset();
}

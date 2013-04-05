package ppbackend.model;

public interface Persist{
	public boolean doesPersist();
	public void tick();
	public void reset();
}

package ppbackend.model.effect;

public class InstantList{
	Instant[] instants;
	int[] validPhases;

	public InstantList(Instant[] instants, int[] validPhases){
		this.instants = instants;
		this.validPhases = validPhases;
	}

	public String ppserialize(boolean full){
		return "InstantList";
	}

	public int[] getPhases(){
		return this.validPhases;
	}

	public Instant[] getInstants(){
		return this.instants;
	}
}

package ppbackend.model.effect;

public class PersistActivateList{
	PersistActivate[] pactivates;

	public PersistActivateList(PersistActivate[] pactivates){
		this.pactivates = pactivates;
	}

	public String ppserialize(boolean full){
		return "PersistActivateList";
	}

	public PersistActivate[] getPersistActivates(){
		return this.pactivates;
	}
}

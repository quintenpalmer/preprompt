package ppbackend.model.effect;

import ppbackend.model.*;

public class PersistList{
	Persist[] persistList;

	public PersistList(Persist[] persistList){
		this.persistList = persistList;
	}

	public String xmlOutput(boolean full){
		return "PersistList";
	}

	public boolean doesPersist(){
		boolean doesPersist = true;
		for ( Persist persist : this.persistList){
			doesPersist = doesPersist && persist.doesPersist();
		}
		return doesPersist;
	}

	public void tick(){
		for(Persist persist : this.persistList){
			persist.tick();
		}
	}

	public void reset(){
		for(Persist persist : this.persistList){
			persist.reset();
		}
	}
}

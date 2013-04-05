package ppbackend.model;

import ppbackend.model.*;

public class PersistList{
	Persist[] persistList;
	boolean doesPersist;

	public PersistList(Persist[] persistList, boolean persists){
		this.persistList = persistList;
		this.doesPersist = doesPersist;
	}

	public String xmlOutput(boolean full){
		return "PersistList";
	}

	public boolean doesPersist(){
		return this.doesPersist;
	}
}

package ppbackend.model;

import java.util.*;
import ppbackend.model.Instant;

public class InstantList{
	Instant[] instants;
	int[] validPhases;

	public InstantList(Instant[] instants, int[] validPhases){
		this.instants = instants;
		this.validPhases = validPhases;
	}

	public String xmlOutput(boolean full){
		return "InstantList";
	}

	public int[] getPhases(){
		return this.validPhases;
	}

	public Instant[] getInstants(){
		return this.instants;
	}
}

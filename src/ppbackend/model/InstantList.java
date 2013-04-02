package ppbackend.model;

import java.util.*;
import ppbackend.model.Instant;

public class InstantList{
	ArrayList<Instant> instants;
	int[] validPhases;

	public InstantList(ArrayList<Instant> instants, int[] validPhases){
		this.instants = instants;
		this.validPhases = validPhases;
	}

	public String xmlOutput(boolean full){
		return "InstantList";
	}

	public int[] getPhases(){
		return this.validPhases;
	}

	public ArrayList<Instant> getInstants(){
		return this.instants;
	}
}

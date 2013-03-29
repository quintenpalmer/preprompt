package model.effect;

import java.util.*;
import model.effect.Instant;

public class InstantList{
	ArrayList<Instant> instants;
	int[] validPhases;

	public InstantList(ArrayList<Instant> instants, int[] validPhases){
		this.instants = instants;
		this.validPhases = validPhases;
	}

	public int[] getPhases(){
		return this.validPhases;
	}

	public ArrayList<Instant> getInstants(){
		return this.instants;
	}
}

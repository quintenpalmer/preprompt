package ppbackend.model;

import java.util.ArrayList;

import ppbackend.model.InstantEffect;
import ppbackend.model.InstantCond;

import ppbackend.model.ActionSub;

public class Instant{
	InstantEffect effects;
	ArrayList<InstantCond> conditions;

	public void applyTo(ActionSub action){
	}
}

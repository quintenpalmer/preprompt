package model;

import java.util.*;
import org.w3c.dom.Element;

import pplib.XmlParser;
import pplib.exceptions.*;

import model.Phase;
import model.SuperPhase;

public class ControlState{
	Set<Integer> uids;
	int phase;
	int superPhase;
	int turnOwner;
	boolean hasDrawn;

	public ControlState(Set<Integer> uids){
		this.uids = uids;
		this.phase = Phase.first;
		this.superPhase = SuperPhase.first;
		this.hasDrawn = false;
		this.turnOwner = decideFirstPlayer();
	}

	public ControlState(XmlParser xmlParser, Element element, Set<Integer> uids) throws PPXmlException{
		this.uids = uids;
		this.phase = xmlParser.parseInt(element,"phase");
		this.superPhase = xmlParser.parseInt(element,"super_phase");
		this.hasDrawn = xmlParser.parseBool(element,"has_drawn");
		this.turnOwner = xmlParser.parseInt(element,"turn_owner");
	}

	public String xmlOutput(boolean full) throws PPGameActionException{
		String xml = "<super_phase>"+Integer.toString(this.superPhase)+"</super_phase>";
		xml += "<phase>"+Integer.toString(this.phase)+"</phase>";
		xml += "<has_drawn>"+Boolean.toString(this.hasDrawn)+"</has_drawn>";
		xml += "<turn_owner>"+Integer.toString(this.turnOwner)+"</turn_owner>";
		return xml;
	}

	public void stepPhase() throws PPGameActionException{
		this.phase++;
		if(this.phase > Phase.last){
			this.phase = Phase.last;
			throw new PPGameActionException("Phase went past the last one");
		}
	}

	public void didDraw(){
		this.hasDrawn = true;
	}

	public void toggleTurn() throws PPGameActionException{
		if(this.phase == Phase.post){
			this.phase = Phase.draw;
			this.hasDrawn = false;
		}
		else{
			throw new PPGameActionException("Can only end your turn during the post phase");
		}
	}

	public void exitSetupSuperPhase() throws PPGameActionException{
		verifyGivenSuperPhase(SuperPhase.setup);
		this.superPhase = SuperPhase.main;
	}

	public void exitMainSuperPhase() throws PPGameActionException{
		verifyGivenSuperPhase(SuperPhase.main);
		this.superPhase = SuperPhase.end;
	}

	public void verifyGivenSuperPhase(int superPhase) throws PPGameActionException{
		if(!(this.superPhase == superPhase)){
			throw new PPGameActionException("Wrong super phase");
		}
	}

	public void verifyGivenPhase(int givenPhase) throws PPGameActionException{
		if(!(this.phase == givenPhase)){
			throw new PPGameActionException("Wrong phase");
		}
	}

	public void verifyGivenPhases(ArrayList<Integer> givenPhases) throws PPGameActionException{
		if(!(givenPhases.contains(this.phase))){
			throw new PPGameActionException("Wrong phase");
		}
	}

	public void verifyCanDraw() throws PPGameActionException{
		if(this.hasDrawn){
			throw new PPGameActionException("Already drew this turn");
		}
	}

	public int getSuperPhase(){
		return this.superPhase;
	}
	public int getPhase(){
		return this.phase;
	}
	public int getTurnOwner(){
		return this.turnOwner;
	}

	private int decideFirstPlayer(){
		int who = (int)this.uids.toArray()[0];
		return who;
	}

}

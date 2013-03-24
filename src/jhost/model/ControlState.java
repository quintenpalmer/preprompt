package model;

import org.w3c.dom.Element;

import pplib.XmlParser;
import pplib.exceptions.*;

import model.Phase;
import model.SuperPhase;

public class ControlState{
	int phase;
	int superPhase;
	int turnOwner;
	boolean hasDrawn;

	public ControlState(){
		this.phase = Phase.first;
		this.superPhase = SuperPhase.first;
		this.turnOwner = decideFirstPlayer();
		this.hasDrawn = false;
	}

	public ControlState(XmlParser xmlParser, Element element){
		try{
			this.phase = xmlParser.parseInt(element,"phase");
			this.superPhase = xmlParser.parseInt(element,"super_phase");
			this.turnOwner = xmlParser.parseInt(element,"turn_owner");
			this.hasDrawn = xmlParser.parseBool(element,"has_drawn");
		}
		catch(PPXmlException e){
			System.out.println(e.getMessage());
		}
	}

	public void stepPhase() throws PPGameActionException{
		this.phase++;
		if(this.phase > Phase.last){
			this.phase = Phase.last;
			throw new PPGameActionException("Phase went past the last one");
		}
	}

	public void toggleTurn(int numPlayers) throws PPGameActionException{
		if(this.phase == Phase.post){
			this.turnOwner += 1;
			if(this.turnOwner >= numPlayers){
				this.turnOwner = 0;
			}
			this.phase = Phase.draw;
			this.hasDrawn = false;
		}
		else{
			throw new PPGameActionException("Can only end your turn during the post phase");
		}
	}

	public void exitSetupSuperPhase() throws PPGameActionException{
		if(this.superPhase == SuperPhase.setup){
			this.superPhase = SuperPhase.main;
		}
		else{
			throw new PPGameActionException("Can only be performed in the setup super phase");
		}
	}

	public void exitMainSuperPhase() throws PPGameActionException{
		if(this.superPhase == SuperPhase.main){
			this.superPhase = SuperPhase.end;
		}
		else{
			throw new PPGameActionException("Can only be performed in the main super phase");
		}
	}

	public boolean isGivenPhase(int givenPhase){
		return this.phase == givenPhase;
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
		int who = 0;
		return who;
	}
}

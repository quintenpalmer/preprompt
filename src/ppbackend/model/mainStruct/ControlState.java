package ppbackend.model.mainStruct;

import java.util.*;
import org.w3c.dom.Element;

import pplib.XmlParser;
import pplib.exceptions.*;

public class ControlState{
	int[] uids;
	int phase;
	int superPhase;
	int turnOwner;
	boolean hasDrawn;

	public ControlState(Set<Integer> uids){
		this.uids = new int[uids.size()];
		int i=0;
		for(Integer integer : uids){
			this.uids[i++] = integer;
		}
		this.phase = Phase.first;
		this.superPhase = SuperPhase.first;
		this.hasDrawn = false;
		this.turnOwner = decideFirstPlayer();
	}

	public ControlState(XmlParser xmlParser, Element element, Set<Integer> uids) throws PPXmlException{
		this.uids = new int[uids.size()];
		int i=0;
		for(Integer integer : uids){
			this.uids[i] = integer;
			i++;
		}
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

	private void canDraw(int uid) throws PPGameActionException{
		this.verifyGivenSuperPhase(SuperPhase.main);
		this.verifyCurrentTurnOwner(uid);
		this.verifyGivenPhase(Phase.draw);
		this.verifyHasNotDrawn();
	}

	public void draw(int uid) throws PPGameActionException{
		this.canDraw(uid);
		this.hasDrawn = true;
	}

	private void canStepPhase(int uid) throws PPGameActionException{
		this.verifyGivenSuperPhase(SuperPhase.main);
		this.verifyCurrentTurnOwner(uid);
	}

	public void stepPhase(int uid) throws PPGameActionException{
		this.canStepPhase(uid);
		this.phase++;
		if(this.phase > Phase.last){
			this.phase = Phase.last;
			throw new PPGameActionException("Phase went past the last one");
		}
	}

	private void canToggleTurn(int uid) throws PPGameActionException{
		this.verifyGivenSuperPhase(SuperPhase.main);
		this.verifyCurrentTurnOwner(uid);
		if(! (this.phase == Phase.post)){
			throw new PPGameActionException("Can only end your turn during the post phase");
		}
	}

	public void toggleTurn(int uid) throws PPGameActionException{
		this.canToggleTurn(uid);
		if(this.uids[0] == uid){
			this.turnOwner = uids[1];
		}
		else{
			this.turnOwner = uids[0];
		}
		this.phase = Phase.draw;
		this.hasDrawn = false;
	}

	private void canPlay(int uid, int[] phases) throws PPGameActionException{
		this.verifyGivenSuperPhase(SuperPhase.main);
		this.verifyCurrentTurnOwner(uid);
		this.verifyGivenPhases(phases);
	}

	public void play(int uid, int[] phases) throws PPGameActionException{
		this.canPlay(uid,phases);
	}

	public void exitSetupSuperPhase() throws PPGameActionException{
		this.verifyGivenSuperPhase(SuperPhase.setup);
		this.superPhase = SuperPhase.main;
	}

	public void exitMainSuperPhase() throws PPGameActionException{
		this.verifyGivenSuperPhase(SuperPhase.main);
		this.superPhase = SuperPhase.end;
	}

	private void verifyGivenSuperPhase(int superPhase) throws PPGameActionException{
		if(!(this.superPhase == superPhase)){
			throw new PPGameActionException("Wrong super phase");
		}
	}

	private void verifyGivenPhase(int givenPhase) throws PPGameActionException{
		if(!(this.phase == givenPhase)){
			throw new PPGameActionException("Wrong phase");
		}
	}

	private void verifyGivenPhases(int[] givenPhases) throws PPGameActionException{
		boolean contains = false;
		for(int phase : givenPhases){
			if(phase == this.phase){
				contains = true;
			}
		}
		if(!contains){
			throw new PPGameActionException("Wrong phase");
		}
	}

	private void verifyHasNotDrawn() throws PPGameActionException{
		if(this.hasDrawn){
			throw new PPGameActionException("Already drew this turn");
		}
	}

	private void verifyCurrentTurnOwner(int uid) throws PPGameActionException{
		if(!(this.turnOwner == uid)){
			throw new PPGameActionException("It is not player "+Integer.toString(uid)+"'s turn");
		}
	}

	private int decideFirstPlayer(){
		int who = this.uids[0];
		return who;
	}

}

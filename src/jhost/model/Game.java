package model;

import org.w3c.dom.Element;

import pplib.XmlParser;
import pplib.exceptions.*;

import model.PlayerContainer;
import model.ControlState;


public class Game{
	PlayerContainer[] players;
	ControlState controlState;

	public Game(PlayerContainer p1, PlayerContainer p2){
		this.players = new PlayerContainer[2];
		this.players[0] = p1;
		this.players[1] = p2;
		this.controlState = new ControlState();
	}

	public Game(String xml){
		try{
			XmlParser xmlParser = new XmlParser();
			Element rawElement = xmlParser.createElement(xml);
			Element gameElement = xmlParser.parseElement(rawElement,"game");
			this.players = new PlayerContainer[2];
			this.players[0] = new PlayerContainer(xmlParser,xmlParser.parseElement(gameElement,"me"));
			this.players[1] = new PlayerContainer(xmlParser,xmlParser.parseElement(gameElement,"them"));
			this.controlState = new ControlState(xmlParser,xmlParser.parseElement(gameElement,"control_state"));
		}
		catch(PPXmlException e){
			System.out.println(e.getMessage());
		}
	}

	public String xmlOutput(int uid){
		return "<game>hi</game>";
	}

	public PlayerContainer getMeFromUid(int uid) throws PPGameActionException{
		if(this.players[0].getPlayer().getUid() == uid){
			return this.players[0];
		}
		else if(this.players[1].getPlayer().getUid() == uid){
			return this.players[1];
		}
		else{
			throw new PPGameActionException("Not the uid of a player playing this game");
		}
	}

	public PlayerContainer getThemFromUid(int uid) throws PPGameActionException{
		if(this.players[0].getPlayer().getUid() == uid){
			return this.players[1];
		}
		else if(this.players[1].getPlayer().getUid() == uid){
			return this.players[0];
		}
		else{
			throw new PPGameActionException("Not the uid of a player playing this game");
		}
	}

	public int getIndexFromUid(int uid) throws PPGameActionException{
		if(this.players[0].getPlayer().getUid() == uid){
			return 0;
		}
		else if(this.players[1].getPlayer().getUid() == uid){
			return 1;
		}
		else{
			throw new PPGameActionException("Not the uid of a player playing this game");
		}
	}

	public int getCurrentTurnOwnerUid(){
		return this.players[this.controlState.getTurnOwner()].getPlayer().getUid();
	}

	public void verifyMainSuperPhase() throws PPGameActionException{
		if(!(this.controlState.getSuperPhase() == SuperPhase.main)){
			throw new PPGameActionException("Can only be performed during the main super phase");
		}
	}

	public void verifySetupSuperPhase() throws PPGameActionException{
		if(!(this.controlState.getSuperPhase() == SuperPhase.main)){
			throw new PPGameActionException("Can only be be done during the setup super phase");
		}
	}

	public void verifyCurrentTurnOwner(int uid) throws PPGameActionException{
		if(!(getCurrentTurnOwnerUid() == uid)){
			throw new PPGameActionException("It is not player "+Integer.toString(uid)+"'s turn");
		}
	}

	public int checkGameEnd(){
		int uid=0;
		for(int i=0;i<this.players.length;i++){
			if(this.players[i].getPlayer().getHealth() <= 0){
				if(uid!=0){
					uid = -1;
				}
				else{
					uid = this.players[i].getPlayer().getUid();
				}
			}
		}
		return uid;
	}
}

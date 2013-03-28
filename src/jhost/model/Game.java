package model;

import org.w3c.dom.Element;
import java.util.*;

import pplib.XmlParser;
import pplib.exceptions.*;

import model.ClTypes;
import model.PlayerContainer;
import model.ControlState;
import model.Effect;


public class Game{
	HashMap<Integer,PlayerContainer> players;
	ControlState controlState;

	public Game(PlayerContainer p1, PlayerContainer p2){
		this.players = new HashMap<Integer,PlayerContainer>();
		this.players.put(p1.getPlayer().getUid(),p1);
		this.players.put(p2.getPlayer().getUid(),p2);
		this.controlState = new ControlState(this.players.keySet());
	}

	public Game(String xml){
		try{
			XmlParser xmlParser = new XmlParser();
			Element rawElement = xmlParser.createElement(xml);
			Element gameElement = xmlParser.parseElement(rawElement,"game");
			this.players = new HashMap<Integer,PlayerContainer>();
			PlayerContainer tmpPlayer = new PlayerContainer(xmlParser,xmlParser.parseElement(gameElement,"me"));
			this.players.put(tmpPlayer.getPlayer().getUid(),tmpPlayer);
			tmpPlayer = new PlayerContainer(xmlParser,xmlParser.parseElement(gameElement,"them"));
			this.players.put(tmpPlayer.getPlayer().getUid(),tmpPlayer);
			this.controlState = new ControlState(xmlParser,xmlParser.parseElement(gameElement,"control_state"),this.players.keySet());
		}
		catch(PPXmlException e){
			System.out.println(e.getMessage());
		}
	}

	public String xmlOutput(int meUid) throws PPGameActionException{
		int mePlayerType;
		int themPlayerType;
		boolean full;
		if(meUid == PlayerType.full){
			mePlayerType = PlayerType.full;
			themPlayerType = PlayerType.full;
			full = true;
		}
		else{
			mePlayerType = PlayerType.me;
			themPlayerType = PlayerType.them;
			full = false;
		}

		String xml = "<game>";
		xml += "<me>"+getMeFromUid(meUid).xmlOutput(mePlayerType)+"</me>";
		xml += "<them>"+getThemFromUid(meUid).xmlOutput(themPlayerType)+"</them>";
		xml += "<control_state>"+this.controlState.xmlOutput(full)+"</control_state>";
		xml += "</game>";
		return xml;
	}

	public PlayerContainer getMeFromUid(int uid) throws PPGameActionException{
		if(this.players.containsKey(uid)){
			return this.players.get(uid);
		}
		else{
			throw new PPGameActionException("Not the uid of a player playing this game");
		}
	}

	public PlayerContainer getThemFromUid(int uid) throws PPGameActionException{
		boolean takeNext = false;
		Object[] keys = this.players.keySet().toArray();
		if(keys[0] == uid){
			System.out.println(this.players.get(keys[1]));
			return this.players.get(keys[1]);
		}
		else if(keys[1] == uid){
			System.out.println(keys);
			return this.players.get(keys[0]);
		}
		else{
			throw new PPGameActionException("Not the uid of a player playing this game");
		}
	}

	public void verifyCurrentTurnOwner(int uid) throws PPGameActionException{
		if(!(this.controlState.getTurnOwner() == uid)){
			throw new PPGameActionException("It is not player "+Integer.toString(uid)+"'s turn");
		}
	}

	public int checkGameEnd(){
		int uid=0;
		for(PlayerContainer pc : this.players.values()){
			if(pc.getPlayer().getHealth() <= 0){
				if(uid!=0){
					uid = -1;
				}
				else{
					uid = pc.getPlayer().getUid();
				}
			}
		}
		return uid;
	}

	public void setup() throws PPGameActionException{
		this.controlState.verifyGivenSuperPhase(SuperPhase.setup);
		for(PlayerContainer player : this.players.values()){
			for(int i=0;i<5;i++){
				player.getDeck().draw();
			}
		}
		this.controlState.exitSetupSuperPhase();
	}

	public void draw(int uid) throws PPGameActionException{
		this.controlState.verifyGivenSuperPhase(SuperPhase.main);
		verifyCurrentTurnOwner(uid);
		this.controlState.verifyGivenPhase(Phase.draw);
		this.controlState.verifyCanDraw();
		getMeFromUid(uid).getDeck().draw();
		this.controlState.didDraw();
	}

	public void play(int uid) throws PPGameActionException{
		this.controlState.verifyGivenSuperPhase(SuperPhase.main);
		verifyCurrentTurnOwner(uid);
		//TODO Implement card playing
		int srcList = 1;
		int srcCard = 0;
		PlayerContainer me = getMeFromUid(uid);
		Effect effect = me.getDeck().getCardList(srcList).getCard(srcCard).getEffect();
		this.controlState.verifyGivenPhases(effect.getInstantList().getPhases());
	}

	public void stepPhase(int uid) throws PPGameActionException{
		this.controlState.verifyGivenSuperPhase(SuperPhase.main);
		verifyCurrentTurnOwner(uid);
		this.controlState.stepPhase();
	}

	public void stepTurn(int uid) throws PPGameActionException{
		this.controlState.verifyGivenSuperPhase(SuperPhase.main);
		verifyCurrentTurnOwner(uid);
		this.controlState.toggleTurn();
	}

	public void forfeit(int uid) throws PPGameActionException{
		//TODO Implement forfeit
	}

	public Collection<PlayerContainer> getPlayers(){
		return this.players.values();
	}
}

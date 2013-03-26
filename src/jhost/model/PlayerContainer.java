package model;

import org.w3c.dom.Element;

import pplib.XmlParser;
import pplib.exceptions.*;

import model.Player;
import model.Deck;

public class PlayerContainer{
	Player player;
	Deck deck;

	public PlayerContainer(Player player, Deck deck){
		this.player = player;
		this.deck = deck;
	}

	public PlayerContainer(XmlParser xmlParser, Element element) throws PPXmlException {
		this.player = new Player(xmlParser,xmlParser.parseElement(element,"player"));
		this.deck = new Deck(xmlParser,xmlParser.parseElement(element,"deck"));
	}

	public String xmlOutput(int playerType) throws PPGameActionException{
		String xml = "<player>"+this.player.xmlOutput(playerType)+"</player>";
		xml += "<collection>"+this.deck.xmlOutput(playerType)+"</collection>";
		return xml;
	}

	public Player getPlayer(){
		return this.player;
	}

	public Deck getDeck(){
		return this.deck;
	}
}

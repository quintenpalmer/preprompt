package model;

import org.w3c.dom.Element;

import pplib.XmlParser;
import pplib.exceptions.PPXmlException;

import model.Player;
import model.Deck;

public class PlayerContainer{
	Player player;
	Deck deck;

	public PlayerContainer(Player player, Deck deck){
		this.player = player;
		this.deck = deck;
	}

	public PlayerContainer(XmlParser xmlParser, Element element){
		try{
			this.player = new Player(xmlParser,xmlParser.parseElement(element,"player"));
			this.deck = new Deck(xmlParser,xmlParser.parseElement(element,"deck"));
		}
		catch(PPXmlException e){
			System.out.println(e.getMessage());
		}
	}

	public Player getPlayer(){
		return this.player;
	}
}

package model;

import org.w3c.dom.Element;

import pplib.XmlParser;
import pplib.exceptions.*;

import model.Visibility;
import model.CardList;
import model.Card;
import model.ClTypes;

public class Deck{
	CardList[] cardLists;
	Visibility visibility;

	public Deck(Card[] cards){
		this.cardLists = new CardList[ClTypes.size];
		this.cardLists[ClTypes.deck] = new CardList(cards);
		for(int i=1;i<ClTypes.size;i++){
			this.cardLists[i] = new CardList();
		}
		this.visibility = new Visibility();
	}

	public Deck(XmlParser xmlParser, Element element){
		try{
			this.cardLists = new CardList[ClTypes.size];
			this.cardLists[ClTypes.deck] = new CardList(xmlParser,xmlParser.parseElement(element,"deck"));
			this.cardLists[ClTypes.hand] = new CardList(xmlParser,xmlParser.parseElement(element,"hand"));
			this.cardLists[ClTypes.active] = new CardList(xmlParser,xmlParser.parseElement(element,"active"));
			this.cardLists[ClTypes.grave] = new CardList(xmlParser,xmlParser.parseElement(element,"grave"));
			this.cardLists[ClTypes.special] = new CardList(xmlParser,xmlParser.parseElement(element,"special"));
			this.cardLists[ClTypes.other] = new CardList(xmlParser,xmlParser.parseElement(element,"other"));
			this.visibility = new Visibility(xmlParser,xmlParser.parseElement(element,"visibilities"));
		}
		catch(PPXmlException e){
			System.out.println(e.getMessage());
		}
	}

	public void draw() throws PPGameActionException{
		this.cardLists[ClTypes.hand].push(this.cardLists[ClTypes.deck].pop(-1));
	}

	public void playToActive(int cardId) throws PPGameActionException{
		this.cardLists[ClTypes.active].push(this.cardLists[ClTypes.hand].pop(cardId));
	}

	public void playToGrave(int cardId) throws PPGameActionException{
		this.cardLists[ClTypes.grave].push(this.cardLists[ClTypes.hand].pop(cardId));
	}
}

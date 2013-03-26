package model;

import org.w3c.dom.Element;

import pplib.XmlParser;
import pplib.exceptions.*;

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

	public String xmlOutput(int playerType){
		return "";
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

	public CardList getCardList(int clType){
		return this.cardLists[clType];
	}

	private class Visibility{
		boolean[][] visible;

		public Visibility(){
			this.visible = new boolean[ClTypes.size][];
			this.visible = new boolean[][] {
			{true,false,false},
			{true,true,false},
			{true,true,true},
			{true,true,true},
			{true,false,false},
			{true,true,false}};
			/*
			this.visible[ClTypes.deck] = {true,false,false};
			this.visible[ClTypes.hand] = {true,true,false};
			this.visible[ClTypes.active] = {true,true,true};
			this.visible[ClTypes.grave] = {true,true,true};
			this.visible[ClTypes.special] = {true,false,false};
			this.visible[ClTypes.special] = {true,true,false};
			*/
		}

		public Visibility(XmlParser xmlParser, Element element){
			this.visible = new boolean[ClTypes.size][];
			/*
			Element subElement = xmlParser.parseElement(element,cltypes.names[cltypes.deck]);
			this.visible = {true,xmlParser.parseBool(subElement,"me_vis"),xmlParser.parseBool(subElement,"them_vis")};
			subElement = xmlParser.parseElement(element,cltypes.names[cltypes.hand]);
			this.visible = {true,xmlParser.parseBool(subElement,"me_vis"),xmlParser.parseBool(subElement,"them_vis")};
			subElement = xmlParser.parseElement(element,cltypes.names[cltypes.active]);
			this.visible = {true,xmlParser.parseBool(subElement,"me_vis"),xmlParser.parseBool(subElement,"them_vis")};
			subElement = xmlParser.parseElement(element,cltypes.names[cltypes.grave]);
			this.visible = {true,xmlParser.parseBool(subElement,"me_vis"),xmlParser.parseBool(subElement,"them_vis")};
			subElement = xmlParser.parseElement(element,cltypes.names[cltypes.special]);
			this.visible = {true,xmlParser.parseBool(subElement,"me_vis"),xmlParser.parseBool(subElement,"them_vis")};
			subElement = xmlParser.parseElement(element,cltypes.names[cltypes.other]);
			this.visible = {true,xmlParser.parseBool(subElement,"me_vis"),xmlParser.parseBool(subElement,"them_vis")};
			*/
		}
	}
}

package model;

import org.w3c.dom.Element;

import pplib.XmlParser;
import pplib.exceptions.*;

import model.CardList;
import model.Card;
import model.ClTypes;
import model.PlayerType;

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

	public Deck(XmlParser xmlParser, Element element) throws PPXmlException{
		this.cardLists = new CardList[ClTypes.size];
		this.cardLists[ClTypes.deck] = new CardList(xmlParser,xmlParser.parseElement(element,"deck"));
		this.cardLists[ClTypes.hand] = new CardList(xmlParser,xmlParser.parseElement(element,"hand"));
		this.cardLists[ClTypes.active] = new CardList(xmlParser,xmlParser.parseElement(element,"active"));
		this.cardLists[ClTypes.grave] = new CardList(xmlParser,xmlParser.parseElement(element,"grave"));
		this.cardLists[ClTypes.special] = new CardList(xmlParser,xmlParser.parseElement(element,"special"));
		this.cardLists[ClTypes.other] = new CardList(xmlParser,xmlParser.parseElement(element,"other"));
		this.visibility = new Visibility(xmlParser,xmlParser.parseElement(element,"visibilities"));
	}

	public String xmlOutput(int playerType) throws PPGameActionException{
		int visIndex;
		boolean full;
		if(playerType == PlayerType.full){
			visIndex = 0;
			full = true;
		}
		else{
			full = false;
			if(playerType == PlayerType.me){
				visIndex = 1;
			}
			else if(playerType == PlayerType.them){
				visIndex = 2;
			}
			else{
				throw new PPGameActionException("Internal Error invalid player type passed");
			}
		}

		String xml = "<lists>";
		for(int i=0;i<ClTypes.size;i++){
			xml += "<"+ClTypes.names[i]+">";
			xml += this.cardLists[i].xmlOutput(full,this.visibility.doubleIndex(i,visIndex));
			xml += "</"+ClTypes.names[i]+">";
		}
		if(full){
			xml += "<visibilities>";
			xml += this.visibility.xmlOutput();
			xml += "<visibilities>";
		}
		return xml;
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
			this.visible = new boolean[][] {
			{true,false,false},
			{true,true,false},
			{true,true,true},
			{true,true,true},
			{true,false,false},
			{true,true,false}};
		}

		public Visibility(XmlParser xmlParser, Element element) throws PPXmlException{
			Element deckElement = xmlParser.parseElement(element,ClTypes.names[ClTypes.deck]);
			Element handElement = xmlParser.parseElement(element,ClTypes.names[ClTypes.deck]);
			Element activeElement = xmlParser.parseElement(element,ClTypes.names[ClTypes.deck]);
			Element graveElement = xmlParser.parseElement(element,ClTypes.names[ClTypes.deck]);
			Element specialElement = xmlParser.parseElement(element,ClTypes.names[ClTypes.deck]);
			Element otherElement = xmlParser.parseElement(element,ClTypes.names[ClTypes.deck]);
			this.visible = new boolean[][] {
			{true,xmlParser.parseBool(deckElement,"me_vis"),xmlParser.parseBool(deckElement,"them_vis")},
			{true,xmlParser.parseBool(handElement,"me_vis"),xmlParser.parseBool(handElement,"them_vis")},
			{true,xmlParser.parseBool(activeElement,"me_vis"),xmlParser.parseBool(activeElement,"them_vis")},
			{true,xmlParser.parseBool(graveElement,"me_vis"),xmlParser.parseBool(graveElement,"them_vis")},
			{true,xmlParser.parseBool(specialElement,"me_vis"),xmlParser.parseBool(specialElement,"them_vis")},
			{true,xmlParser.parseBool(otherElement,"me_vis"),xmlParser.parseBool(otherElement,"them_vis")}};
		}

		public String xmlOutput(){
			String xml = "";
			for(int i=0;i<ClTypes.size;i++){
				xml += "<"+ClTypes.names[i]+">";
				xml += "<me_vis>"+Boolean.toString(this.visible[i][1])+"</me_vis>";
				xml += "<them_vis>"+Boolean.toString(this.visible[i][2])+"</them_vis>";
				xml += "</"+ClTypes.names[i]+">";
			}
			return xml;
		}

		public boolean doubleIndex(int i, int j){
			return this.visible[i][j];
		}
	}
}

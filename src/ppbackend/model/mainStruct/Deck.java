package ppbackend.model.mainStruct;

import org.w3c.dom.Element;
import java.util.ArrayList;

import pplib.XmlParser;
import pplib.exceptions.*;

import ppbackend.model.shared.CLTypes;

public class Deck{
	CardList[] cardLists;
	Visibility visibility;

	public Deck(ArrayList<Card> cards){
		this.cardLists = new CardList[CLTypes.size];
		this.cardLists[CLTypes.deck] = new CardList(cards);
		for(int i=1;i<CLTypes.size;i++){
			this.cardLists[i] = new CardList();
		}
		this.visibility = new Visibility();
	}

	public Deck(XmlParser xmlParser, Element element) throws PPXmlException{
		this.cardLists = new CardList[CLTypes.size];
		this.cardLists[CLTypes.deck] = new CardList(xmlParser,xmlParser.parseElement(element,"deck"));
		this.cardLists[CLTypes.hand] = new CardList(xmlParser,xmlParser.parseElement(element,"hand"));
		this.cardLists[CLTypes.active] = new CardList(xmlParser,xmlParser.parseElement(element,"active"));
		this.cardLists[CLTypes.grave] = new CardList(xmlParser,xmlParser.parseElement(element,"grave"));
		this.cardLists[CLTypes.special] = new CardList(xmlParser,xmlParser.parseElement(element,"special"));
		this.cardLists[CLTypes.other] = new CardList(xmlParser,xmlParser.parseElement(element,"other"));
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
		for(int i=0;i<CLTypes.size;i++){
			xml += "<"+CLTypes.names[i]+">";
			xml += this.cardLists[i].xmlOutput(full,this.visibility.doubleIndex(i,visIndex));
			xml += "</"+CLTypes.names[i]+">";
		}
		xml += "</lists>";
		if(full){
			xml += "<visibilities>";
			xml += this.visibility.xmlOutput();
			xml += "<visibilities>";
		}
		return xml;
	}

	public void draw() throws PPGameActionException{
		this.cardLists[CLTypes.hand].push(this.cardLists[CLTypes.deck].pop(-1));
	}

	public void playHandToActive(int cardId) throws PPGameActionException{
		this.cardLists[CLTypes.active].push(this.cardLists[CLTypes.hand].pop(cardId));
	}

	public void playHandToGrave(int cardId) throws PPGameActionException{
		this.cardLists[CLTypes.grave].push(this.cardLists[CLTypes.hand].pop(cardId));
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
			Element deckElement = xmlParser.parseElement(element,CLTypes.names[CLTypes.deck]);
			Element handElement = xmlParser.parseElement(element,CLTypes.names[CLTypes.deck]);
			Element activeElement = xmlParser.parseElement(element,CLTypes.names[CLTypes.deck]);
			Element graveElement = xmlParser.parseElement(element,CLTypes.names[CLTypes.deck]);
			Element specialElement = xmlParser.parseElement(element,CLTypes.names[CLTypes.deck]);
			Element otherElement = xmlParser.parseElement(element,CLTypes.names[CLTypes.deck]);
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
			for(int i=0;i<CLTypes.size;i++){
				xml += "<"+CLTypes.names[i]+">";
				xml += "<me_vis>"+Boolean.toString(this.visible[i][1])+"</me_vis>";
				xml += "<them_vis>"+Boolean.toString(this.visible[i][2])+"</them_vis>";
				xml += "</"+CLTypes.names[i]+">";
			}
			return xml;
		}

		public boolean doubleIndex(int i, int j){
			return this.visible[i][j];
		}
	}
}

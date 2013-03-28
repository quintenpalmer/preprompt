package model;

import java.util.ArrayList;
import org.w3c.dom.Element;

import pplib.XmlParser;
import pplib.exceptions.*;

import model.Card;
import model.EmptyCard;

public class CardList{
	ArrayList<Card> cards;

	public CardList(){
		this.cards = new ArrayList<Card>();
	}
	public CardList(ArrayList<Card> cards){
		this.cards = new ArrayList<Card>(cards.size());
		for(Card card : cards){
			this.cards.add(card);
		}
	}
	public CardList(XmlParser xmlParser, Element element) throws PPXmlException{
		Element[] cardElements = xmlParser.parseElements(element,"card");
		this.cards = new ArrayList<Card>(cardElements.length);
		for(int i=0;i<cardElements.length;i++){
			cards.add(new Card(xmlParser,cardElements[i]));
		}
	}

	public String xmlOutput(boolean full, boolean visible){
		String xml = "<cards>";
		for(Card card : this.cards){
			xml += "<card>";
			if(visible){
				xml += card.xmlOutput(full);
			}
			else{
				xml += EmptyCard.xmlOutput;
			}
			xml += "</card>";
		}
		xml += "</cards>";
		return xml;
	}

	public Card pop(int index) throws PPGameActionException{
		try{
			if(index == -1){
				index = this.cards.size()-1;
			}
			return this.cards.remove(index);
		}
		catch(IndexOutOfBoundsException e){
			System.out.println(e.getMessage());
			throw new PPGameActionException("Card List Empty");
		}
	}

	public void push(Card card){
		this.cards.add(card);
	}

	public ArrayList<Card> getCards(){
		return this.cards;
	}

	public Card getCard(int index){
		return this.cards.get(index);
	}

	public void shuffle(){
		//TODO
	}
}

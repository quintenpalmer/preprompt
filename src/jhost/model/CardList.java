package model;

import java.util.ArrayList;
import org.w3c.dom.Element;

import pplib.XmlParser;
import pplib.exceptions.*;

import model.Card;

public class CardList{
	ArrayList<Card> cards;

	public CardList(){
		this.cards = new ArrayList<Card>();
	}
	public CardList(Card[] cards){
		this.cards = new ArrayList<Card>(cards.length);
		for(int i=0;i<cards.length;i++){
			this.cards.add(i,cards[i]);
		}
	}
	public CardList(XmlParser xmlParser, Element element){
		try{
			Element[] cardElements = xmlParser.parseElements(element,"card");
			this.cards = new ArrayList<Card>(cardElements.length);
			for(int i=0;i<cardElements.length;i++){
				cards.add(new Card(xmlParser,cardElements[i]));
			}
		}
		catch(PPXmlException e){
			System.out.println(e.getMessage());
		}
	}

	public String xmlOutput(boolean full, boolean vis){
		return "hi";
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

	public void shuffle(){
	}
}

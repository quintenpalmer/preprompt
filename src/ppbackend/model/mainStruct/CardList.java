package ppbackend.model.mainStruct;

import java.util.*;
import org.w3c.dom.Element;

import pplib.XmlParser;
import pplib.exceptions.*;

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

	public String ppserialize(boolean full, boolean visible){
		String xml = "<cards>";
		for(Card card : this.cards){
			xml += "<card>";
			if(visible){
				xml += card.ppserialize(full);
			}
			else{
				xml += EmptyCard.ppserialize;
			}
			xml += "</card>";
		}
		xml += "</cards>";
		return xml;
	}

	public Card pop(Card card) throws PPGameActionException{
		try{
			this.cards.remove(card);
			return card;
		}
		catch(IndexOutOfBoundsException e){
			throw new PPGameActionException("Card List Empty");
		}
	}

	public Card pop(int index) throws PPGameActionException{
		try{
			if(index == -1){
				index = this.cards.size()-1;
			}
			return this.cards.remove(index);
		}
		catch(IndexOutOfBoundsException e){
			throw new PPGameActionException("Card List Empty "+Integer.toString(index));
		}
	}

	public void push(Card card,int index){
		if(index == -1){
			this.cards.add(card);
		}
		else{
			this.cards.add(index,card);
		}
	}

	public Card getCard(int index) throws PPGameActionException{
		try{
			return this.cards.get(index);
		}
		catch(IndexOutOfBoundsException e){
			throw new PPGameActionException("Card List did not contain that Card");
		}
	}

	public ArrayList<Card> getCards(){
		return this.cards;
	}

	public void shuffle(){
		int startSize = this.cards.size();
		ArrayList<Card> newList = new ArrayList<Card>();
		Random rgen = new Random();
		for(int i=startSize;i>0;i--){
			int r = rgen.nextInt(i);
			newList.add(this.cards.get(r));
			this.cards.remove(r);
		}
		this.cards = newList;
	}
}

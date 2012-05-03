package host.model.list;

import org.w3c.dom.Element;

import shared.control.Parser;
import shared.model.list.CardList;
import host.model.card.HostCard;

/** The model for the list of cards for the host
*/
public class HostCardList{
	// an array of all of the cards in this HostCardList
	HostCard[] cards = null;
	// the number of cards currently in the HostCardList
	int size=0;

	public HostCardList(int newSize){
		size = newSize;
		cards = new HostCard[size];
	}

	/** initializes the CardList to a list of 20 cards
	*/
	// @TODO REMOVE THIS SO THAT YOU DON'T NEED TO START WITH 20 GARBAGE CARDS
	public void init(){
		for(int i=0;i<20;i++){
			this.push(new HostCard(i));
		}
	}

	public HostCard pop(){
		HostCard card = this.cards[this.size-1];
		this.cards[this.size]=null;
		this.size--;
		return card;
	}

	public void push(HostCard card){
		card.setLocation(size);
		this.cards[this.size]=card;
		this.size++;
	}

	public HostCard remove(int cardNumber){
		int i=0;
		int j=0;
		for(i=0;i<this.size;i++){
			if(this.cards[i].getLocation()==cardNumber){
				HostCard card = this.cards[i];
				this.cards[i]=null;
				this.size--;
				for(j=i;j<this.size;j++){
					this.cards[j]=this.cards[j+1];
				}
				return card;
			}
		}
		return null;
	}

	public HostCard view(int index){
		return cards[index];
	}

	/** Unserializes the xml input into a CardList
	* @param ele the element to unserialize
	*/
	public void xmlInput(Element ele){
		Parser parser = new Parser();
		size = parser.eleParseInt(ele,"number");	
		for(int i=0;i<size;i++){
			cards[i] = new HostCard(i);
			cards[i].xmlInput(parser.eleParseElement(ele,"cards"));
		}
	}

	/** Serializes the CardList to an xml string
	* Only contains the individual cards if the CardList both
	* is viewable and contains more than 0 cards
	* @param viewable whether or not this card list can be viewed
	* @return the unique xml string that represents this CardList
	*/
	public String xmlOutput(boolean viewable){
		String xml = "";
		xml += "<visible>";
		if(viewable){
			xml += "true";
		}
		else{
			xml += "false";
		}
		xml += "</visible>";

		xml += "<number>" + size + "</number>";
		if(viewable && size > 0){
			xml += "<cards>";
			if(size>0){
				for(int i=0;i<size;i++){
					xml += view(i).xmlOutput();
				}
			}
			xml += "</cards>";
		}

		return xml;
	}

	/** Serializes the CardList to an xml string
	* Only contains the individual cards if the CardList has more than 0 cards
	* @return the unique xml string that represents this CardList
	*/
	public String xmlOutput() {
		String xml = "";
		xml += "<visible>true</visible>";
		xml += "<number>" + size + "</number>";
		if(size > 0){
			xml += "<cards>";
			if(size>0){
				for(int i=0;i<size;i++){
					xml += view(i).xmlOutput();
				}
			}
			xml += "</cards>";
		}

		return xml;
	}
}

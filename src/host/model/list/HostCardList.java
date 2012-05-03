package host.model.list;

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
		// @TODO REMOVE THIS SO THAT YOU DON'T NEED TO START WITH 20 GARBAGE CARDS
		for(int i=0;i<size;i++){
			this.cards[i]=new HostCard(i);
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

		xml += "<size>" + size + "</size>";
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
}

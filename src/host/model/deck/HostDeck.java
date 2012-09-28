package host.model.deck;

import host.model.list.HostCardList;
import host.model.card.HostCard;
import shared.model.list.CLType;
import shared.model.player.PlayerType;
import shared.model.deck.ListVisibility;

/** A HostDeck is a list of all of a player's card
 * including their hand, grave, active cards, and the remaing stack of cards to draw from
 */
public class HostDeck{
	HostCardList[] cardList;
	ListVisibility meVisible;
	ListVisibility themVisible;

	/** Constructor for the deck, makes an 
	 * empty deck with the given number of cards
	 * @param numCards how many cards deck cardlist should start with
	 * @return the new HostDeck
	 */
	public HostDeck(int numCards){
		meVisible = new ListVisibility(PlayerType.me);
		themVisible = new ListVisibility(PlayerType.them);
		cardList = new HostCardList[4];
		cardList[CLType.stack.i()] = new HostCardList(numCards);
		cardList[CLType.hand.i()] = new HostCardList(0);
		cardList[CLType.active.i()] = new HostCardList(0);
		cardList[CLType.grave.i()] = new HostCardList(0);
	}

	/** serializes the deck into an xml string
	 * @param full whether or not to get a full client
	 * @return the xml string
	 */
	public String xmlOutput(PlayerType pType){
		ListVisibility tempVis;
		if(pType == PlayerType.me){
			tempVis = meVisible;
		}
		else{
			tempVis = themVisible;
		}
		String xml = "";
		xml += "<visible>";
		xml += tempVis.xmlOutput();
		xml += "</visible>";
		xml += "<stack>";
		xml += cardList[CLType.stack.i()].xmlOutput(tempVis.getVisible(0));
		xml += "</stack>";
		xml += "<hand>";
		xml += cardList[CLType.hand.i()].xmlOutput(tempVis.getVisible(1));
		xml += "</hand>";
		xml += "<active>";
		xml += cardList[CLType.active.i()].xmlOutput(tempVis.getVisible(2));
		xml += "</active>";
		xml += "<grave>";
		xml += cardList[CLType.grave.i()].xmlOutput(tempVis.getVisible(3));
		xml += "</grave>";
		return xml;
	}
	
	/** Gets the card list
	 * @param list the type of card list to get
	 * @return the card list
	 */
	public HostCardList getCL(CLType list){
		return cardList[list.i()];
	}

	/** moves a card from one card list to another
	 * @param cardList1 the card list to move from
	 * @param cardList2 the card list to move to
	 */
	public void move(int cardList1, int cardList2){
		HostCard card = cardList[cardList1].pop();
		cardList[cardList2].push(card);
	}

	public void draw(){
		this.move(CLType.stack.i(),CLType.hand.i());
	}
}

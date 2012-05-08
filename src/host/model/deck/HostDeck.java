package host.model.deck;

import host.model.list.HostCardList;
import shared.model.player.PlayerType;
import shared.model.deck.ListVisibility;

/** A HostDeck is a list of all of a player's card
 * including their hand, grave, active cards, and the remaing stack of cards to draw from
 */
public class HostDeck{
	ListVisibility meVisible;
	ListVisibility themVisible;
	HostCardList stack;
	HostCardList hand;
	HostCardList active;
	HostCardList grave;

	/** Constructor for the deck, makes an 
	 * empty deck with the given number of cards
	 * @param numCards how many cards deck cardlist should start with
	 * @return the new HostDeck
	 */
	public HostDeck(int numCards){
		meVisible = new ListVisibility(PlayerType.me);
		themVisible = new ListVisibility(PlayerType.them);
		stack = new HostCardList(numCards);
		active = new HostCardList(0);
		grave = new HostCardList(0);
		hand = new HostCardList(0);
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
		xml += stack.xmlOutput(tempVis.getVisible(0));
		xml += "</stack>";
		xml += "<hand>";
		xml += hand.xmlOutput(tempVis.getVisible(1));
		xml += "</hand>";
		xml += "<active>";
		xml += active.xmlOutput(tempVis.getVisible(2));
		xml += "</active>";
		xml += "<grave>";
		xml += grave.xmlOutput(tempVis.getVisible(3));
		xml += "</grave>";
		return xml;
	}
}

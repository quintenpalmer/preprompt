package host.model.deck;

import host.model.list.HostCardList;
import shared.model.player.PlayerType;
import shared.control.Parser;
import org.w3c.dom.Element;

/** A HostDeck is a list of all of a player's card
 * including their hand, grave, active cards, and the remaing stack of cards to draw from
 */
public class HostDeck{
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
		stack = new HostCardList(numCards);
		active = new HostCardList(0);
		grave = new HostCardList(0);
		hand = new HostCardList(0);
	}

	/** serializes the deck into an xml string
	 * @param full whether or not to get a full client
	 * @return the xml string
	 */
	public String xmlOutput(boolean full){
		String xml = "";
		xml += "<stack>";
		xml += stack.xmlOutput(false);
		xml += "</stack>";
		xml += "<hand>";
		xml += hand.xmlOutput(full);
		xml += "</hand>";
		xml += "<active>";
		xml += active.xmlOutput(true);
		xml += "</active>";
		xml += "<grave>";
		xml += grave.xmlOutput(true);
		xml += "</grave>";
		return xml;
	}
}

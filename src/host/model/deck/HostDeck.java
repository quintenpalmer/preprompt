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
	 * @param pType the type of player this deck corresponds to
	 * @return the xml string
	 */
	public String xmlOutput(PlayerType pType){
		boolean who = false;
		if(pType==PlayerType.me){
			who = true;
		}
		String xml = "";
		xml += "<stack>";
		xml += stack.xmlOutput(false);
		xml += "</stack>";
		xml += "<hand>";
		xml += stack.xmlOutput(who);
		xml += "</hand>";
		xml += "<active>";
		xml += stack.xmlOutput(true);
		xml += "</active>";
		xml += "<grave>";
		xml += stack.xmlOutput(true);
		xml += "</grave>";
		return xml;
	}

	/** reads in a dom element and populates the deck
	 * @param ele the element to populate off of
	 */
	public void xmlInput(Element ele){
		Parser parser = new Parser();
		stack.xmlInput(parser.eleParseElement(ele,"stack"));
		hand.xmlInput(parser.eleParseElement(ele,"hand"));
		active.xmlInput(parser.eleParseElement(ele,"active"));
		grave.xmlInput(parser.eleParseElement(ele,"grave"));
	}
}

package client.model.deck;

import org.w3c.dom.Element;
import shared.control.Parser;
import client.model.list.ClientCardList;
import client.model.list.ClientVisibleCardList;
import client.model.list.ClientNonVisibleCardList;
import shared.model.list.CLType;
import shared.model.player.PlayerType;
import shared.model.deck.ListVisibility;

/** A ClientDeck is a list of all of a player's card
 * including their hand, grave, active cards, and the remaing stack of cards to draw from
 */
public class ClientDeck{
	ListVisibility visible;
	ClientCardList stack;
	ClientCardList hand;
	ClientCardList active;
	ClientCardList grave;

	/** Constructor for the deck, makes an 
	 * empty deck with the given number of cards
	 * @param numCards how many cards deck cardlist should start with
	 * @param pType what type of player this is (me or them)
	 * @return the new ClientDeck
	 */
	public ClientDeck(int numCards, PlayerType pType){
		visible = new ListVisibility(pType);
		stack = new ClientNonVisibleCardList(0);
		active = new ClientVisibleCardList(0);
		grave = new ClientVisibleCardList(0);
		if(pType==PlayerType.me){
			hand = new ClientVisibleCardList(0);
		}
		else{
			hand = new ClientNonVisibleCardList(0);
		}
	}

	/** serializes the deck into an xml string
	 * @return the xml string
	 */
	public String xmlOutput(){
		String xml = "";
		xml += "<visible>";
		xml += visible.xmlOutput();
		xml += "</visible>";
		xml += "<stack>";
		xml += stack.xmlOutput();
		xml += "</stack>";
		xml += "<hand>";
		xml += hand.xmlOutput();
		xml += "</hand>";
		xml += "<active>";
		xml += active.xmlOutput();
		xml += "</active>";
		xml += "<grave>";
		xml += grave.xmlOutput();
		xml += "</grave>";
		return xml;
	}

	public ClientCardList getStack(){
		return stack;
	}

	public ClientCardList getHand(){
		return hand;
	}

	/** reads in a dom element and populates the deck
	 * @param parser the parser used to parse the element
	 * @param ele the element to populate off of
	 */
	public void xmlInput(Parser parser, Element ele){
		visible.xmlInput(parser,parser.eleParseElement(ele,"visible"));
		stack = visible.createCardList(parser, parser.eleParseElement(ele,"stack"), CLType.stack);
		hand = visible.createCardList(parser, parser.eleParseElement(ele,"hand"), CLType.hand);
		active = visible.createCardList(parser, parser.eleParseElement(ele,"active"), CLType.active);
		grave = visible.createCardList(parser, parser.eleParseElement(ele,"grave"), CLType.grave);
	}
}

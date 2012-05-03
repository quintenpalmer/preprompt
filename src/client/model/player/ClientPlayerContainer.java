package client.model.player;

import client.model.deck.ClientDeck;
import shared.model.player.PlayerType;
import shared.control.Parser;
import org.w3c.dom.Element;

public class ClientPlayerContainer{
	ClientPlayer player;
	ClientDeck deck;

	/** Constructor for ClientPlayerContainer
	 * @param name name for the player
	 * @return the new player container
	 */
	public ClientPlayerContainer(String name, PlayerType pType){
		player = new ClientPlayer(name);
		deck = new ClientDeck(20, pType);
	}

	/** unserializes a dom element into a client player container
	 * @param parser the parser to unserialize
	 * @param ele the element to parse
	 */
	public void xmlInput(Parser parser, Element ele){
		player.xmlInput(parser, parser.eleParseElement(ele,"player"));
		deck.xmlInput(parser, parser.eleParseElement(ele,"deck"));
	}

	/** serializes the player into an xml string
	 * @return the xml string
	 */
	public String xmlOutput(){
		String xml = "";
		xml += "<player>";
		xml += player.xmlOutput();
		xml += "</player>";
		xml += "<deck>";
		xml += deck.xmlOutput();
		xml += "</deck>";
		return xml;
	}

	/** Getter for the player
	 * @return the client player
	 */
	public ClientPlayer getPlayer(){
		return player;
	}

	/** Getter for the deck
	 * @return the client deck
	 */
	public ClientDeck getDeck(){
		return deck;
	}
}

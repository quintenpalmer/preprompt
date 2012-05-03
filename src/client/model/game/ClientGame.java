package client.model.game;

import client.model.player.ClientPlayer;
import client.model.deck.ClientDeck;
import shared.control.Parser;

/** The ClientGame is the client's representation of the game
* One player represents the person playing the game
* and the other represents his/her opponent
* There is also a deck for each player, which is a set 
* of list of all of that player's cards
*/
public class ClientGame{

	ClientPlayer playerMe;
	ClientPlayer playerThem;

	ClientDeck playerMeDeck;
	ClientDeck playerThemDeck;

	/** Constructor for the ClientGame
	* @param player1name the name of the self player
	* @param player2name the name of the enemy player
	*/
	public ClientGame(String player1name, String player2name) {
		playerMe = new ClientPlayer(player1name);
		playerThem = new ClientPlayer(player2name);
	}

	/** Gets one of the players (1 is me, 2 is them)
	 * @param which Which player (1 is me, 2 is them)
	 * @return the player
	 */
	public ClientPlayer getPlayer(int which){
		if(which==1){
			return playerMe;
		}
		else if(which==2){
			return playerThem;
		}
		else{
			return null;
		}
	}

	/** used to serialize the game into the xml format
	* @return String that uniquely represents the ClientGame
	*/
	public String xmlOutput(){
		String xml = "";
		xml += "<mePlayer>"; 
		xml += playerMe.xmlOutput();
		xml += "</mePlayer>"; 
		xml += "<themPlayer>"; 
		xml += playerThem.xmlOutput();
		xml += "</themPlayer>"; 
		return xml;
	}

	/** used to unserialze the xml element into a ClientGame
	* @param xml the string that represents the game state
	*/
	public void xmlInput(String xml){
		Parser parser = new Parser();
		playerMe.xmlInput(parser.parseElement(xml,"mePlayer"));
		playerThem.xmlInput(parser.parseElement(xml,"themPlayer"));
	}
}

package client.model.game;

import client.model.player.ClientPlayerContainer;
import shared.model.player.PlayerType;
import shared.control.Parser;

/** The ClientGame is the client's representation of the game
* One player represents the person playing the game
* and the other represents his/her opponent
* There is also a deck for each player, which is a set 
* of list of all of that player's cards
*/
public class ClientGame{

	ClientPlayerContainer playerMe;
	ClientPlayerContainer playerThem;

	/** Constructor for the ClientGame
	* @param player1name the name of the self player
	* @param player2name the name of the enemy player
	*/
	public ClientGame(String player1name, String player2name) {
		playerMe = new ClientPlayerContainer(player1name, PlayerType.me);
		playerThem = new ClientPlayerContainer(player2name, PlayerType.them);
	}

	/** Gets one of the players (1 is me, 2 is them)
	 * @param which Which player (1 is me, 2 is them)
	 * @return the player
	 */
	public ClientPlayerContainer getPlayer(int which){
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

	/** used to unserialze the xml element into a ClientGame
	 * @param parser the parser used to parse the element
	 * @param xml the string that represents the game state
	 */
	public void xmlInput(Parser parser, String xml){
		playerMe.xmlInput(parser,parser.parseElement(xml,"playerMe"));
		playerThem.xmlInput(parser,parser.parseElement(xml,"playerThem"));
	}

	/** serializes the game into an xml string
	 * @return the xml string
	 */
	public String xmlOutput(){
		String xml = "";
		xml += "<playerMe>";
		xml += playerMe.xmlOutput();
		xml += "</playerMe>";
		xml += "<playerThem>";
		xml += playerThem.xmlOutput();
		xml += "</playerThem>";
		return xml;
	}
}

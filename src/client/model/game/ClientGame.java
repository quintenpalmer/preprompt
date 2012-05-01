package client.model.game;

import client.model.player.ClientPlayer;
import shared.control.Parser;
import org.w3c.dom.Element;

/** The ClientGame is the client's representation of the game
* One player represents the person playing the game
* and the other represents his/her opponent
*/
public class ClientGame{

	ClientPlayer playerme;
	ClientPlayer playerthem;

	/** Constructor for the ClientGame
	* @param player1name the name of the self player
	* @param player2name the name of the enemy player
	*/
	public ClientGame(String player1name, String player2name) {
		playerme = new ClientPlayer(player1name);
		playerthem = new ClientPlayer(player2name);
	}

	/** Gets one of the players (1 is self, 2 is enemy)
	 * @param which Which player (1 is self, 2 is enemy)
	 * @return the player
	 */
	public ClientPlayer getPlayer(int which){
		if(which==1){
			return playerme;
		}
		else if(which==2){
			return playerthem;
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
		xml += "<player1>"; 
		xml += playerme.xmlOutput();
		xml += "</player1>";
		xml += "<player2>"; 
		xml += playerthem.xmlOutput();
		xml += "</player2>"; 
		return xml;
	}

	/** used to unserialze the xml element into a ClientGame
	* @param ele the element of the sax xml parser
	*/
	public void xmlInput(Element ele){
		Parser parser = new Parser();
		playerme.xmlInput(parser.eleParseElement(ele,"player"));
		playerthem.xmlInput(parser.eleParseElement(ele,"player"));
	}
}

package client.model;

import client.model.game.ClientGame;
import shared.control.Parser;
import org.w3c.dom.Element;

/** The Model of the M-V-C Pattern
* Stores the state of the game
*/
public class Model{
	// The state of the model
	ClientGame game;

	/** constructor for the Model
	 * @param newState the new state
	 * @return a new Model
	 */
	public Model(int newState){
		game = new ClientGame("vim","emacs");
	}

	/** unserializes an input xml string gamestate into a model
	 * @param xml the string representation of the game state
	 */
	public void xmlInput(String xml){
		Parser parser = new Parser();
		Element ele = parser.parseElement(xml,"game");
		game.xmlInput(ele);
	}
	
	/** serializes the game to an xml string that represents the game state
	 * @return the string that represents the game state
	 */
	public String xmlOutput(){
		String xml = "";
		xml += "<game>";
		xml += game.xmlOutput();
		xml += "</game>";
		return xml;
	}

	/** Gets the game of the model
	 * @return the game of the model
	 */
	public ClientGame getGame(){
		return game;
	}
}

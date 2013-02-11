package client.model;

import client.model.game.ClientGame;
import shared.control.Parser;
import shared.model.constants.Constants;

/** The Model of the M-V-C Pattern
 *	Stores the state of the game
 */
public class Model{
	ClientGame game;

	/** constructor for the Model
	 *	@param newState the new state
	 *	@return a new Model
	 */
	public Model(int newState){
		game = new ClientGame(Constants.me,Constants.them);
	}

	/** unserializes an input xml string gamestate into a model
	 *	@param xml the string representation of the game state
	 */
	public void xmlInput(String xml){
		Parser parser = new Parser();
		game.xmlInput(parser, xml);
	}

	/** serializes the model into an xml string
	 *	@return the xml string
	 */
	public String xmlOutput(){
		String xml = "";
		xml += "<game>";
		xml += game.xmlOutput();
		xml += "</game>";
		return xml;
	}
	
	/** Gets the game of the model
	 *	@return the game of the model
	 */
	public ClientGame getGame(){
		return game;
	}
}

package client.model;

import client.model.card.ClientCard;
import client.model.card.VisibleCard;
import shared.control.Parser;
import org.w3c.dom.Element;

/** The Model of the M-V-C Pattern
* Stores the state of the game
*/
public class Model{
	// The state of the model
	ClientCard card;

	/** constructor for the Model
	* @param newState the new state
	* @return a new Model
	*/
	public Model(int newState){
		card = new VisibleCard(newState);
	}

	/** unserializes an input xml string gamestate into a model
	* @param xml the string representation of the game state
	*/
	public void xmlInput(String xml){
		Parser parser = new Parser();
		Element ele = parser.parseElement(xml,"card");
		card = new VisibleCard(1);
		card.xmlInput(ele);
	}

	/** Gets the card of the model
	* @return the card of the model
	*/
	public ClientCard getCard(){
		return card;
	}
}

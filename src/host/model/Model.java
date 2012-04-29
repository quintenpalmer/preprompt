package host.model;

import host.model.card.HostCard;

/** The Model of the M-V-C Pattern
* Stores the state of the game
*/
public class Model{
	// The state of the model
	HostCard card;

	/** constructor for the Model
	* @param newState the new state
	* @return a new Model
	*/
	public Model(int newState){
		card = new HostCard(newState);
	}

	/** Adds a game to the list of games that the server has
	* @param startInfo string representation of how to load the game
	* TODO Actually load in game
	*/
	public void addGame(String startInfo){
		int i = 0;
	}

	/** serializes the game state into an xml string
	* @return the xml string that represents the game state
	*/
	public String xmlOutput(){
		String xml = "";
		xml += "<game>";
		xml += card.xmlOutput();
		xml += "</game>";
		return xml;
	}
}

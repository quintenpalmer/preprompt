package host.model;

import host.model.game.HostGame;

/** The Model of the M-V-C Pattern
* Stores the state of the game
*/
public class Model{
	// The state of the model
	HostGame game;

	/** constructor for the Model
	* @param newState the new state
	* @return a new Model
	*/
	public Model(int newState){
	}

	/** Adds a game to the list of games that the server has
	* @param startInfo string representation of how to load the game
	* TODO Actually load in game
	*/
	public void addGame(int uid1, int did1,int uid2, int did2){
		game = new HostGame(uid1,did1,uid2,did2);
	}

	/** serializes the game state into an xml string
	 *@param uid the user id of the person requesting the game state
	 * @return the xml string that represents the game state
	 */
	public String xmlOutput(int uid){
		String xml = "";
		xml += "<game>";
		xml += game.xmlOutput(uid);
		xml += "</game>";
		return xml;
	}

	public void draw(int uid){
		game.draw(uid);
	}
}

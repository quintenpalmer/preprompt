package client.model.player;

import org.w3c.dom.Element;
import shared.control.Parser;
import shared.model.constants.Constants;

/** ClientPlayer is the model of a player
* on the client end
*/
public class ClientPlayer{

	String name;
	int health;

	/** Constructor for the ClientPlayer
	* @param name the name of the player to create
	*/
	public ClientPlayer(String newName){
		name = newName;
		health = Constants.startHealth;
	}

	/** used to serialize the player game into the xml format
	* @return String that uniquely represents the ClientPlayer
	*/
	public String xmlOutput(){
		String xml = "";
		xml += "<name>" + name + "</name>";
		xml += "<health>" + health + "</health>";
		return xml;
	}

	/** used to unserialze the xml element into a ClientPlayer
	* @param ele the element of the sax xml parser
	*/
	public void xmlInput(Element ele){
		Parser parser = new Parser();
		name = parser.eleParseString(ele,"name");
		health = parser.eleParseInt(ele,"health");
	}

	/** getter for the player's name
	 * @return the player's name
	 */
	public String getName(){
		return name;
	}

	/** getter for the player's health
	 * @return the player's health
	 */
	public int getHealth(){
		return health;
	}

	/** setter for the player's health
	 * @param newHealth the players new health
	 */
	public void setHealth(int newHealth){
		health = newHealth;
	}
}

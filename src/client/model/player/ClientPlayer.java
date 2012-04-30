package client.model.player;

import org.w3c.dom.Element;

import shared.control.Parser;

/** ClientPlayer is the model of a player
* on the client end
*/
public class ClientPlayer{

	String name;

	/** Constructor for the ClientPlayer
	* @param name the name of the player to create
	*/
	public ClientPlayer(String newName){
		name = newName;
	}

	/** used to serialize the player game into the xml format
	* @return String that uniquely represents the ClientPlayer
	*/
	public String xmlOutput(){
		String xml = "";
		xml += "<name>" + name + "</name>";
		return xml;
	}

	/** used to unserialze the xml element into a ClientPlayer
	* @param ele the element of the sax xml parser
	*/
	public void xmlInput(Element ele){
		Parser parser = new Parser();
		name = parser.eleParseString(ele,"name");
	}
}

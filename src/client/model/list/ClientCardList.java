package client.model.list;

import org.w3c.dom.Element;
import shared.control.Parser;

/** Abstract Class for client card lists 
 * (both visible and nonvisible implement this)
 */
public abstract class ClientCardList{
	int size;

	public ClientCardList(int newSize){
		size = newSize;
	}

	/** reads in an dom Element and populates the card list
	 * @param parser the parser used to parse the element
	 * @param ele the dom Element
	 */
	public void xmlInput(Parser parser, Element ele){
		size = parser.eleParseInt(ele,"size");
	}

	/** serializes the card list into an xml string
	 * @return the xml string
	 */
	public String xmlOutput(){
		String xml = "";
		xml += "<visible>false</visible>";
		xml += "<size>" + size + "</size>";
		return xml;
	}

	/** getter for the size
	 * @return the size
	 */
	public int getSize(){
		return size;
	}
}

package shared.model.deck;

import shared.model.player.PlayerType;
import shared.control.Parser;
import org.w3c.dom.Element;

/** A list of the visibilities of the card lists
 */
public class ListVisibility{
	boolean[] visible;

	/** Constructor for ListVisibility
	 * @param the player type to construct for
	 * @return the ListVisibility
	 */
	public ListVisibility(PlayerType pType){
		visible = new boolean[4];
		visible[0] = false;
		visible[2] = true;
		visible[3] = true;
		if(pType == PlayerType.me){
			visible[1] = true;
		}
		else{
			visible[1] = false;
		}
	}

	/** getter for the visbility
	 * @param the index of the list to get the visibility of
	 * @return whether that list is visible
	 */
	public boolean getVisible(int index){
		return visible[index];
	}

	/** setter for the visbility
	 * @param index the index of the list to set the visibility of
	 * @param vis the visibility to set it to
	 */
	public void getVisibile(int index, boolean vis){
		visible[index] = vis;
	}

	/** serialize the list visibilities to an xml string
	 * @return the xml string
	 */
	public String xmlOutput(){
		String xml = "";
		xml += "<v0>" + visible[0] + "</v0>";
		xml += "<v1>" + visible[1] + "</v1>";
		xml += "<v2>" + visible[2] + "</v2>";
		xml += "<v3>" + visible[3] + "</v3>";
		return xml;
	}

	/** unserializes an xml string into a listvisibility
	 * @param parser the parser to parse the xml string
	 * @param ele the element to parse
	 */
	public void xmlInput(Parser parser, Element ele){
		visible[0] = parser.eleParseBoolean(ele,"v0");
		visible[1] = parser.eleParseBoolean(ele,"v1");
		visible[2] = parser.eleParseBoolean(ele,"v2");
		visible[3] = parser.eleParseBoolean(ele,"v3");
	}
}

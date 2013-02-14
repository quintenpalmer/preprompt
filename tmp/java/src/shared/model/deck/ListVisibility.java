package shared.model.deck;

import shared.model.list.CLType;
import shared.model.player.PlayerType;
import shared.control.Parser;
import org.w3c.dom.Element;
import client.model.list.ClientCardList;
import client.model.list.ClientVisibleCardList;
import client.model.list.ClientNonVisibleCardList;

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
		visible[CLType.stack.i()] = false;
		visible[CLType.active.i()] = true;
		visible[CLType.grave.i()] = true;
		if(pType == PlayerType.me){
			visible[CLType.hand.i()] = true;
		}
		else{
			visible[CLType.hand.i()] = false;
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
		xml += "<" + CLType.stack.str() + ">" + visible[CLType.stack.i()] + "</" + CLType.stack.str() + ">";
		xml += "<" + CLType.hand.str() + ">" + visible[CLType.hand.i()] + "</" + CLType.hand.str() + ">";
		xml += "<" + CLType.active.str() + ">" + visible[CLType.active.i()] + "</" + CLType.active.str() + ">";
		xml += "<" + CLType.grave.str() + ">" + visible[CLType.grave.i()] + "</" + CLType.grave.str() + ">";
		return xml;
	}

	/** unserializes an xml string into a listvisibility
	 * @param parser the parser to parse the xml string
	 * @param ele the element to parse
	 */
	public void xmlInput(Parser parser, Element ele){
		visible[CLType.stack.i()] = parser.eleParseBoolean(ele,CLType.stack.str());
		visible[CLType.hand.i()] = parser.eleParseBoolean(ele,CLType.hand.str());
		visible[CLType.active.i()] = parser.eleParseBoolean(ele,CLType.active.str());
		visible[CLType.grave.i()] = parser.eleParseBoolean(ele,CLType.grave.str());
	}

	/** Creates a new CardList depending on the visibility of the cardList to create
	 * @param parser the parser to pass to create the new CardList
	 * @param ele the element to pass to create the new CardList
	 * @param which which CardList to create
	 * @return the CardList
	 */
	public ClientCardList createCardList(Parser parser, Element ele, CLType which){
		if(visible[which.i()]){
			return new ClientVisibleCardList(parser,ele);
		}
		else{
			return new ClientNonVisibleCardList(parser,ele);
		}
	}
}

package shared.model.deck;

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
		visible[CardListType.stack.getIndex()] = false;
		visible[CardListType.active.getIndex()] = true;
		visible[CardListType.grave.getIndex()] = true;
		if(pType == PlayerType.me){
			visible[CardListType.hand.getIndex()] = true;
		}
		else{
			visible[CardListType.hand.getIndex()] = false;
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
		xml += "<" + CardListType.stack.getString() + ">" + visible[CardListType.stack.getIndex()] + "</" + CardListType.stack.getString() + ">";
		xml += "<" + CardListType.hand.getString() + ">" + visible[CardListType.hand.getIndex()] + "</" + CardListType.hand.getString() + ">";
		xml += "<" + CardListType.active.getString() + ">" + visible[CardListType.active.getIndex()] + "</" + CardListType.active.getString() + ">";
		xml += "<" + CardListType.grave.getString() + ">" + visible[CardListType.grave.getIndex()] + "</" + CardListType.grave.getString() + ">";
		return xml;
	}

	/** unserializes an xml string into a listvisibility
	 * @param parser the parser to parse the xml string
	 * @param ele the element to parse
	 */
	public void xmlInput(Parser parser, Element ele){
		visible[CardListType.stack.getIndex()] = parser.eleParseBoolean(ele,CardListType.stack.getString());
		visible[CardListType.hand.getIndex()] = parser.eleParseBoolean(ele,CardListType.hand.getString());
		visible[CardListType.active.getIndex()] = parser.eleParseBoolean(ele,CardListType.active.getString());
		visible[CardListType.grave.getIndex()] = parser.eleParseBoolean(ele,CardListType.grave.getString());
	}

	/** Creates a new CardList depending on the visibility of the cardList to create
	 * @param parser the parser to pass to create the new CardList
	 * @param ele the element to pass to create the new CardList
	 * @param which which CardList to create
	 * @return the CardList
	 */
	public ClientCardList createCardList(Parser parser, Element ele, CardListType which){
		if(visible[which.getIndex()]){
			return new ClientVisibleCardList(parser,ele);
		}
		else{
			return new ClientNonVisibleCardList(parser,ele);
		}
	}
}

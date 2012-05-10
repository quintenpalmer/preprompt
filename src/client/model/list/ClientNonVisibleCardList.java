package client.model.list;

import shared.control.Parser;
import org.w3c.dom.Element;

/** Class for non-visible card lists
 */
public class ClientNonVisibleCardList extends ClientCardList{

	/** Constructor for non-visible card lists
	 * @param newSize the new size of the card list
	 * @return the new ClientVisibleCardList
	 */
	public ClientNonVisibleCardList(int newSize){
		super(newSize);
	}

	/** Constructor for non-visible card lists
	 * @param parser the parser used to create the new card list
	 * @param ele the element to parser
	 * @return the new ClientVisibleCardList
	 */
	public ClientNonVisibleCardList(Parser parser, Element ele){
		super(0);
		xmlInput(parser,ele);
	}
}

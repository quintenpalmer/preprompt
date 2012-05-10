package client.model.list;

import org.w3c.dom.Element;
import shared.control.Parser;
import client.model.card.ClientVisibleCard;

/** Class for visible card lists
 */
public class ClientVisibleCardList extends ClientCardList{

	ClientVisibleCard[] cards;

	/** Constructor for visible card lists
	 * @param newSize the new size of the card list
	 * @return the new ClientVisibleCardList
	 */
	public ClientVisibleCardList(int newSize){
		super(newSize);
		cards = new ClientVisibleCard[size];
	}

	/** Constructor for visible card lists
	 * @param parser the parser used to create the new card list
	 * @param ele the element to parser
	 * @return the new ClientVisibleCardList
	 */
	public ClientVisibleCardList(Parser parser, Element ele){
		super(0);
		xmlInput(parser,ele);
	}

	/** reads in an dom Element and populates the card list
	 * @param parser the parser used to parse the element
	 * @param ele the dom Element
	 */
	public void xmlInput(Parser parser, Element ele){
		size = parser.eleParseInt(ele,"size");
		cards = new ClientVisibleCard[size];
		for(int i=0;i<size;i++){
			cards[i].xmlInput(parser, parser.eleParseElement(ele,"card"));
		}
	}

	/** serializes the card list into an xml string
	 * @return the xml string
	 */
	public String xmlOutput(){
		String xml = "";
		xml += "<visible>true</visible>";
		xml += "<size>" + size + "</size>";
		for(int i=0;i<size;i++){
			xml += "<card>";
			xml += cards[i].xmlOutput();
			xml += "</card>";
		}
		return xml;
	}
}

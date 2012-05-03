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
	 */
	public ClientVisibleCardList(int newSize){
		super(newSize);
		cards = new ClientVisibleCard[size];
	}

	/** reads in an dom Element and populates the card list
	 * appropriately
	 * @param ele the dom Element
	 */
	public void xmlInput(Element ele){
		Parser parser = new Parser();
		size = parser.eleParseInt(ele,"size");
		for(int i=0;i<size;i++){
			cards[i].xmlInput(parser.eleParseElement(ele,"card"));
		}
	}

	/** serializes the card list into an xml string
	 * @return the xml string
	 */
	public String xmlOutput(){
		String xml = "";
		xml += "<size>" + size + "</size>";
		for(int i=0;i<size;i++){
			xml += "<card>";
			xml += cards[i].xmlOutput();
			xml += "</card>";
		}
		return xml;
	}
}
